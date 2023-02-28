'''
This is the main script for the dashboard. It will be used to create the layout of the dashboard.
This will call pages in the container view. -R
'''

import dash
from dash import Dash, html, dcc, dash_table, Input, Output, State, ClientsideFunction
#import plotly.express as px
#import pandas as pd
import dash_bootstrap_components as dbc

# Initialize the app
app = Dash(__name__,
           external_stylesheets=[dbc.themes.BOOTSTRAP],
           use_pages=True)
app.title = 'Lie-brary'

# LAYOUT PAGE
app.layout = html.Div([
	dbc.Container([
        # Header
	    html.H1(children='Lie-brary',
	        style={'textAlign': 'left', 'color': 'blue', 'font-size': '40px', 'font-weight': 'bold'}),

        html.Div(children='"Bringing clarity to the chaos of online information"',
            style={'textAlign': 'left', 'color': 'black', 'font-size': '20px', 'font-style': 'italic'}),

	    html.Hr(),

        # Navigation bar
	    html.Div(
            [
                html.Div(
                    dcc.Link(
                        f"{page['name']}", href=page["relative_path"]
                    )
                )
                for page in dash.page_registry.values()

        ]),
        html.Hr(),
    #Pages from the pages will be rendered here
	dash.page_container,

    ]) # End of container
]) # End of layout

if __name__ == '__main__':
	app.run_server(debug=True)
