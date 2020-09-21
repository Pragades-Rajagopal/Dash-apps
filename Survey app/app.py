import dash
import dash_core_components as dcc
import dash_html_components as html 
from dash.dependencies import Input, Output
import plotly.express as px
import data

app = dash.Dash(__name__)

d = data.data

airline = d['airline'].unique()
year = d['year'].unique()

app.layout = html.Div([

    html.H1("Flight Data Dashboard", style={'text-align':'center'}),

    html.H4("Select the Airline"),
    dcc.Dropdown(
        id="select-airline",
        options=[{"label":x, "value":x} for x in airline],
        value="American Airlines Inc.",
        style={"width":"40%"},
        multi=False
    ),

    html.Div(id="my-container", children=[]),
    html.Br(),

    dcc.Graph(id="my-graph", figure={})

])

@app.callback(
    [Output(component_id="my-container", component_property="children"),
    Output(component_id="my-graph", component_property="figure")],
    [Input(component_id="select-airline", component_property="value")]
)

def graph(airlines):
    print(str(airlines))

    container = "Selected airline is {}".format(airlines)

    d_copy = d.copy()
    d_copy = d_copy[d_copy['airline'] == airlines]

    fig = px.line(
        d_copy,
        x= "distance",
        y= "avgdelay"
    )

    return container, fig

if __name__ == '__main__':
    app.run_server(debug=True)

