import dash_bootstrap_components as dbc
from dash import dcc, html
from lists import body_types, fuel_types, brands, transmissions, colors


def get_predict_layout():
    return dbc.Row(
        [
            dbc.Col(
                [dbc.Card(id="car-output", body=True, class_name="car-card")],
                width=6,
                xs=12,
                md=6,
            ),
            dbc.Col(
                [
                    html.H5("Введите параметры автомобиля"),
                    html.H6("Год выпуска"),
                    dbc.Input(
                        id="year-input",
                        placeholder="Введите год выпуска",
                        type="number",
                        value=2016,
                        class_name="input",
                    ),
                    html.H6("Мощность двигателя (л.с)"),
                    dbc.Input(
                        id="power-input",
                        placeholder="Введите мощность двигателя (л.с)",
                        type="number",
                        value=184,
                        class_name="input",
                    ),
                    html.H6("Пробег (км)"),
                    dbc.Input(
                        id="mileage-input",
                        placeholder="Введите пробег (км)",
                        type="number",
                        value=165507,
                        class_name="input",
                    ),
                    html.H6("Тип кузова"),
                    dcc.Dropdown(
                        id="body-type-input",
                        options=body_types,
                        placeholder="Выберите тип кузова",
                        searchable=False,
                        value="Седан",
                        className="form-control input dropdown",
                    ),
                    html.H6("Тип топлива"),
                    dcc.Dropdown(
                        id="fuel-type-input",
                        options=fuel_types,
                        placeholder="Выберите тип топлива",
                        searchable=False,
                        value="Бензин",
                        className="form-control input dropdown",
                    ),
                    html.H6("Марка"),
                    dcc.Dropdown(
                        id="brand-input",
                        options=brands,
                        placeholder="Выберите марку",
                        searchable=True,
                        value="BMW",
                        maxHeight=400,
                        className="form-control input dropdown",
                    ),
                    html.H6("Модель"),
                    dcc.Dropdown(
                        id="name-input",
                        options=[],
                        placeholder="Выберите модель",
                        searchable=True,
                        value="5-Series",
                        maxHeight=400,
                        className="form-control input dropdown",
                    ),
                    html.H6("Тип трансмиссии"),
                    dcc.Dropdown(
                        id="transmission-input",
                        options=transmissions,
                        placeholder="Выберите тип трансмиссии",
                        searchable=False,
                        value="АКПП",
                        className="form-control input dropdown",
                    ),
                    html.H6("Цвет"),
                    dcc.Dropdown(
                        id="color-input",
                        options=colors,
                        placeholder="Выберите цвет",
                        searchable=True,
                        value="Черный",
                        className="form-control input dropdown",\
                        style={"marginBottom": "10px"}
                    ),
                    html.Button("Подтвердить", id="submit-button", className="default-button"),
                ],
                style={
                    "display": "flex",
                    "flexDirection": "column",
                    "gap": "6px",
                },
                width=6,
                xs=12,
                md=6,
            ),
        ],
        className="mb-3",
    )
