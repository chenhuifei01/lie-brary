'''
Interactive mythbusting page powered by GPT-3.
- R
'''
from dash import dcc, html, register_page, get_asset_url, callback, Input, Output
import lie_brary.scripts.scrap.key as key
import openai
import dash_bootstrap_components as dbc

register_page(__name__)

layout = html.Div([
    html.H1('Mythbusting the topics with GPT-3'),
    html.P('Please enter the topic you want to mythbust.'),
    html.Br(),
    # input box
    dbc.Textarea(id = 'topic',
                 className="mb-3",
                 placeholder="Write the topic here...",
                 value=''),
    html.Button('Submit', id='submit-button1', n_clicks=0),
    html.Br(),
    html.Br(),
    # output box
    html.H4('Mythbusting result:'),
    html.Br(),
    html.Div(id='output1')
])

@callback(
    Output('output1', 'children'),
    Output('submit-button1', 'n_clicks'),
    Input('submit-button1', 'n_clicks'),
    Input('topic', 'value')
)
def update_output(n_clicks, topic):
    if topic == '' or n_clicks == 0:
        return 'Please enter some values in topic and click submit.', 0
    openai.api_key = key.OPENAI_KEY
    if n_clicks > 0:
        text = topic
        prompts = "Write text to counteract misinformation on Illinois' Pre-Trial Fairness Act in this topics: "
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                  messages=[{"role": "user", "content":prompts+text}])
        response = completion.choices[0].message.content
        return response, 0