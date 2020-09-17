import pandas as pd
import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

df = pd.read_csv("intro_bees.csv")
df = df.groupby(['State', 'ANSI', 'Affected by', 'Year', 'state_code'])[['Pct of Colonies Impacted']].mean()
df.reset_index(inplace=True)
# print(df[:5])

app.layout = html.Div([

    html.H1("Web Dashboard for bees", style={'text-align' : 'center'}),

    dcc.Dropdown(id='select_year',
                 options=[
                     {"label": "2015", "value": 2015},
                     {"label": "2016", "value": 2016},
                     {"label": "2017", "value": 2017},
                     {"label": "2018", "value": 2018}
                 ],
                 multi=False,
                 value = 2015,
                 style= {'width': '40%'}
                 ),

    dcc.Dropdown(id='select_reason',
                 options=[
                     {"label": "Disease", "value": "Disease"},
                     {"label": "Pesticides", "value": "Pesticides"},
                     {"label": "Varroa mites", "value": "Varroa_mites"},
                     {"label": "Others", "value": "Other"},
                     {"label": "Unknown", "value": "Unknown"},
                 ],
                 multi=False,
                 value = "Disease",
                 style= {'width': '40%'}
                 ),

    html.Div(id='output-container', children=[]),
    html.Br(),

    dcc.Graph(id='my-bee-map', figure={})

])

@app.callback(
    [Output(component_id='output-container', component_property='children'),Output(component_id='my-bee-map', component_property='figure')],
    [Input(component_id='select_year', component_property='value'),
    Input(component_id='select_reason', component_property='value')]
)

def graph_update(selection, reason):
    print(selection, type(selection), str(reason))

    container = "The year chosen is {0}, reason {1}".format(selection, reason)


    new_df = df.copy()
    new_df = new_df[new_df['Year'] == selection]
    new_df = new_df[new_df['Affected by'] == reason]

    fig = px.choropleth(
        data_frame= new_df,
        locationmode= 'USA-states',
        locations= 'state_code',
        scope= "usa",
        color= 'Pct of Colonies Impacted',
        hover_data= ['State', 'Pct of Colonies Impacted'],
        color_continuous_scale= px.colors.sequential.YlOrRd,
        labels= {'Pct of Colonies Impacted': 'Percent of Bee colonies'},
        template= 'plotly_dark'
    )

    return container, fig


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=5000, debug=True)

