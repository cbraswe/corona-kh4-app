import dash
from dash import html

dash.register_page(__name__)

layout = html.Div(html.H1("I'm watching. 404"))
