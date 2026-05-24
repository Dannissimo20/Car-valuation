from dash import Dash
import dash_bootstrap_components as dbc
from layouts.layout import create_layout
# from utils.data_loader import load_data
# from callbacks import co_callback, no2_callback, o3_callback, so2_callback, pm2_5_callback, pm10_callback, weather_callback, data_store

app = Dash(__name__, external_stylesheets=[dbc.themes.MINTY])
app.title = 'Оценка авто'
app.layout = create_layout()

server = app.server

if __name__ == '__main__':
    app.run(debug=True)