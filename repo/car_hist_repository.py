import pandas as pd
from sqlalchemy import select, func

from database.database import DBWriter
from database.models.car_hist_model import CarHistModel


class CarHistRepository:
    def __init__(self, db: DBWriter):
        self.db = db

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

    def get_top_brands_mean_price_in_time(self):
        top_brands = self._get_top_brands()
        query = (
            select(
                func.date_trunc('month', CarHistModel.date_posted).label('month'),
                CarHistModel.marka,
                func.avg(CarHistModel.price).label('avg_price')
            )
            .where(CarHistModel.marka.in_(top_brands))
            .group_by(
                func.date_trunc('month', CarHistModel.date_posted),
                CarHistModel.marka
            )
            .order_by(
                func.date_trunc('month', CarHistModel.date_posted),
                CarHistModel.marka
            )
        )

        with self.db.get_session() as session:
            top_brands = session.execute(query).all()
        
        df = pd.DataFrame(top_brands, columns=['month', 'marka', 'avg_price'])
        monthly_avg_by_brand = df.pivot(index='month', columns='marka', values='avg_price')
        
        return monthly_avg_by_brand
