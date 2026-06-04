from dash import Output, Input
from repo.car_hist_repository import CarHistRepository
from utils import measure_time

def register_callbacks(app, cars_hist_repo: CarHistRepository):
    @app.callback(
        Output('model-graph-data-store', 'data'),
        Input('brand-hist-input', 'value'),
        Input('model-hist-input', 'value'),
        Input('generation-hist-input', 'value'),
    )
    @measure_time
    def load_model_graph_store(marka, model, generation):
        monthly_avg_for_model = cars_hist_repo.get_car_mean_price_change(marka, model, generation)

        return {
            "monthly_avg_for_model": monthly_avg_for_model.to_json(date_format="iso", orient="split"),
        }