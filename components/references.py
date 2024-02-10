from dash import html
import dash_bootstrap_components as dbc
from pybtex.plugin import find_plugin
from pybtex.database import parse_file

APA = find_plugin("pybtex.style.formatting", "apa7")()
HTML = find_plugin("pybtex.backends", "html")()

name = "References"
bibliography = parse_file("assets/project.bib", "bibtex")
formatted_bib = APA.format_bibliography(bibliography)


layout = dbc.Container(
    children=[
        html.Div([html.Hr(), html.H1("References"), html.Br()]),
        html.Div(
            [
                html.Iframe(
                    srcDoc="<head><style> body {color: white;}</style>"
                    + f"{entry.text.render(HTML)}</head>",
                    id=entry.key,
                    className="bs-body",
                    style={"width": "100%", "height": "50px"},
                )
                for entry in formatted_bib
            ]
        ),  # the ID for the iframes are the citaiton key in zotero
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.P(""),
    ],
    id="references",  # the id is required to create anchor links
    style={"display": "flex", "flex-direction": "column"},
)
