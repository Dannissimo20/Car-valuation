from database.database import DBWriter
from model.model import ModelWrapper
from repo.car_repository import CarRepository


class Container:
    def __init__(self):
        self.db = DBWriter()
        self.car_repo = CarRepository(self.db)
        self.model = ModelWrapper(self.car_repo)