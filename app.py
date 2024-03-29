
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from flask import Flask
import socket

server = Flask(__name__)
app = dash.Dash()
dragonData=pd.read_excel("https://github.com/shashisingh5/dashDummy/blob/master/Dragon_details.xlsx?raw=true");



    
print (dragonData['Year']);

trace1 = go.Bar(
    x=dragonData['Year'],
    y=dragonData['Won'],
    name='Goku Won'
)

trace2 = go.Bar(
    x=dragonData['Year'],
    y=dragonData['Loss'],
    name='Goku Loss'
)


app.layout = html.Div([
    dcc.Graph(id='bar_plot',
              figure=go.Figure(data=[trace1,trace2],
                               layout=go.Layout(barmode='stack'))
              )
    ])

host = socket.gethostbyname(socket.gethostname())
app.run_server(debug=False, host=host, port = 8080)

