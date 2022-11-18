from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
Datos = pd.read_csv('/home/PizzaDude/mysite/data/steam.csv')
JoinData = pd.read_csv('/home/PizzaDude/mysite/data/steam_genre.csv')

app.layout = html.Div(children=[
    html.Div([
        html.H1(children='Steam Database'),

        html.Div(children='''
            Recolección de datos acerda de juegos en la plataforma Steam.
        '''),

        dcc.Graph(id='genre_graph'),

        dcc.Dropdown(['Metacritic',
                    'RecommendationCount',
                    'PriceInitial'],
                    id='yaxis-column'
        ),
    ])
])#,style={'background-color': '#242a44'})

@app.callback(
    Output('genre_graph', 'figure'),
    Input('yaxis-column', 'value')
    )
def update_graph(yaxis_column_name):
    fig = px.bar(JoinData, x="Genre",
                y=yaxis_column_name)
    return fig



