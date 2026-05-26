import joblib
import pandas as pd
import numpy as np


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
        "location_ord", 
        "color_ord"
    ]

    cat_input_map = {
        'body_ord': 'bodyType',
        'fuel_ord': 'fuelType',
        'name_ord': 'name',
        'brand_ord': 'brand',
        'transmission_ord': 'transmission',
        'location_ord': 'location',
        'color_ord': 'color'
    }


    def __init__(self, model_path: str, maps_path: str, scaler_path: str):
        self.model = joblib.load(model_path)
        self.mappings = joblib.load(maps_path)
        self.scaler = joblib.load(scaler_path)


    def _ensure_df(self, data):
        if isinstance(data, dict):
            return pd.DataFrame([data])
        if isinstance(data, list):
            return pd.DataFrame(data)


    def _prepare(self, raw_df: pd.DataFrame) -> np.ndarray:
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
        X = self._prepare(data)
        preds = np.expm1(self.model.predict(X))
        return preds


model = ModelWrapper(
    model_path=r'C:\Code\Python\Python_Analytic\car-valuation\notebooks\xgb_regressor.joblib', 
    maps_path=r'C:\Code\Python\Python_Analytic\car-valuation\notebooks\ord_mappings.joblib',
    scaler_path=r'C:\Code\Python\Python_Analytic\car-valuation\notebooks\scaler.joblib'
)

prediction = model.predict(
    [
        {
            'year': 2013,
            'power': 122,
            'mileage': 195600,
            'bodyType': 'Хэтчбек 5 дв.',
            'fuelType': 'Бензин',
            'name': 'Golf',
            'brand': 'Volkswagen',
            'transmission': 'Механика',
            'location': 'Ростов-на-Дону',
            'color': 'Черный'
        },
        {
            'year': 2009,
            'power': 102,
            'mileage': 230000,
            'bodyType': 'Хэтчбек 5 дв.',
            'fuelType': 'Бензин',
            'name': 'Golf',
            'brand': 'Volkswagen',
            'transmission': 'Робот',
            'location': 'Михайловск',
            'color': 'Красный'
        },
        {
            'year': 2016,
            'power': 184,
            'mileage': 165507,
            'bodyType': 'Седан',
            'fuelType': 'Бензин',
            'brand': 'BMW',
            'name': '5-Series',
            'transmission': 'Автомат',
            'location': 'Москва',
            'color': 'Черный'
        },
        {
            'year': 1982,
            'power': 71,
            'mileage': 97000,
            'bodyType': 'Седан',
            'fuelType': 'Бензин',
            'brand': 'Лада',
            'name': '2107',
            'transmission': 'Механика',
            'location': 'Искитим',
            'color': 'Белый'
        },
    ]
)
print(prediction.astype(int))