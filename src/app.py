import dash
from dash import html
import dash_bootstrap_components as dbc

# since we are using pages, each page is stored in a .py file under /pages
# the page must be registered and has some parameters to pass: https://dash.plotly.com/urls#reference-for-dash.register_page
app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SUPERHERO])
app.title = "Corona"

app.layout = dbc.Container(
    children=[
        dbc.Row(
            dbc.Navbar(
                children=[
                    dbc.Col(
                        html.A(
                            html.Img(
                                src="/assets/wlogo_nobg.png",
                                height="50px",
                                style={"margin-left": "10px"},
                            ),
                            href="/",
                        )
                    ),
                    dbc.Col(
                        html.A(
                            html.Img(
                                src="/assets/github_white.png",
                                height="50px",
                                style={"margin-right": "10px", "margin-left": "10px"},
                            ),
                            href="https://github.com/cbraswe/corona-kh4-app/",
                        ),
                        style={
                            "flex": "0 1 auto",
                            "border-left": "2px solid white",
                            "margin-right": "2px",
                        },
                    ),
                ],
                style={
                    "position": "fixed",
                    "width": "100%",
                    "top": 0,
                    "z-index": "9999",
                },
            )
        ),
        dbc.Row(
            dash.page_container,
            style={"margin-top": "75px", "width": "100%", "maxWidth": "100%"},
        ),
    ],
    style={"maxWidth": "100%", "height": "auto"},
)

server = app.server
