import os
from dash import Input, Output, State, html
from lists import names
from model.model import ModelWrapper
from dotenv import load_dotenv

load_dotenv()


model = ModelWrapper(
            model_path=os.getenv("MODEL_PATH"), 
            maps_path=os.getenv("MAPS_PATH"),
            scaler_path=os.getenv("SCALER_PATH")
        )

def register_handler(app):
    @app.callback(
        Output('car-output', 'children'),
        Input('submit-button', 'n_clicks'),
        State('year-input', 'value'),
        State('power-input', 'value'),
        State('mileage-input', 'value'),
        State('body-type-input', 'value'),
        State('fuel-type-input', 'value'),
        State('brand-input', 'value'),
        State('name-input', 'value'),
        State('transmission-input', 'value'),
        State('location-input', 'value'),
        State('color-input', 'value')
    )
    def predict_price(n_clicks, year, power, mileage, bodyType, fuelType, brand, name, transmission, location, color):      
        features = {
            'year': year,
            'power': power,
            'mileage': mileage,
            'bodyType': bodyType,
            'fuelType': fuelType,
            'name': name,
            'brand': brand,
            'transmission': transmission,
            'location': location,
            'color': color
        }
        print(features)
        result = model.predict(features)
        print(result)

        result = f"{round(result[0], -3):,.0f}".replace(",", " ")
        
        return html.Div([
            html.H3(f"Стоимость для автомобиля: {brand} {name}"),
            html.H5(f"Год - {year}"),
            html.H5(f"Мощность - {power} л.с."),
            html.H5(f"Пробег - {mileage} км"),
            html.H5(f"Город - {location}"),
            html.H4(f"Результат - {result} ₽"),
        ])

    @app.callback(
        Output('name-input', 'options'),
        Input('brand-input', 'value')
    )
    def update_model_options(selected_brand):
        if not selected_brand:
            return []

        models = names.get(selected_brand, [])
        return [{'label': model, 'value': model} for model in models]