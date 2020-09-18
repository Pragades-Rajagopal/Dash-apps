import dash
import dash_core_components as dcc
import dash_html_components as html 
from dash.dependencies import Input, Output
import plotly.express as px
import data

app = dash.Dash(__name__)

d = data.data

airline = d['airline'].unique()

app.layout = html.Div([

    html.H1("Flight Data Dashboard", style={'text-align':'center'}),

    html.H4("Select the Airline"),
    dcc.Dropdown(
        id="select-airline",
        options=[{"label":x, "value":x} for x in airline],
        value="American Airlines Inc.",
        style={"width":"40%"},
        multi=False
    )


])


if __name__ == '__main__':
    app.run_server(debug=True)

