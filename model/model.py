import os
from pathlib import Path
from dotenv import load_dotenv

import joblib
import pandas as pd
import numpy as np

load_dotenv()


class ModelWrapper:
    required_columns = [
        "year", 
        "mileage", 
        "power", 
        "bodyType_ord", 
        "fuelType_ord", 
        "name_freq", 
        "brand_freq",
        "transmission_ord",
        "color_ord"
    ]

    cat_input_map = {
        'bodyType_ord': 'bodyType',
        'fuelType_ord': 'fuelType',
        'name_freq': 'name',
        'brand_freq': 'brand',
        'transmission_ord': 'transmission',
        'color_ord': 'color'
    }


    def __init__(self):
        self.MODEL_DIR = Path(os.getenv("MODEL_FILES_PATH"))
        self.mappings = joblib.load(self.MODEL_DIR / 'mappings.joblib')
        self.scaler = joblib.load(self.MODEL_DIR / 'scaler.joblib')
        self.model = joblib.load(self.MODEL_DIR / 'xgb_regressor.joblib')


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
