from datetime import datetime
from .model import ModelWrapper


def test_prediction(model: ModelWrapper):
    recource = [
            {
                'year': 2013,
                'power': 122,
                'mileage': 195600,
                'bodyType': 'Хэтчбек 5 дв.',
                'fuelType': 'Бензин',
                'name': 'Golf',
                'brand': 'Volkswagen',
                'transmission': 'Механика',
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
                'color': 'Серый'
            },
            {
                'year': 2005,
                'power': 110,
                'mileage': 270000,
                'bodyType': 'Седан', 
                'fuelType': 'Бензин', 
                'name': 'Toyota', 
                'brand': 'Corolla', 
                'transmission': 'Механика', 
                'color': 'Серый'
            },
            {
                'year': 2016,
                'power': 249,
                'mileage': 265000,
                'bodyType': 'Седан', 
                'fuelType': 'Бензин', 
                'name': 'Audi', 
                'brand': 'A6', 
                'transmission': 'Робот', 
                'color': 'Черный'
            }
        ]

    prediction = model.predict(recource)

    sample = [950000, 500000, 1580000, 134000, 900000, 460000, 1900000]
    result_lines = []
    model_lines = f"PARAMS:\nn_estimators: {model.n_estimators}\nlearning_rate: {model.learning_rate}\nmax_depth: {model.max_depth}\nsubsample: {model.subsample}\ncolsample_bytree: {model.colsample_bytree}\nreg_alpha: {model.reg_alpha}\nreg_lambda: {model.reg_lambda}\nlower_quantile: {model.lower_quantile}\nupper_quantile: {model.upper_quantile}\n \n"

    prediction = prediction.astype(int)

    print("\n---------------------------------")
    for i, (s, p) in enumerate(zip(sample, prediction)):
        s_fmt = f"{s:,}".replace(",", " ")
        p_fmt = f"{round(p, -3):,}".replace(",", " ")
        line = f"{str(recource[i]['brand']).upper()} {str(recource[i]['name']).upper()} {recource[i]['year']}: образец - {s_fmt}, отклик - {p_fmt}"
        print(line)
        result_lines.append(line)
    print("---------------------------------\n")

    
    with open("results.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M')}\n \n" + model_lines + "\n".join(result_lines) + "\n-------------------------------------------------------\n")
