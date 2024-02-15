from dash import html
import dash_bootstrap_components as dbc

name = "Corona DSMs"
layout = dbc.Container(
    children=[
        html.Hr(),
        html.H1("Corona Digital Surface Model (DSM) Creation"),
        html.Br(),
        html.P(
            "Since KH-4 collected data using a stereoscopic system, it is possible to create a DSM for each pair. This data can be compared to LiDAR derived DSM."
        ),
    ],
    id="corona-dsm",
    class_name="offset",
)
