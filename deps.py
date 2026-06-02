from database.database import DBWriter
from model.fitter import Fitter
from model.model import ModelWrapper
from repo.car_repository import CarRepository


class Container:
    def __init__(self, env: str):
        self.db = DBWriter()
        self.car_repo = CarRepository(self.db)
        if env == "DEV":
            self.fitter = Fitter(self.car_repo)
            self.fitter.fit()
        self.model = ModelWrapper()
