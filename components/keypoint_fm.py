from dash import html
import dash_bootstrap_components as dbc

name = "Keypoint Detection & Feature Matching"
layout = dbc.Container(
    children=[
        html.Hr(),
        html.H1("Keypoint Detection"),
        html.Br(),
        html.P(""),
    ],
    id="keypoint-fm",
    class_name="offset",
)
