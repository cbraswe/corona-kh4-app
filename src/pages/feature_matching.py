import dash
from dash import html

dash.register_page(__name__, name="Feature Matching")

layout = html.Div(
    [
        html.P(
            "This is gonna be the feature matching page if it works out to have a live demo item."
        ),
        html.Br(),
    ]
)
