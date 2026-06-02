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
                    dbc.Input(
                        id="year-input",
                        placeholder="Введите год выпуска",
                        type="number",
                        value=2016,
                        class_name="mb-3",
                    ),
                    dbc.Input(
                        id="power-input",
                        placeholder="Введите мощность двигателя (л.с)",
                        type="number",
                        value=184,
                        class_name="mb-3",
                    ),
                    dbc.Input(
                        id="mileage-input",
                        placeholder="Введите пробег (км)",
                        type="number",
                        value=165507,
                        class_name="mb-3",
                    ),
                    dcc.Dropdown(
                        id="body-type-input",
                        options=body_types,
                        placeholder="Выберите тип кузова",
                        searchable=False,
                        value="Седан",
                        className="form-control mb-3",
                    ),
                    dcc.Dropdown(
                        id="fuel-type-input",
                        options=fuel_types,
                        placeholder="Выберите тип топлива",
                        searchable=False,
                        value="Бензин",
                        className="form-control mb-3",
                    ),
                    dcc.Dropdown(
                        id="brand-input",
                        options=brands,
                        placeholder="Выберите марку",
                        searchable=True,
                        value="BMW",
                        maxHeight=400,
                        className="form-control mb-3",
                    ),
                    dcc.Dropdown(
                        id="name-input",
                        options=[],
                        placeholder="Выберите модель",
                        searchable=True,
                        value="5-Series",
                        maxHeight=400,
                        className="form-control mb-3",
                    ),
                    dcc.Dropdown(
                        id="transmission-input",
                        options=transmissions,
                        placeholder="Выберите тип трансмиссии",
                        searchable=False,
                        value="АКПП",
                        className="form-control mb-3",
                    ),
                    dcc.Dropdown(
                        id="color-input",
                        options=colors,
                        placeholder="Выберите цвет",
                        searchable=True,
                        value="Черный",
                        className="form-control mb-3",
                    ),
                    html.Button("Подтвердить", id="submit-button"),
                ],
                width=6,
                xs=12,
                md=6,
            ),
        ],
        className="mb-3",
    )
