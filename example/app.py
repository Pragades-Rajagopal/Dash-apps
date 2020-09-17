import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import dash

app = dash.Dash(__name__)

data = pd.read_csv('emission-data.csv')
data = data.groupby(['Country', 'Continent'])[['Emission']].mean()
data.reset_index(inplace=True)

continents = data['Continent'].unique()

app.layout = html.Div([

    html.H1("Dashboard for Global Emission data", style={"text-align":"center"}),

    html.H4("Choose the continent"),
    dcc.Dropdown(id='select-continent',
                options=[{'label':x, 'value':x} for x in continents],
                value='Asia',
                multi=False,
                style={'width':'40%'}
                ),

    html.Div(id='my-container', children=[]),
    html.Br(),

    dcc.Graph(id='my-graph', figure={})

])

@app.callback(
    [Output(component_id='my-container', component_property='children'),
    Output(component_id='my-graph', component_property='figure')],
    [Input(component_id='select-continent', component_property='value')]
)

def graph(continent):
    print(str(continent))

    container = "Selected continent is {}".format(continent)

    new_df = data.copy()
    new_df = new_df[new_df['Continent'] == continent]

    fig = px.bar(
            new_df,
            x='Country',
            y='Emission',
            color='Emission',
            template="plotly_dark"
        )

    return container, fig


if __name__ == '__main__':
    app.run_server(debug=True)