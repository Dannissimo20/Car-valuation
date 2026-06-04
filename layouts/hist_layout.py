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
                        dbc.Row(dcc.Graph(id="avg-model-price-graph")),
                        dbc.Row(html.H6(id="cars_count")),
                    ],
                    width=6,
                    xs=12,
                    md=6,
                ),
                dbc.Col(
                    [
                        dcc.Dropdown(
                            id="brand-hist-input",
                            options=hist_brands,
                            placeholder="Выберите марку",
                            searchable=True,
                            maxHeight=400,
                            value="Volkswagen",
                            className="form-control mb-3",
                        ),
                        dcc.Dropdown(
                            id="model-hist-input",
                            options=hist_models,
                            placeholder="Выберите модель",
                            searchable=True,
                            maxHeight=400,
                            value="Golf",
                            className="form-control mb-3",
                        ),
                        dcc.Dropdown(
                            id="generation-hist-input",
                            options=hist_models,
                            placeholder="Выберите поклоение",
                            searchable=False,
                            value="1",
                            className="form-control mb-3",
                        ),
                    ],
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
                    dcc.Graph(id="avg-brands-price-graph"),
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
