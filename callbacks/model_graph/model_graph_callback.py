import json

from dash import Output, Input
import pandas as pd
import plotly.graph_objects as go
from utils import measure_time
from lists import hist_models

def register_handler(app):
    @app.callback(
        Output('avg-model-price-graph', 'figure'),
        Output('cars_count', 'children'),
        Input('model-graph-data-store', 'data'),
        Input('brand-hist-input', 'value'),
        Input('model-hist-input', 'value'),
    )
    @measure_time
    def model_graph_callback(data, marka, model):
        monthly_avg_for_model = json.loads(data["monthly_avg_for_model"])
        monthly_avg_for_model = pd.DataFrame(monthly_avg_for_model["data"], index=pd.to_datetime(monthly_avg_for_model["index"]), columns=monthly_avg_for_model["columns"])

        if monthly_avg_for_model.shape[0] % 10 == 1:
            cars_count = f'График построен по {monthly_avg_for_model.shape[0]} объявлению'
        else:
            cars_count = f'График построен по {monthly_avg_for_model.shape[0]} объявлениям'
        
        model_fig = go.Figure(
            data=[go.Scatter(
                x=monthly_avg_for_model['month'],
                y=monthly_avg_for_model['avg_price'],
                name='Цена'
            )]
        )

        model_fig.update_layout(
            title=f'Изменение средней стоимости {marka} {model}',
            xaxis_title='Месяц',
            yaxis_title='Средняя цена',
            template='ggplot2'
        )

        return  model_fig, cars_count,

    @app.callback(
        Output('model-hist-input', 'options'),
        Input('brand-hist-input', 'value')
    )
    def update_model_options(selected_brand):
        if not selected_brand:
            return []

        models = hist_models.get(selected_brand, [])
        return [{'label': model, 'value': model} for model in models]

    @app.callback(
        Output('generation-hist-input', 'options'),
        Output('generation-hist-input', 'value'),
        Input('model-hist-input', 'value'),
        Input('brand-hist-input', 'value')
    )
    def update_generation_options(selected_model, selected_brand):
        if not selected_model:
            return []

        models = hist_models.get(selected_brand, [])
        generations = models[selected_model]

        return [{'label': generation, 'value': generation} for generation in generations], generations[0]
