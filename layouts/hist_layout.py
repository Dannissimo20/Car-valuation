import dash_bootstrap_components as dbc
from dash import dcc, html
from lists import hist_brands, hist_models


def get_hist_layout():
    return [
        dcc.Store(id='hist-data-store', storage_type='memory'),
        dcc.Store(id='model-graph-data-store', storage_type='memory'),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            dcc.Graph(
                                id="avg-model-price-graph",
                                style={'borderRadius': '6px', 'overflow': 'hidden'},
                            ),
                        ),
                        dbc.Row(html.H6(id="cars_count"), class_name='mb-3 cars_count'),
                    ],
                    width=6,
                    xs=12,
                    md=6,
                ),
                dbc.Col(
                    [
                        html.H6("Марка"),
                        dcc.Dropdown(
                            id="brand-hist-input",
                            options=hist_brands,
                            placeholder="Выберите марку",
                            searchable=True,
                            maxHeight=400,
                            value="Volkswagen",
                            className="form-control input dropdown",
                        ),
                        html.H6("Модель"),
                        dcc.Dropdown(
                            id="model-hist-input",
                            options=hist_models,
                            placeholder="Выберите модель",
                            searchable=True,
                            maxHeight=400,
                            value="Golf",
                            className="form-control input dropdown",
                        ),
                        html.H6("Поколение"),
                        dcc.Dropdown(
                            id="generation-hist-input",
                            options=hist_models,
                            placeholder="Выберите поклоение",
                            searchable=False,
                            value="1",
                            className="form-control input dropdown",
                        ),
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
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        dcc.Graph(
                            id="avg-brands-price-graph",
                            style={'borderRadius': '6px', 'overflow': 'hidden'},
                        ),
                    ),
                    
                    width=12,
                    xs=12,
                )
            ],
            className="mb-3",
        ),
        dbc.Row(
            [
                dbc.Col(
                    # html.H4("Самые популярные Модели Российские (Топ 5)"),
                    dbc.Card(id="models-top-ru-output", body=True, class_name="car-card"),
                    width=6,
                    xs=12,
                    md=6,
                ),
                dbc.Col(
                    # html.H4("Самые популярные иномарки (Топ 5)"),
                    dbc.Card(id="models-top-non-ru-output", body=True, class_name="car-card"),
                    width=6,
                    xs=12,
                    md=6,
                ),
            ],
            className="mb-3",
        ),
    ]
