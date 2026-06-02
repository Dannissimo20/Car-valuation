from dash import Input, Output, State, html
import plotly.graph_objects as go
from repo.car_hist_repository import CarHistRepository

def register_handler(app, cars_hist_repo: CarHistRepository):
    @app.callback(
        Output('car-hist-output', 'children'),
    )
    def hist_callback():
        result = cars_hist_repo.get_top_brands_mean_price_in_time()
        return result
        # go.Figure(
        #     data=[go.Scatter(x=data["hours"], y=data["temps"], mode='lines+markers', name='Температура')],
        #     layout=go.Layout(title='Температура по часам', xaxis_title='Время', yaxis_title='Температура (°C)')
        # )
