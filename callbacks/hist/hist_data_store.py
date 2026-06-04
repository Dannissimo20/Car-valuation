from dash import Output
from repo.car_hist_repository import CarHistRepository
from utils import measure_time

def register_callbacks(app, cars_hist_repo: CarHistRepository):
    @app.callback(
        Output('hist-data-store', 'data')
    )
    @measure_time
    def load_hist_store():
        top_brands = cars_hist_repo._get_top_brands()
        monthly_avg_by_brand = cars_hist_repo.get_top_brands_mean_price_change(top_brands)
        top_ru_models = cars_hist_repo.get_top_ru_models()
        top_non_ru_models = cars_hist_repo.get_top_non_ru_models()

        monthly_avg_by_brand = monthly_avg_by_brand.pivot(
                index="month", columns="marka", values="avg_price"
            )

        return {
            "top_brands": top_brands,
            "monthly_avg_by_brand": monthly_avg_by_brand.to_json(date_format='iso', orient='split'),
            "top_ru_models": top_ru_models.to_json(date_format="iso", orient="split"),
            "top_non_ru_models": top_non_ru_models.to_json(date_format="iso", orient="split")
        }
