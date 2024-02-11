from dash import html
import dash_bootstrap_components as dbc

name = "Analyzing NRO data"
layout = dbc.Container(
    children=[
        html.Hr(),
        html.H1("NRO Data Retrieval"),
        html.Br(),
        html.P(""),
    ],
    id="nro-data",
    class_name="offset",
)
