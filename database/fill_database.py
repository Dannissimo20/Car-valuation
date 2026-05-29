from datetime import datetime

import pandas

from database.database import DBWriter
from database.models.car_model import CarModel

start_time = datetime.now()
print(f"Начало работы: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

df = pandas.read_csv(r'C:\Code\car-valuation\datasets\ml_410k.csv')

db = DBWriter()

with db.get_session() as session:
    cars = [CarModel(**row) for row in df.to_dict(orient="records")]
    session.add_all(cars)
    session.commit()

end_time = datetime.now()
print(f"Окончание работы: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Длительность: {end_time - start_time}")
