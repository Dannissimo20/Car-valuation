import os
from pathlib import Path
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error

from repo.car_repository import CarRepository
from utils import measure_time
from dotenv import load_dotenv

load_dotenv()

class Fitter:
    def __init__(self, car_repo: CarRepository):
        self.n_estimators = 500
        self.learning_rate = 0.04
        self.max_depth = 15
        self.subsample = 0.8
        self.colsample_bytree = 0.8
        self.reg_alpha = 0.05
        self.reg_lambda = 0.05
        self.random_state = 42

        self.lower_quantile = 0.1
        self.upper_quantile = 0.9

        self.car_repo = car_repo

        self.MODEL_DIR = Path(os.getenv("MODEL_FILES_PATH"))
        self.MODEL_DIR.mkdir(parents=True, exist_ok=True)


    @measure_time
    def fit(self):
        # Чтение данных из Postgres
        data = self.car_repo.load_model_data()
        cars = pd.DataFrame(data)

        # Определение категориальных признаков и способа кодирования
        self.cat_cols_ord = ['bodyType', 'fuelType', 'transmission', 'color']
        self.cat_cols_freq = ['brand', 'name']

        # Кодирование категориальных признаков с малым количеством категорий
        enc = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
        for col in self.cat_cols_ord:
            cars[col + '_ord'] = enc.fit_transform(cars[[col]])
            # cars['fuel_ord'] = enc.fit_transform(cars[['fuelType']])
            # cars['transmission_ord'] = enc.fit_transform(cars[['transmission']])
            # cars['color_ord'] = enc.fit_transform(cars[['color']])

        # Кодирование категориальных признаков с большим количеством категорий
        for col in self.cat_cols_freq:
            freq = cars[col].value_counts()
            cars[col + '_freq'] = cars[col].map(freq)

        # Создание маппингов для предсказаний
        mappings = {}
        for c in self.cat_cols_ord:
            cats = cars[c].astype(str).unique().tolist()
            mappings[c] = {cat: i for i, cat in enumerate(cats)}
        self.mappings = mappings

        for col in self.cat_cols_freq:
            freq = cars[col].value_counts().to_dict()
            mappings[col] = freq

        # Удаление лишних столбцов
        cars = cars.drop(columns=['engineDisplacement', 'name', 'brand', 'bodyType', 'fuelType', 'transmission', 'location', 'color'])

        # Винсоризация данных
        lower = cars['price'].quantile(self.lower_quantile)
        upper = cars['price'].quantile(self.upper_quantile)
        cars['price'] = cars['price'].clip(lower, upper)

        # Разбиение датасета на целевую переменную и признаки
        X = cars.drop(columns=['price'])
        y = cars['price']

        # Выравнивание признаков
        scaler = StandardScaler()
        X = scaler.fit_transform(X)
        self.scaler = scaler

        # Разбиение на тестовую и трейновую выборки
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42)

        # Логарифмирование целевой переменной для ее сглаживания
        y_train_log = np.log1p(y_train)

        # Создание модели
        model = xgb.XGBRegressor(
            objective='reg:squarederror',
            n_estimators=self.n_estimators,
            learning_rate=self.learning_rate,
            max_depth=self.max_depth,
            subsample=self.subsample,
            colsample_bytree=self.colsample_bytree,
            reg_alpha=self.reg_alpha,
            reg_lambda=self.reg_lambda,
            random_state=self.random_state,
            n_jobs=-1
        )

        # Обучение модели
        model.fit(
            X_train, y_train_log
        )

        self.model = model

        y_pred = np.expm1(model.predict(X_test))
        rmse_test = np.sqrt(mean_squared_error(y_test, y_pred))
        mae_test = mean_absolute_error(y_test, y_pred)
        r2_test = r2_score(y_test, y_pred)

        print(f"Test RMSE: {rmse_test:.2f}, MAE: {mae_test:.2f}, R2: {r2_test:.4f}")

        joblib.dump(mappings, self.MODEL_DIR / 'mappings.joblib')
        joblib.dump(scaler, self.MODEL_DIR / 'scaler.joblib')
        joblib.dump(model, self.MODEL_DIR / 'xgb_regressor.joblib', compress=5)

        del cars
