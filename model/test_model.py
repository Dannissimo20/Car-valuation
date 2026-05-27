import os
from .model import ModelWrapper
from dotenv import load_dotenv

load_dotenv()


def test_prediction():
    model = ModelWrapper(
        model_path=os.getenv("MODEL_PATH"), 
        maps_path=os.getenv("MAPS_PATH"),
        scaler_path=os.getenv("SCALER_PATH")
    )

    prediction = model.predict(
        [
            {
                'year': 2013,
                'power': 122,
                'mileage': 195600,
                'bodyType': 'Хэтчбек 5 дв.',
                'fuelType': 'Бензин',
                'name': 'Golf',
                'brand': 'Volkswagen',
                'transmission': 'Механика',
                'location': 'Ростов-на-Дону',
                'color': 'Черный'
            },
            {
                'year': 2009,
                'power': 102,
                'mileage': 230000,
                'bodyType': 'Хэтчбек 5 дв.',
                'fuelType': 'Бензин',
                'name': 'Golf',
                'brand': 'Volkswagen',
                'transmission': 'Робот',
                'location': 'Михайловск',
                'color': 'Красный'
            },
            {
                'year': 2016,
                'power': 184,
                'mileage': 165507,
                'bodyType': 'Седан',
                'fuelType': 'Бензин',
                'brand': 'BMW',
                'name': '5-Series',
                'transmission': 'Автомат',
                'location': 'Москва',
                'color': 'Черный'
            },
            {
                'year': 1982,
                'power': 71,
                'mileage': 97000,
                'bodyType': 'Седан',
                'fuelType': 'Бензин',
                'brand': 'Лада',
                'name': '2107',
                'transmission': 'Механика',
                'location': 'Искитим',
                'color': 'Белый'
            },
            {
                'year': 2020, 
                'power': 87, 
                'mileage': 70000, 
                'bodyType': 'Седан', 
                'fuelType': 'Бензин', 
                'name': 'Гранта', 
                'brand': 'Лада', 
                'transmission': 'Механика', 
                'location': 'Киров', 
                'color': 'Серый'
            }
        ]
    )

    print('Образец - [950 000, 600 000, 1 580 000, 134 000, 900 000]\n')
    prediction = prediction.astype(int)
    result = "["
    for res in prediction:
        result += f"{round(res, -3):,.0f}; ".replace(",", " ")
    result += "]"
    print(f'Отклик1 - {result}')
