from dash import Dash
import dash_bootstrap_components as dbc
from deps import Container
from layouts.layout import create_layout
# from utils.data_loader import load_data
from callbacks import callback
from model.test_model import test_prediction
from dotenv import load_dotenv
import os

load_dotenv()

container = Container(os.getenv("ENV"))

app = Dash(__name__, external_stylesheets=[dbc.themes.MINTY])
app.title = 'Оценка авто'
app.layout = create_layout()

if os.getenv("ENV") == 'DEV':
    test_prediction(container)
callback.register_handler(app, container.model)
server = app.server

if __name__ == '__main__':
    app.run(debug=True)