import dash
from dash import html

dash.register_page(
    __name__, title="Corona KH-4 DSM", name="Corona DSM", path="/corona-dsm"
)

layout = html.Div(
    [
        html.P(
            "This is gonna be the example showing DSMs created from corona stereoscopic img vs airbreather collected lidar. Likely images but maybe a strange tiled server implementation with dash-leaflet is possible"
        ),
        html.Br(),
    ]
)
