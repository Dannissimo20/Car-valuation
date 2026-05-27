from dash import Dash
import dash_bootstrap_components as dbc
from layouts.layout import create_layout
# from utils.data_loader import load_data
from callbacks import callback
from model.test_model import test_prediction

app = Dash(__name__, external_stylesheets=[dbc.themes.MINTY])
app.title = 'Оценка авто'
app.layout = create_layout()

callback.register_handler(app)

test_prediction()

server = app.server

if __name__ == '__main__':
    app.run(debug=True)