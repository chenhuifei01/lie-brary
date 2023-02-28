from dash import html, register_page, get_asset_url

register_page(__name__)

# html location
layout = html.Div([
    # get from iFrame
    html.Iframe(id='analysis_iframe',
                src=get_asset_url('analysis.html'),
                style={'width': '100%', 'height': '100vh'}),
])