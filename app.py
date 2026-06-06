from dash import Dash
import dash_bootstrap_components as dbc
from callbacks.hist import hist_callback, hist_data_store
from callbacks.model_graph import model_graph_callback, model_graph_data_store
from deps import Container
from layouts.layout import create_layout
from callbacks import predict_callback
from model.test_model import test_prediction
from dotenv import load_dotenv
import os

load_dotenv()

container = Container(os.getenv("ENV"))

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
app.title = 'Оценка авто'
app.layout = create_layout()

if os.getenv("ENV") == 'DEV':
    test_prediction(container)
predict_callback.register_handler(app, container.model)
hist_data_store.register_callbacks(app, container.car_hist_repo)
model_graph_data_store.register_callbacks(app, container.car_hist_repo)
hist_callback.register_handler(app)
model_graph_callback.register_handler(app)
server = app.server

if __name__ == '__main__':
    app.run(debug=True)