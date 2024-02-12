from dash import callback, html, Input, Output, State
import dash_bootstrap_components as dbc
from utils import reverse_code_text, notebook_to_md, update_code_button

name = "Analyzing NRO data"

layout = dbc.Container(
    children=[
        html.Hr(),
        html.H1("NRO Extraction, Analysis & Modeling"),
        html.Br(),
        html.P("Overall, NRO's FOIA page is well-maintained and sets a standard for providing accessible public access to government records. The archivists provide a title for each document, context on the document type (i.e., MEMO, TWX), number of pages, and dates. Despite this fidelity, it seems impractical to locate every record required for the project solely based on title. Similarly, it is impractical to locate documents by dates or pages using the site, since the sort features do not work for these fields. Therefore, the data will be retrieved, processed, and modeled to identify relevant documents."),
        html.Br(),
        html.H3("Step 1: Retrieve the Data"),
        html.Br(),
        html.P(children=[
            "To retrieve the data, the table containing a list of documents must be obtained from ",
            html.A("the NRO CAL Library Listing.", href='https://www.nro.gov/foia-home/foia-declassified-major-nro-programs-and-projects/CAL-Library-Listing/'),
            " Following the request for the page's content, it is required to parse the return and identify all links to a document. Once all links are identified, a request must be submitted for each document. Lastly, the documents must be stored and saved locally to prevent constant re-downloading of data."
        ]),
        dbc.Button("", id="data-retrieval-collapse-button", n_clicks=0),
        dbc.Collapse(
            notebook_to_md("notebooks/1_fetch_nro.ipynb"),
            id="data-retrieval-collapse-code",
            className='notebook-embed',
        ),
        html.Br(),
        html.Br(),
        html.H3("Step 2: Convert the PDFs to Images"),
        html.Br(),
        html.P('The primary OCR technologies available in Python are keras-ocr, pytesseract, tesserocr, and several other Tesseract libraries. However, most of these libraries require the input to be an image instead of a PDF, although some can process in-memory images. Therefore, it is ideal to convert each PDF to a set of images (i.e., a PDF with 500 pages becomes 500 images). There are multiple options for this: GhostScript and pdf2images are both options I have used in the past; however, pdf2images has a threading option, manages the creation of the output folder, and handles numbering of page numbers to images. Therefore, it was chosen instead. The DPI may also be adjusted; however, a quick search showed PDF scans are typically around 2-300 DPI, and Tesseract works best with 300+ DPI. If the PDF is not a scan, then it is probable the text may be extracted directly without the use of OCR.'),
        dbc.Button("", id="data-pdf2image-collapse-button", n_clicks=0),
        dbc.Collapse(
            notebook_to_md("notebooks/2_convert_nro_pdfs_to_imgs.ipynb"),
            id="data-pdf2image-collapse-code",
            className='notebook-embed',
        ),
        html.Br(),
        html.Br(),
        html.H3("Step 3: Use an OCR tool on the Images"),
        html.Br(),
        html.P('For this step, Pytesseract was used, which required installing Tesseract-OCR. There are minimal parameters available to an end-user to affect output; however, it is advisable to set the output parameter to a dict or other enriched format. Adjusting the output will transition to providing a dictionary with coordinates of the text, the text detected, and a confidence level for the text. For this project, the confidence level will likely provide exceptionally meaningful in determining text to discard. Step needs rewritten with some image processing techniques (a low pass filter to remove noise.)'),
        dbc.Button("", id="data-imgs2json-collapse-button", n_clicks=0),
        dbc.Collapse(
            notebook_to_md("notebooks/3_convert_imgs_to_json_text.ipynb"),
            id="data-imgs2json-collapse-code",
           className='notebook-embed',
        ),
        html.Br(),
        html.Br(),
    ],
    id="nro-data",
    class_name="offset",
)


#! TODO: Find a better mechanism to handle these shared code cases. I think matching will work
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
    return update_code_button(n_clicks, is_open, button_text)

@callback(
    [
        Output("data-pdf2image-collapse-code", "is_open"),
        Output("data-pdf2image-collapse-button", "children"),
    ],  # text displayed on button
    [Input("data-pdf2image-collapse-button", "n_clicks")],
    [
        State("data-pdf2image-collapse-code", "is_open"),
        State("data-pdf2image-collapse-button", "children"),
    ],
)
def toggle_pdf_retrieval_collapse(n_clicks, is_open, button_text):
    return update_code_button(n_clicks, is_open, button_text)

@callback(
    [
        Output("data-imgs2json-collapse-code", "is_open"),
        Output("data-imgs2json-collapse-button", "children"),
    ],  # text displayed on button
    [Input("data-imgs2json-collapse-button", "n_clicks")],
    [
        State("data-imgs2json-collapse-code", "is_open"),
        State("data-imgs2json-collapse-button", "children"),
    ],
)
def toggle_pdf_retrieval_collapse(n_clicks, is_open, button_text):
    return update_code_button(n_clicks, is_open, button_text)