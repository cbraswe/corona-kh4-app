import dash
from dash import html

dash.register_page(__name__, name="NRO Document Search", order=1)

layout = html.Div(
    [html.P("This is gonna be THE DOC SEARCH TOOL. ."), html.Br()],
)
