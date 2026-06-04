import pandas as pd
from sqlalchemy import select, func

from database.database import DBWriter
from database.models.car_hist_model import CarHistModel
from utils import measure_time


class CarHistRepository:
    def __init__(self, db: DBWriter):
        self.db = db


    @measure_time
    def _get_top_brands(self):
        query = (
            select(CarHistModel.marka)
            .group_by(CarHistModel.marka)
            .order_by(func.count().desc())
            .limit(5)
        )
        with self.db.get_session() as session:
            top_brands = session.execute(query).scalars().all()

        return top_brands


    @measure_time
    def get_top_brands_mean_price_change(self, top_brands: list[str]):
        month = func.date_trunc("month", CarHistModel.date_posted)

        query = (
            select(
                month.label("month"),
                CarHistModel.marka,
                func.avg(CarHistModel.price).label("avg_price"),
            )
            .where(CarHistModel.marka.in_(top_brands))
            .group_by(month, CarHistModel.marka)
            .order_by(month, CarHistModel.marka)
        )

        with self.db.get_session() as session:
            top_brands = session.execute(query).all()

        return pd.DataFrame(top_brands, columns=["month", "marka", "avg_price"])


    @measure_time
    def get_car_mean_price_change(self, marka: str, model: str, generation: int):
        month = func.date_trunc("month", CarHistModel.date_posted)
        query = (
            select(
                month.label("month"),
                CarHistModel.marka,
                CarHistModel.model,
                func.avg(CarHistModel.price).label("avg_price")
            )
            .where(CarHistModel.marka == marka, CarHistModel.model == model, CarHistModel.generation == generation)
            .group_by(month, CarHistModel.marka, CarHistModel.model)
            .order_by(month)
        )

        with self.db.get_session() as session:
            avg_price_for_model = session.execute(query).all()

        return pd.DataFrame(avg_price_for_model, columns=["month", "marka", "model", "avg_price"])


    @measure_time
    def get_top_ru_models(self):
        car_count = func.count(CarHistModel.id).label('car_count')

        query = (
            select(
                CarHistModel.model,
                car_count
            )
            .where(CarHistModel.marka == 'Лада')
            .group_by(CarHistModel.model)
            .order_by(car_count.desc())
            .limit(5)
        )

        with self.db.get_session() as session:
            top_ru_models = session.execute(query).all()
        
        return pd.DataFrame(top_ru_models, columns=['model', 'car_count'])
    

    @measure_time
    def get_top_non_ru_models(self):
        car_count = func.count(CarHistModel.id).label('car_count')

        query = (
            select(
                CarHistModel.model,
                car_count
            )
            .where(CarHistModel.marka != 'Лада')
            .group_by(CarHistModel.model)
            .order_by(car_count.desc())
            .limit(5)
        )

        with self.db.get_session() as session:
            top_ru_models = session.execute(query).all()
        
        return pd.DataFrame(top_ru_models, columns=['model', 'car_count'])

