import dash
from dash import html
import dash_bootstrap_components as dbc

# since we are using pages, each page is stored in a .py file under /pages
# the page must be registered and has some parameters to pass: https://dash.plotly.com/urls#reference-for-dash.register_page
app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SUPERHERO])
app.title = "Corona"

app.layout = dbc.Container(
    children=[
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
                    dbc.Nav(
                        children=[
                            dbc.NavLink(
                                page["name"],
                                href=page["path"],
                                style={
                                    "border-left": "2px solid white",
                                    "margin-right": "2px",
                                },
                            )
                            for page in dash.page_registry.values()
                            if page["path"] != "/not-found-404" and page["path"] != "/"
                        ],
                        style={"justify-content": "end"},
                        className="ml-auto",  # css flexbox margin left: auto to right align content
                    ),
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
                    style={'flex': '0 1 auto', "border-left": "2px solid white", "margin-right": "2px",}
                ),
            ]
        ),
        dash.page_container,
    ],
    style={"maxWidth": "75%", "height": "auto"},
)

server = app.server
