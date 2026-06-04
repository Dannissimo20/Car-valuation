import json

from dash import Output, html, Input
import pandas as pd
import plotly.graph_objects as go
from utils import measure_time

def register_handler(app):
    @app.callback(
        Output('avg-brands-price-graph', 'figure'),
        Output('models-top-ru-output', 'children'),
        Output('models-top-non-ru-output', 'children'),
        Input("hist-data-store", "data")
    )
    @measure_time
    def hist_callback(data):
        brands_fig = go.Figure()

        top_brands = data["top_brands"]
        monthly_avg_by_brand = json.loads(data["monthly_avg_by_brand"])
        monthly_avg_by_brand = pd.DataFrame(monthly_avg_by_brand["data"], index=pd.to_datetime(monthly_avg_by_brand["index"]), columns=monthly_avg_by_brand["columns"])
        top_ru_models = json.loads(data["top_ru_models"])
        top_ru_models = pd.DataFrame(top_ru_models["data"], index=pd.to_datetime(top_ru_models["index"]), columns=top_ru_models["columns"])
        top_non_ru_models = json.loads(data["top_non_ru_models"])
        top_non_ru_models = pd.DataFrame(top_non_ru_models["data"], index=pd.to_datetime(top_non_ru_models["index"]), columns=top_non_ru_models["columns"])

        for brand in top_brands:
            brands_fig.add_trace(
                go.Scatter(
                    x=monthly_avg_by_brand.index,
                    y=monthly_avg_by_brand[brand],
                    mode='lines',
                    name=brand
                )
            )
        
        brands_fig.update_layout(
            title='Изменение средней стоимости 5 самых продаваемых автомобилей',
            xaxis_title='Месяц',
            yaxis_title='Средняя цена',
            template='ggplot2'
        )

        models_top_ru = html.Div([
            html.H3("Самые популярные модели российские"),
            *[
                html.H5(f"{row['model']}: {row['car_count']}")
                for _, row in top_ru_models.iterrows()
            ]
        ])

        models_top_non_ru = html.Div([
            html.H3("Самые популярные модели иномарок"),
            *[
                html.H5(f"{row['model']}: {row['car_count']}")
                for _, row in top_non_ru_models.iterrows()
            ]
        ])

        
        return brands_fig, models_top_ru, models_top_non_ru
