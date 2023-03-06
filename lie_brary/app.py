'''
This is the main script for the dashboard. It will be used to create the layout of the dashboard.
This will call pages in the container view.
# Author: Reza R Pratama
'''
from dash import Dash, html, page_container
import dash_bootstrap_components as dbc
import lie_brary.scripts.dashboard.helper as helper

# Initialize the app
app = Dash(__name__,
           external_stylesheets=[dbc.themes.BOOTSTRAP],
           use_pages=True)
app.title = 'Lie-brary'


# Navigation bar
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Dashboard", href="/", active="exact", style={'font-weight': 'bold'})),
        dbc.NavItem(dbc.NavLink("Analysis", href="/analysis", active="exact", style={'font-weight': 'bold'})),
        dbc.NavItem(dbc.NavLink("Data", href="/datatable", style={'font-weight': 'bold'})),
        dbc.NavItem(dbc.NavLink("Feedback", href="/feedback", style={'font-weight': 'bold'})),
        dbc.NavItem(dbc.NavLink("Mythbusting", href="/mythbusting", style={'font-weight': 'bold'})),
        dbc.NavItem(dbc.NavLink("Fact-Finding", href="/factfinding", style={'font-weight': 'bold'})),
    ],
    brand_href="/",
    sticky="top",
    color="#0C2D48",
    dark=True,
)

# LAYOUT PAGE
app.layout = html.Div([
	dbc.Container([
        # Header
	    html.H1(children='Lie-brary',
	        style={'textAlign': 'left', 'color': '#0C2D48', 'font-size': '40px', 'font-weight': 'bold'}),

        html.Div(children='"Bringing clarity to the chaos of online information"',
            style={'textAlign': 'left', 'color': 'black', 'font-size': '20px', 'font-style': 'italic'}),

        # Navigation bar
        html.Div(navbar),
        html.Br(),
        html.P(helper.get_last_update(), style={'textAlign': 'right', 'color': 'black', 'font-size': '12px'}),

        #Pages from the pages will be rendered here
        page_container,

    ]) # End of container
]) # End of layout