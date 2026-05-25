from dash import Dash
import dash_bootstrap_components as dbc
from layouts.layout import create_layout
# from utils.data_loader import load_data
from callbacks import callback

app = Dash(__name__, external_stylesheets=[dbc.themes.MINTY])
app.title = 'Оценка авто'
app.layout = create_layout()

callback.register_handler(app)

server = app.server

if __name__ == '__main__':
    app.run(debug=True)