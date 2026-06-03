from dash import Output
import plotly.graph_objects as go
from repo.car_hist_repository import CarHistRepository

def register_handler(app, cars_hist_repo: CarHistRepository):
    @app.callback(
        Output('avg-brand-price-graph', 'figure'),
    )
    def hist_callback():
        fig = go.Figure()
        top_brands = cars_hist_repo._get_top_brands()
        monthly_avg_by_brand = cars_hist_repo.get_top_brands_mean_price_in_time()

        for brand in top_brands:
            fig.add_trace(
                go.Scatter(
                    x=monthly_avg_by_brand.index,
                    y=monthly_avg_by_brand[brand],
                    mode='lines',
                    name=brand
                )
            )
        
        fig.update_layout(
            title='Изменение средней стоимости 5 самых продаваемых автомобилей',
            xaxis_title='Месяц',
            yaxis_title='Средняя цена',
            template='ggplot2'
        )
        
        return fig
