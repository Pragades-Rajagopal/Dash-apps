import dash
import dash_core_components as dcc
import dash_html_components as html 
from dash.dependencies import Input, Output
import plotly.express as px

app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1("Flight Data Dashboard", style={'text-align':'center'}),

    

])


if __name__ == '__main__':
    app.run_server(debug=True)

