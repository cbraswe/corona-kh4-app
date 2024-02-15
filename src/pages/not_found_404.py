import dash
from dash import html

dash.register_page(__name__)

layout = html.Div(
    html.H1(
        "PAGE NOT FOUND: To boldly go where no man has gone before does not work on this site!"
    )
)
