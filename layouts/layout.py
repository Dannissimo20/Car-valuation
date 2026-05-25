import dash_bootstrap_components as dbc
from dash import dcc, html
from lists import body_types, fuel_types, brands, names, transmissions, locations, colors

def create_layout():
    return dbc.Container([
        dbc.NavbarSimple(brand='Дашборд оценки автомобиля', color='primary', className='car-navbar mb-3'),
        dbc.Row([
            dbc.Col([
                dbc.Card(id='car-output', body=True, class_name='car-card')
            ], width=6, xs=12, md=6),
            
            dbc.Col([
                html.H5('Введите параметры автомобиля'),
                dbc.Input(id='year-input',
                          placeholder='Введите год выпуска',
                          type='number',
                          value=2016,
                          class_name='mb-3'),
                dbc.Input(id='power-input',
                          placeholder='Введите мощность двигателя (л.с)',
                          type='number',
                          value=184,
                          class_name='mb-3'),
                dbc.Input(id='mileage-input',
                          placeholder='Введите пробег (км)',
                          type='number',
                          value=165507,
                          class_name='mb-3'),
                dbc.Select(id='body-type-input',
                           placeholder='Выберите тип кузова',
                           options=body_types,
                           value="Седан",
                           class_name='form-control mb-3'),
                dbc.Select(id='fuel-type-input',
                           placeholder='Выберите тип топлива',
                           options=fuel_types,
                           value="Бензин",
                           class_name='form-control mb-3'),
                dcc.Dropdown(id="brand-input",
                             options=brands,
                             placeholder="Выберите марку",
                             searchable=True,
                             value="BMW",
                             className='form-control mb-3'),
                dcc.Dropdown(id="name-input",
                             options=names,
                             placeholder="Выберите модель",
                             searchable=True,
                             value="5-Series",
                             className='form-control mb-3'),
                dbc.Select(id='transmission-input',
                           placeholder='Выберите тип трансмиссии',
                           options=transmissions,
                           value="АКПП",
                           class_name='form-control mb-3'),
                dcc.Dropdown(id="location-input",
                             options=locations,
                             placeholder="Выберите регион продажи",
                             searchable=True,
                             value="Москва",
                             className='form-control mb-3'),
                dcc.Dropdown(id="color-input",
                             options=colors,
                             placeholder="Выберите цвет",
                             searchable=True,
                             value="Черный",
                             className='form-control mb-3'),
                html.Button('Подтвердить', id='submit-button'),
            ], width=6, xs=12, md=6)
        ], className='mb-3')
    ])