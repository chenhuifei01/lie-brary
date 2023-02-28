import dash
from dash import html, dcc, callback, Input, Output, dash_table
#import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from scripts.dashboard.helper import filter_data, SENTIMENT, FACT, SOURCE, KEYWORD



dash.register_page(__name__)

data = pd.read_csv('data\cleaned_data\cleaned_data.csv')
df = data[['sentiment', 'fact', 'sources', 'text']]

layout = dbc.Container([
    html.H3('Table: Post Data'),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='page-size',
                options=[
                    {'label': '5', 'value': 5},
                    {'label': '10', 'value': 10},
                    {'label': '20', 'value': 20},
                ],
                value=10,
            )
        ], width=2),
    ]),
    dbc.Row([
        dbc.Col([
            dash_table.DataTable(
                id='table',
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict('records'),
                page_current=0,
                page_size=10,
                page_action='custom',
                style_cell={'textAlign': 'left'},
                style_data={'whiteSpace': 'normal',
                            'height': 'auto'},
                style_table={'overflowX': 'scroll'},
            )
        ]),
    ]),

])



@callback(
    [Output('table', 'data'),
     Output('table', 'page_current')],
    [Input('page-size', 'value'),
     Input('table', 'page_current'),
     Input('table', 'page_action')])
def update_table(page_size, page_current, page_action):
    if page_action == 'custom':
        return df.iloc[page_current*page_size:(page_current+ 1)*page_size].to_dict('records'), page_current
    return df.to_dict('records'), 0
