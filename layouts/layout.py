import dash_bootstrap_components as dbc
from dash import html
from layouts.predict_layout import get_predict_layout
from layouts.hist_layout import get_hist_layout

def create_layout():
    return  html.Div([
        dbc.NavbarSimple(brand='Дашборд оценки автомобиля', color='primary', className='car-navbar'),
        dbc.Container([ 
            dbc.Tabs(
                id='car-tabs',
                active_tab='live-car-tab',
                className="car-tabs",
                children=[
                    dbc.Tab(
                        label='Стоимость авто',
                        tab_id='live-car-tab',
                        children=get_predict_layout()
                    ),
                    dbc.Tab(
                        label='Графики',
                        tab_id='hist-car-tab',
                        children=get_hist_layout()
                    )
                ]
            )
        ])
    ])

