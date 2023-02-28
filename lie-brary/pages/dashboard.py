'''
This file contains the dashboard page.
- R
'''

import dash
from dash import html, dcc, callback, Input, Output
#import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from scripts.dashboard.helper import filter_data, SENTIMENT, FACT, SOURCE, KEYWORD
import scripts.dashboard.visualization as viz

dash.register_page(__name__,  path='/')

# Import Data
data = pd.read_csv('data/cleaned_data/cleaned_data.csv')
data['count'] = 1

# Create Control List
sentiment_options = [{'label': label, 'value': label} for label in SENTIMENT]
fact_options = [{'label': label, 'value': label} for label in FACT]
source_options = [{'label': label, 'value': label} for label in SOURCE]
keyword_options = [{'label': label, 'value': label} for label in KEYWORD]


# Dropdowns Menu
dropdown_sentiment = dbc.Card([

    html.Div([
    # sentiment dropdown label
    html.P('Sentiment'),
    dcc.Dropdown(id='sentiment_dropdown',
                options=sentiment_options,
                multi=True,
                value=list(SENTIMENT)
                ),

    # fact dropdown label
    html.P('Fact'),
    dcc.Dropdown(id='fact_dropdown',
                options=fact_options,
                multi=True,
                value=list(FACT)
                ),

    # source dropdown label
    html.P('Source'),
    dcc.Dropdown(id='source_dropdown',
                options=source_options,
                multi=True,
                value=list(SOURCE)
                ),

    # source dropdown label
    html.P('Keyword'),
    dcc.Dropdown(id='keyword_dropdown',
                options=keyword_options,
                multi=True,
                value=list(KEYWORD)
                )
])

], body=True, color='light')



# LAYOUT PAGE
layout = html.Div([
    # Dropdowns Menu
    dbc.Row([
        dbc.Col(dropdown_sentiment, md=4, style={'margin-top':'20px'}),
        dbc.Col(dcc.Graph(id='line_numpost'),md=8),

    ]),

    # Barplot
    dbc.Row([
        dbc.Col(dcc.Graph(id='bar_fact'),md=6),
        dbc.Col(dcc.Graph(id='bar_sentiment'),md=6),
    ]),



]) # End of Layout


# CALLBACKS
@callback(
    Output('bar_fact', 'figure'),
    Output('bar_sentiment', 'figure'),
    Output('line_numpost', 'figure'),
    [Input('sentiment_dropdown', 'value'),
     Input('fact_dropdown', 'value'),
     Input('source_dropdown', 'value'),
     Input('keyword_dropdown', 'value')],
)
def filtering_data(sentiment, fact, source, keyword):
    '''
    Filter data based on user input
    Input:
        sentiment: list of sentiment
        fact: list of fact
        source: list of source
        keyword: list of keyword
    Output:
        bar_fact: barplot of fact
        bar_sentiment: barplot of sentiment
    '''
    dff = filter_data(data, sentiment, fact, source, keyword)
    aggregate = dff.groupby(['sentiment','fact']).sum().reset_index()

    bar_fact = viz.barplot_fact(aggregate)
    bar_sentiment = viz.barplot_sentiment(aggregate)
    line_numpost = viz.line_numpost(dff)

    return bar_fact, bar_sentiment, line_numpost