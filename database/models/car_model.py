from sqlalchemy import Column, Integer, String, Float

from database.database import Base

class CarModel(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True)
    brand = Column(String)
    name = Column(String)
    bodyType = Column(String)
    color = Column(String)
    fuelType = Column(String)
    year = Column(Integer)
    mileage = Column(Integer)
    transmission = Column(String)
    power = Column(Integer)
    price = Column(Integer)
    engineDisplacement = Column(Float)
    location = Column(String)
