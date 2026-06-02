from datetime import datetime
import pandas as pd
from sqlalchemy import insert

from database import DBWriter
from models.car_hist_model import CarHistModel

start_time = datetime.now()
print(f"Начало работы: {start_time:%Y-%m-%d %H:%M:%S}")

db = DBWriter()

chunk_size = 30_000
current = 0
temp = pd.read_csv(r'C:\Code\Python\Python_Analytic\car-valuation\datasets\drom_archive_2017-2025_clean.csv')
total = temp.shape[0]
del temp
            
for chunk in pd.read_csv(r'C:\Code\Python\Python_Analytic\car-valuation\datasets\drom_archive_2017-2025_clean.csv', chunksize=chunk_size):
    
    chunk = chunk.astype(object).where(pd.notna(chunk), None)

    records = chunk.to_dict(orient="records")
    
    with db.get_session() as session:
        session.execute(insert(CarHistModel), records)
        session.commit()
    
    current += chunk.shape[0]
    print(f"Загружено строк: {current}/{total}: {round((current/total)*100, 2)}")

end_time = datetime.now()
print(f"Окончание работы: {end_time:%Y-%m-%d %H:%M:%S}")
print(f"Длительность: {end_time - start_time}")