import plotly.graph_objects as go

COLORS = {
    # Основные цвета графиков (для линий, баров, точек)
    'chart_colors': [
        "#83B5FF",  # blue.default
        '#0DC074',  # green.default
        '#E64056',  # red.default
        '#FFBE18',  # yellow.default
        '#57F5FF',  # из градиента 2
        '#FF57EE',  # из градиента 3
        '#7D9AB1',  # grey1.default
        '#B1BAD3',  # grey5.default
    ],
    
    # Фоны и сетка
    'background': '#22313E',      # grey2.default - основной фон
    'paper_bgcolor': '#0D1E2B',   # grey3.default - фон области графика
    'plot_bgcolor': '#122430',    # grey7.default - фон самой сетки
    
    # Цвета текста и линий
    'text_color': '#FCFEFF',      # whiteGray.default
    'grid_color': '#2F4553',      # grey4.default
    'line_color': '#3C4E5B',      # grey6.default
    
    # Дополнительные акценты
    'highlight': '#3D86F6',       # blue.default для выделений
    'warning': '#FFBE18',         # yellow.default
    'success': '#0DC074',         # green.default
    'error': '#E64056',           # red.default

}

ERROR = '#E64056'

# Базовый шаблон для ВСЕХ графиков
DARK_TEMPLATE = {
    'layout': {
        'paper_bgcolor': COLORS['paper_bgcolor'],
        'plot_bgcolor': COLORS['plot_bgcolor'],
        'font': {'color': COLORS['text_color'], 'family': 'Arial, sans-serif'},
        'xaxis': {
            'gridcolor': COLORS['grid_color'],
            'linecolor': COLORS['line_color'],
            'title_font': {'color': COLORS['text_color']},
            'tickfont': {'color': COLORS['text_color']},
            'zerolinecolor': COLORS['grid_color'],
        },
        'yaxis': {
            'gridcolor': COLORS['grid_color'],
            'linecolor': COLORS['line_color'],
            'title_font': {'color': COLORS['text_color']},
            'tickfont': {'color': COLORS['text_color']},
            'zerolinecolor': COLORS['grid_color'],
        },
        'legend': {
            'font': {'color': COLORS['text_color']},
            'bgcolor': 'rgba(13, 30, 43, 0.8)',  # grey3 с прозрачностью
            'bordercolor': COLORS['grid_color'],
        },
        'title': {
            'font': {'color': COLORS['text_color'], 'size': 16},
            'x': 0.05,
        },
        'hoverlabel': {
            'bgcolor': COLORS['background'],
            'font': {'color': COLORS['text_color']},
            'bordercolor': COLORS['grid_color'],
        },
        'margin': {'t': 50, 'l': 50, 'r': 30, 'b': 50},
        'colorway': COLORS['chart_colors']
    }
}

def apply_theme(fig: go.Figure):
    fig.update_layout(
        **DARK_TEMPLATE['layout'],
        # font = {'color': COLORS['text'], 'family': 'Roboto, sans-serif'},
        # plot_bgcolor = COLORS['surface'],
        
        # colorway = [
        #     COLORS['color1'],
        #     COLORS['color2'],
        #     COLORS['color3'],
        #     COLORS['color4'],
        #     COLORS['color5'],
        # ],
    )

    fig.update_xaxes(
        showgrid = True,
        gridwidth = 1,
        gridcolor = COLORS['grid_color'])
    
    fig.update_yaxes(
        showgrid = True,
        gridwidth = 1,
        gridcolor = COLORS['grid_color'])

    return fig