import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_html_components.Div import Div
import pandas as pd
import plotly.express as px
import pathlib
from app import app

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

data = pd.read_csv(DATA_PATH.joinpath("intro_bees.csv"))
data = data.groupby(["State", "Year", "Affected by", "state_code"])[["Pct of Colonies Impacted"]].mean()
data.reset_index(inplace=True)
# print(data[:5])

cause = data["Affected by"].unique()
states = data["State"].unique()

layout = html.Div([

    html.H1("Web Dashboard for Impacted Bee Colonies", style={'text-align':'center'}),
    html.H3("(Based on Cities and reason of impact)", style={'text-align':'center'}),

    html.Div([
        html.Div([
            html.Pre(children="Choose the cities"),
            dcc.Dropdown(id="select-cities",
                        options=[{'label':x, 'value':x} for x in states],
                        value= ['Alabama'],
                        multi=True,
                        clearable=False,
                        style={'width':'75%'}
                        )
                ], className='six columns'),

        html.Div([
            html.Pre(children="Select the reason"),
            dcc.Dropdown(id="select-reason",
                        options=[{'label':x, 'value':x} for x in cause],
                        value= 'Disease',
                        multi=False,
                        clearable=False,
                        style={'width':'40%'}
                        ),
                ], className='six columns'),
    ], className='row'),

    html.Div(id='container-output', children=[]),
    html.Br(),

    dcc.Graph(id='my-line-chart', figure={})

])

@app.callback(
    [Output(component_id='container-output', component_property='children'),
    Output(component_id='my-line-chart', component_property='figure')],
    [Input(component_id='select-cities', component_property='value'),
    Input(component_id='select-reason', component_property='value')]
)

def line_chart(select_cities, select_reason):
    print(str(select_cities),  str(select_reason))

    container = "Reason is chosen as {}".format(select_reason)

    data_new = data.copy()
    data_new = data_new[data_new["State"].isin(select_cities)]
    data_new = data_new[data_new["Affected by"] == select_reason]

    fig = px.line(
        data_new,
        x= "Year",
        y= "Pct of Colonies Impacted",
        color= "State",
        labels={'Pct of Colonies Impacted':'Percent of Bee colonies impacted'},
        template='plotly_dark'
    )

    return container, fig


