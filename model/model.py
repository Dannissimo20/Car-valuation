import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error


class ModelWrapper:
    required_columns = [
        "year", 
        "mileage", 
        "power", 
        "body_ord", 
        "fuel_ord", 
        "name_ord", 
        "brand_ord",
        "transmission_ord",
        "color_ord"
    ]

    cat_input_map = {
        'body_ord': 'bodyType',
        'fuel_ord': 'fuelType',
        'name_ord': 'name',
        'brand_ord': 'brand',
        'transmission_ord': 'transmission',
        'color_ord': 'color'
    }


    def __init__(self):
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

        # Чтение из файла
        cars = pd.read_csv(r'C:\Code\car-valuation\datasets\ml_410k.csv')

        # Определение категориальных признаков и способа кодирования
        self.cat_cols_ord = ['bodyType', 'fuelType', 'transmission', 'color']
        self.cat_cols_freq = ['brand', 'name']


        enc = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
        cars['body_ord'] = enc.fit_transform(cars[['bodyType']])
        cars['fuel_ord'] = enc.fit_transform(cars[['fuelType']])
        cars['transmission_ord'] = enc.fit_transform(cars[['transmission']])
        cars['color_ord'] = enc.fit_transform(cars[['color']])

        for col in ['brand', 'name']:
            freq = cars[col].value_counts()
            cars[col + '_ord'] = cars[col].map(freq)

        cat_cols = ['bodyType', 'fuelType', 'transmission', 'color']
        mappings = {}
        for c in cat_cols:
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
            X_train, y_train_log,
            eval_set=[(X_test, y_test)],
            verbose=100
        )

        self.model = model

        y_pred = np.expm1(model.predict(X_test))
        rmse_test = np.sqrt(mean_squared_error(y_test, y_pred))
        mae_test = mean_absolute_error(y_test, y_pred)
        r2_test = r2_score(y_test, y_pred)

        print(f"Test RMSE: {rmse_test:.2f}, MAE: {mae_test:.2f}, R2: {r2_test:.4f}")


    def _ensure_df(self, data):
        if isinstance(data, dict):
            return pd.DataFrame([data])
        if isinstance(data, list):
            return pd.DataFrame(data)


    def _prepare_data(self, raw_df: pd.DataFrame) -> np.ndarray:
        df = self._ensure_df(raw_df).copy()

        for ord_col, src_col in self.cat_input_map.items():
            val = df[src_col].astype(str)

            mapping = self.mappings.get(src_col, {})
            mapped = val.map(mapping).fillna(-1).astype(float)
            df[ord_col] = mapped

        X = df[self.required_columns].astype(float).values
        X = self.scaler.transform(X)
        return X


    def predict(self, data):
        """
        data: dict (как ваш пример), или pd.DataFrame, или list[dict]
        возвращает numpy array предсказаний
        """
        X = self._prepare_data(data)
        preds = np.expm1(self.model.predict(X))
        return preds
