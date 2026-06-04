import plotly.graph_objects as go

COLORS = {
    'text': '#000000',
    'grid': "#dddddd",
    'surface': '#ffffff',
    'color1':'#5E35B1',
    'color2': '#1E88E5',
    'color3': '#00897B',
    'color4': '#F4511E',
    'color5': '#C0CA33'
}

def apply_theme(fig: go.Figure):
    fig.update_layout(
        font = {'color': COLORS['text'], 'family': 'Roboto, sans-serif'},
        plot_bgcolor = COLORS['surface'],
        colorway = [
            COLORS['color1'],
            COLORS['color2'],
            COLORS['color3'],
            COLORS['color4'],
            COLORS['color5'],
        ],
    )

    fig.update_xaxes(
        showgrid = True,
        gridwidth = 1,
        gridcolor = COLORS['grid'])
    
    fig.update_yaxes(
        showgrid = True,
        gridwidth = 1,
        gridcolor = COLORS['grid'])

    return fig