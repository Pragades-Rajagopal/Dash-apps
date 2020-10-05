import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_html_components.Div import Div
import plotly.express as px
import pandas as pd
import pathlib
from app import app

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

df = pd.read_csv(DATA_PATH.joinpath("intro_bees.csv"))
df = df.groupby(['State', 'Affected by', 'Year', 'state_code'])[['Pct of Colonies Impacted']].mean()
df.reset_index(inplace=True)

layout = html.Div([


    html.H1("Web Dashboard for Bee colonies", style={'text-align':'center'}),
    html.H3("(Based on diseases and year of impact)", style={'text-align':'center'}),

    html.Div([
        html.Div([
            html.Pre(children="Select one"),
            dcc.Dropdown(id='select-reason',
                        options=[
                            {'label':'Disease', 'value':'Disease'},
                            {'label':'Varroa Mites', 'value':'Varroa Mites'},
                            {'label':'Pesticides', 'value':'Pesticides'},
                            {'label':'Pest & Varroa', 'value':'Pests and Varroa'},
                            {'label':'Unknown', 'value':'Unknown'},
                            {'label':'Others', 'value':'Other'}
                        ],
                        value='Disease',
                        style={'width':'40%'},
                        clearable=False,
                        multi=False)
        ], className='six columns'),

        html.Div([
            html.Pre(children="Select year"),
            dcc.Dropdown(id='select-year',
                        options=[
                            {'label':'2015', 'value':2015},
                            {'label':'2016', 'value':2016},
                            {'label':'2017', 'value':2017},
                            {'label':'2018', 'value':2018},
                            {'label':'2019', 'value':2019}
                        ],
                        value= 2015,
                        multi=False,
                        clearable=False,
                        style={'width':'40%'}
                        )
         ], className='six columns'),
    ], className='row'),

    html.Div(id='container-output', children=[]),

    html.Br(),

    dcc.Graph(id='my-bar-graph', figure={})

])

@app.callback(
    [Output(component_id='container-output', component_property='children'),
    Output(component_id='my-bar-graph', component_property='figure')],
    [Input(component_id='select-reason', component_property='value'),
    Input(component_id='select-year', component_property='value')]
)

def show_bar(reason, year): 
    print(reason, str(year))

    container = "You have chosen reason as {0} & year {1}".format(reason, year)

    data = df.copy()
    data = data[data['Affected by'] == reason]
    data = data[data['Year'] == year]

    fig = px.bar(
        data,
        x= 'State',
        y= 'Pct of Colonies Impacted',
        color= 'Pct of Colonies Impacted',
        labels={'State':'States', 
                'Pct of Colonies Impacted':'Percent of Bee colonies impacted'},
        template="plotly_dark"
    )

    return container, fig


