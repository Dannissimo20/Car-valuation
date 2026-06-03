import dash_bootstrap_components as dbc
from dash import dcc, html


def get_hist_layout():
    return [
        dbc.Row(
            [
                dbc.Col(
                    html.H4("График по пользовательским параметрам"),
                    width=6,
                    xs=12,
                    md=6,
                ),
                dbc.Col(
                    [dbc.Input("brand"), dbc.Input("model")],
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
                    dcc.Graph(id='avg-brand-price-graph'),
                    width=12,
                    xs=12,
                )
            ],
            className="mb-3",
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.H4("Самые популярные Модели Российские (Топ 5)"),
                    width=6,
                    xs=12,
                    md=6,
                ),
                dbc.Col(
                    html.H4("Самые популярные иномарки (Топ 5)"),
                    width=6,
                    xs=12,
                    md=6,
                ),
            ],
            className="mb-3",
        ),
    ]
