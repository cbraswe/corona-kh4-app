from dash import callback, html, Input, Output, State
from dash.dcc import Markdown
import dash_bootstrap_components as dbc
from utils import reverse_code_text, notebook_to_md

name = "Analyzing NRO data"

mkdown_retrieving_pdfs = Markdown(notebook_to_md("notebooks/1_fetch_nro.ipynb"))
notebook_margins = {"margin-left": "75px", "margin-top": "20px"}
layout = dbc.Container(
    children=[
        html.Hr(),
        html.H1("NRO Extraction, Analysis & Modeling"),
        html.Br(),
        html.H2("Step 1: Retrieve the Data"),
        html.Br(),
        html.P("Overall, NRO's FOIA page is well-maintained and sets a standard for providing accessible public access to government records. The archivists provide a title for each document, context on the document type (i.e., MEMO, TWX), number of pages, and dates. Despite this"),
        dbc.Button("", id="data-retrieval-collapse-button", n_clicks=0),
        dbc.Collapse(
            mkdown_retrieving_pdfs,
            id="data-retrieval-collapse-code",
            style=notebook_margins,
        ),
        html.Br(),
        html.P(""),
    ],
    id="nro-data",
    class_name="offset",
)


@callback(
    [
        Output("data-retrieval-collapse-code", "is_open"),
        Output("data-retrieval-collapse-button", "children"),
    ],  # text displayed on button
    [Input("data-retrieval-collapse-button", "n_clicks")],
    [
        State("data-retrieval-collapse-code", "is_open"),
        State("data-retrieval-collapse-button", "children"),
    ],
)
def toggle_pdf_retrieval_collapse(n_clicks, is_open, button_text):
    if n_clicks:
        return not is_open, reverse_code_text(button_text)
    return is_open, reverse_code_text(button_text)
