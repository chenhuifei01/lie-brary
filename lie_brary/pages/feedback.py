'''
This page is to collect feedback from the user.
The feedback will be used to improve the model.
#Reza R Pratama
'''
from dash import dcc, html, register_page, get_asset_url, callback, Input, Output
import pandas as pd
import lie_brary.scripts.dashboard.helper as helper

register_page(__name__)

filename = 'lie_brary/data/cleaned_data/feedback.csv'

# html location
layout = html.Div([
    html.H1('Feedback Form'),

    html.P('Please enter your feedback for the model.',
           'The feedback will be used to improve the model.'),
    html.Br(),
    html.P('Input the post ID (id_str):'),
    dcc.Input(id='id_str', placeholder='id_str', type='text', value=''),
    html.Br(),
    html.Br(),
    html.P('Input the sentiment:'),
    dcc.Dropdown(id='sentiment',
                options=helper.sentiment_options,
                multi=False,
                value=list(helper.SENTIMENT),
                style={'width': '30%'}
                ),
    html.Br(),
    html.P('Input the misinformation label:'),
    dcc.Dropdown(id='misinfo',
                options=helper.sentiment_options,
                multi=False,
                value=list(helper.FACT),
                style={'width': '30%'}
                ),
    html.Br(),
    html.Button('Submit', id='submit-button', n_clicks=0),
    html.Br(),
    html.Div(id='output')
])

@callback(
    Output('output', 'children'),
    Output('submit-button', 'n_clicks'),
    Input('submit-button', 'n_clicks'),
    Input('id_str', 'value'),
    Input('sentiment', 'value'),
    Input('misinfo', 'value')
)
def update_output(n_clicks, id_str, sentiment, misinfo):
    if id_str == '':
        return 'Please enter some values in id_str and click submit.', 0
    if n_clicks > 0:
        # create a dataframe with the input values
        df = pd.DataFrame({'id_str': [id_str],
                           'sentiment': [sentiment],
                           'misinfo': [misinfo]})
        # append the dataframe to the existing CSV file
        df.to_csv(filename, mode='a', header=False, index=False)
        return f'Thank you, for the feedback for {id_str}.', 0
    else:
        return 'Please enter some values and click submit.', 0