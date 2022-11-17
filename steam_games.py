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

fig = px.bar(JoinData, x="Genre", y="Metacritic", barmode="group")

fig2 = px.bar(JoinData, x="Genre", y="RecommendationCount", barmode="group")
#fig2.show()

fig3 = px.bar(JoinData, x="Genre", y="PriceInitial", barmode="group")
#fig3.show()

app.layout = html.Div(children=[
    html.Div([
        html.H1(children='Steam Database'),

        html.Div(children='''
            Recolección de datos acerda de juegos en la plataforma Steam.
        '''),
    
        dcc.Graph(
            id='example-graph',
            figure=fig),
       
    
    ]), 
    html.Div([
         dcc.Graph(
            id='graph2',
            figure=fig2),
            
    ]), 
    html.Div([
         dcc.Graph(
            id='graph3',
            figure=fig3),
    
    ])
],style={'background-color': '#242a44'})