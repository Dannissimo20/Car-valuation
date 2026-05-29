from database.database import DBWriter
from sqlalchemy import select

from database.models.car_model import CarModel
from database.schemas.car_schema import CarSchema
from utils import measure_time

class CarRepository():
    def __init__(self, db: DBWriter):
        self.db = db
    
    @measure_time
    def load_model_data(self):
        with self.db.get_session() as session:
            stmt = select(CarModel)
            data = session.execute(stmt).scalars().all()
            result = [CarSchema.model_validate(item).model_dump() for item in data]
            return result