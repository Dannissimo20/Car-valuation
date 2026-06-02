from sqlalchemy import Column, Integer, String, Float, DateTime, Text

from database.database import Base

class CarHistModel(Base):
    __tablename__ = "cars_hist"

    id = Column(Integer, primary_key=True, autoincrement=True)

    car_name = Column(Text, nullable=True)
    year = Column(Integer, nullable=True)
    date_posted = Column(DateTime, nullable=True)
    price = Column(Float, nullable=True)
    engine_volume = Column(Float, nullable=True)
    engine_type = Column(Text, nullable=True)
    power = Column(Float, nullable=True)
    transmission = Column(Text, nullable=True)
    drive = Column(Text, nullable=True)
    mileage = Column(Float, nullable=True)
    steering_wheel = Column(Text, nullable=True)
    generation = Column(Integer, nullable=True)
    restyling = Column(Integer, nullable=True)
    body_type = Column(Text, nullable=True)
    city = Column(Text, nullable=True)
    trim = Column(Text, nullable=True)
    marka = Column(Text, nullable=True)
    model = Column(Text, nullable=True)
    year_month = Column(String(20), nullable=True)
