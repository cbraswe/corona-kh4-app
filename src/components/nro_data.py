from dash import callback, html, Input, Output, State
import dash_bootstrap_components as dbc
from utils import file_to_md, update_code_button

name = "Analyzing NRO data"

layout = dbc.Container(
    children=[
        html.Hr(),
        html.H1("NRO Extraction, Analysis & Modeling"),
        html.Br(),
        html.P(
            "Overall, NRO's FOIA page is well-maintained and sets a standard for providing accessible public access to government records. The archivists provide a title for each document, context on the document type (i.e., MEMO, TWX), number of pages, and dates. Despite this fidelity, it seems impractical to locate every record required for the project solely based on title. Similarly, it is impractical to locate documents by dates or pages using the site, since the sort features do not work for these fields. Therefore, the data will be retrieved, processed, and modeled to identify relevant documents. These documents will be manually reviewed for information that may be useful in future analysis. A secondary goal is for the documents to be more searchable in bulk (i.e., key term search across a large file corpus)."
        ),
        html.Br(),
        html.H3("Step 1: Retrieve the Data"),
        html.Br(),
        html.P(
            children=[
                "To retrieve the data, the table containing a list of documents must be obtained from ",
                html.A(
                    "the NRO CAL Library Listing.",
                    href="https://www.nro.gov/foia-home/foia-declassified-major-nro-programs-and-projects/CAL-Library-Listing/",
                ),
                " Following the request for the page's content, it is required to parse the return and identify all links to a document. Once all links are identified, a request must be submitted for each document. Lastly, the documents must be stored and saved locally to prevent constant re-downloading of data. The documents are slightly renamed during this process, namely the name starts with an ISO 8601 formatted date. This will allow Windows file systems to chronologically sort when sorting by name. The below code uses asyncio, which reduced runtime from ~17mins to ~40secs compared to requests.",
            ]
        ),
        dbc.Button("", id="data-retrieval-collapse-button", n_clicks=0),
        dbc.Collapse(
            file_to_md("notebooks/nro/1_fetch_nro.py"),
            id="data-retrieval-collapse-code",
            className="notebook-embed",
        ),
        html.Br(),
        html.Br(),
        html.H3("Step 2: Convert the PDFs to Images"),
        html.Br(),
        html.P(
            "The primary OCR technologies available in Python are keras-ocr, pytesseract, tesserocr, and several other Tesseract wrappers. However, most of these libraries require the input to be an image instead of a PDF, although some can process in-memory images. For 2,300 pdfs, it is ideal to convert each PDF to a set of images (i.e., a PDF with 500 pages becomes 500 images) and statically save them. There are multiple options for this: GhostScript and pdf2images are both options I have used in the past; however, pdf2images has a threading option, manages the creation of the output folder, and handles numbering of page numbers to images. Therefore, it was chosen instead. The DPI may also be adjusted; however, a quick search showed PDF scans are typically around 2-300 DPI, and Tesseract works best with 300+ DPI. If the PDF is not a scan, then it is probable the text may be extracted directly without the use of OCR."
        ),
        dbc.Button("", id="data-pdf2image-collapse-button", n_clicks=0),
        dbc.Collapse(
            file_to_md("notebooks/nro/2_convert_nro_pdfs_to_imgs.ipynb"),
            id="data-pdf2image-collapse-code",
            className="notebook-embed",
        ),
        html.Br(),
        html.Br(),
        html.H3("Step 3: Apply OCR"),
        html.Br(),
        html.P(
            "For this step, Pytesseract was used, which required installing Tesseract-OCR. There are minimal parameters available to an end-user to affect output; however, it is advisable to set the output parameter to a dict or other enriched format. Adjusting the output will transition to providing a dictionary with coordinates of the text, the text detected, and a confidence level for the text. For this project, the confidence level will likely provide exceptionally meaningful in determining text to discard."
        ),
        dbc.Button("", id="data-imgs2json-collapse-button", n_clicks=0),
        dbc.Collapse(
            file_to_md("notebooks/nro/3_pytesseract.ipynb"),
            id="data-imgs2json-collapse-code",
            className="notebook-embed",
        ),
        html.Br(),
        html.Br(),
        html.H3("Step 4: Analyze the OCR"),
        html.Br(),
        html.P(
            "This notebook is focused on analyzing the OCR output to improve later code (i.e., conditions in the text that are repeteadly occurring that need addressed)."
        ),
        html.Div(children=[html.Img(
                                src="/assets/original_wordcloud.png",
                                height="200px",
                                style={"margin-right": "10px", "margin-left": "10px"},
                        ),
            html.Img(
                                src="/assets/cleaned_wordcloud.png",
                                height="200px",
                                style={"margin-right": "10px", "margin-left": "10px"},
                    ),
        ]),
        dbc.Button("", id="data-analyzeocr-collapse-button", n_clicks=0),
        dbc.Collapse(
            file_to_md("notebooks/nro/4_analyze_output_ocr_text.ipynb"),
            id="data-analyzeocr-collapse-code",
            className="notebook-embed",
        ),
        html.Br(),
        html.Br(),
        html.H3("Step 5: Clean and Tokenize the OCR"),
        html.Br(),
        html.P(
            "For this step, the rules detected in Step 4 were used to dismiss text. The most peculiar text condition within these documents are repeating characters (i.e., ee) forming a word. After removal of these text conditions, it applies a snowball stemmer and saves the output. "
        ),
        dbc.Button("", id="data-tokenize-collapse-button", n_clicks=0),
        dbc.Collapse(
            file_to_md("notebooks/nro/5_clean_tokenize_ocr.ipynb"),
            id="data-tokenize-collapse-code",
            className="notebook-embed",
        ),
        html.Br(),
        html.Br(),
        html.H3("Step 6: Create Topic Models"),
        html.Br(),
        html.P(
            "This uses Python's Gensim to create a Topic Model. This shows only one parameter variant; however, iterations were run with increased extreme filtering (i.e., tokens that are encountered in many variations of the word) as well as the number of topics. It did cluster similar topics together, and it did provide a starting point for further research (i.e., which documents to read). However, there are many cons: (1) it is still too many documents to manually review, (2) the topics are not perfect, and (3) it feels like a starting point."
        ),
        dbc.Button("", id="data-topic-collapse-button", n_clicks=0),
        dbc.Collapse(
            file_to_md("notebooks/nro/6_create_topic_model.ipynb"),
            id="data-topic-collapse-code",
            className="notebook-embed",
        ),
        html.Br(),
        html.Br(),
        html.H3("Step 7: Examine the OCR Itself"),
        html.Br(),
        html.P(
            "Given the poor quality of the OCR data, let's review the OCR with respect to the confidence scores for the word translations. This step also removes the `hopeless` documents from further OCR. This is primarily to assist with computation time on code consisting of a large number of `for` loops without parallelization."
        ),
        dbc.Button("", id="data-ocr_check-collapse-button", n_clicks=0),
        dbc.Collapse(
            file_to_md("notebooks/nro/7_how_bad_is_the_ocr.ipynb"),
            id="data-ocr_check-collapse-code",
            className="notebook-embed",
        ),
        html.Br(),
        html.Br(),
        html.H3("Step 8: Rotate Base Images Using EAST, Re-OCR"),
        html.Br(),
        html.P(
            "This step is following Tesseract's instructions to clean the data where possible prior to preprocessing. Originally, it was determined that text deskewing or a similar process would be well suited by CRAFT, which is a text detection algorithm. However, CRAFT stores the model weights on a Google drive, which frequently "
            "exceeds the 24 hour quota by Google. Therefore, the weights were not obtainable. In the absence of weights for CRAFT, EAST was chosen as a less then adequate substitution based on https://github.com/argman/EAST/issues/368. Given the needed rotations observed in the raw data are limited to a clockwise or counterclockwise 90 degree rotation, the image is tested for readability using EAST after each rotation."
            "If more text is detected at a rotation than the original, it is rotated and saved."
        ),
        dbc.Button("", id="data-rotate-collapse-button", n_clicks=0),
        dbc.Collapse(
            file_to_md("notebooks/nro/8_rotate_and_reocr.ipynb"),
            id="data-rotate-collapse-code",
            className="notebook-embed",
        ),
        html.Br(),
        html.H3("Step 9: Create the BERT Compatible OCR"),
        html.Br(),
        html.P(
            "This step is creating text for BERT in Step 10. The ultimate goal is to identify poorly translated text, accept small substitions (i.e., vhere -> where), and replace undetermined text with `[MASK]`. To allow small substitions, Levenshtein's distance is calculated between the original word alongside spell check suggestions. The output from the spell checked data is decent; however, other alternatives are available that likely perform better."
        ),
        dbc.Button("", id="data-create-bert-collapse-button", n_clicks=0),
        dbc.Collapse(
            file_to_md("notebooks/nro/9_create_bert_ocr.ipynb"),
            id="data-create-bert-collapse-code",
            className="notebook-embed",
        ),
        html.Br(),
        html.H3("Step 10: Apply BERT Masked to Code"),
        html.Br(),
        html.P(
            "Bidirectional Encoder Representations from Transformers (BERT) was created by Google, and it is available using HuggingFace's transformers library. There are several BERT weight files; however, it can be fine-tuned further. Unfortunately, this dataset is not in an adequate shape for fine-tuning, but after reviewing the documents, it may be possible to have `gold standard` translations that would be able to fine-tune BERT."
        ),
        dbc.Button("", id="data-bert-collapse-button", n_clicks=0),
        dbc.Collapse(
            file_to_md("notebooks/nro/10_bert_fill_in_ocr.ipynb"),
            id="data-bert-collapse-code",
            className="notebook-embed",
        ),
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
    ],
)
def toggle_pdf_retrieval_collapse0(n_clicks, is_open):
    return update_code_button(n_clicks, is_open)


@callback(
    [
        Output("data-pdf2image-collapse-code", "is_open"),
        Output("data-pdf2image-collapse-button", "children"),
    ],  # text displayed on button
    [Input("data-pdf2image-collapse-button", "n_clicks")],
    [State("data-pdf2image-collapse-code", "is_open")],
)
def toggle_pdf_retrieval_collapse1(n_clicks, is_open):
    return update_code_button(n_clicks, is_open)


@callback(
    [
        Output("data-clean_imgs-collapse-code", "is_open"),
        Output("data-clean_imgs-collapse-button", "children"),
    ],  # text displayed on button
    [Input("data-clean_imgs-collapse-button", "n_clicks")],
    [State("data-clean_imgs-collapse-code", "is_open")],
)
def toggle_pdf_retrieval_collapse2(n_clicks, is_open):
    return update_code_button(n_clicks, is_open)

@callback(
    [
        Output("data-imgs2json-collapse-code", "is_open"),
        Output("data-imgs2json-collapse-button", "children"),
    ],  # text displayed on button
    [Input("data-imgs2json-collapse-button", "n_clicks")],
    [State("data-imgs2json-collapse-code", "is_open")],
)
def toggle_pdf_retrieval_collapse3(n_clicks, is_open):
    return update_code_button(n_clicks, is_open)

@callback(
    [
        Output("data-analyzeocr-collapse-code", "is_open"),
        Output("data-analyzeocr-collapse-button", "children"),
    ],  # text displayed on button
    [Input("data-analyzeocr-collapse-button", "n_clicks")],
    [State("data-analyzeocr-collapse-code", "is_open")],
)
def toggle_pdf_retrieval_collapse4(n_clicks, is_open):
    return update_code_button(n_clicks, is_open)

@callback(
    [
        Output("data-tokenize-collapse-code", "is_open"),
        Output("data-tokenize-collapse-button", "children"),
    ],  # text displayed on button
    [Input("data-tokenize-collapse-button", "n_clicks")],
    [State("data-tokenize-collapse-code", "is_open")],
)
def toggle_pdf_retrieval_collapse5(n_clicks, is_open):
    return update_code_button(n_clicks, is_open)

@callback(
    [
        Output("data-topic-collapse-code", "is_open"),
        Output("data-topic-collapse-button", "children"),
    ],  # text displayed on button
    [Input("data-topic-collapse-button", "n_clicks")],
    [State("data-topic-collapse-code", "is_open")],
)
def toggle_pdf_retrieval_collapse6(n_clicks, is_open):
    return update_code_button(n_clicks, is_open)


@callback(
    [
        Output("data-bert-collapse-code", "is_open"),
        Output("data-bert-collapse-button", "children"),
    ],  # text displayed on button
    [Input("data-bert-collapse-button", "n_clicks")],
    [State("data-bert-collapse-code", "is_open")],
)
def toggle_pdf_retrieval_collapse7(n_clicks, is_open):
    return update_code_button(n_clicks, is_open)

@callback(
    [
        Output("data-create-bert-collapse-code", "is_open"),
        Output("data-create-bert-collapse-button", "children"),
    ],  # text displayed on button
    [Input("data-create-bert-collapse-button", "n_clicks")],
    [State("data-create-bert-collapse-code", "is_open")],
)
def toggle_pdf_retrieval_collapse8(n_clicks, is_open):
    return update_code_button(n_clicks, is_open)

@callback(
    [
        Output("data-rotate-collapse-code", "is_open"),
        Output("data-rotate-collapse-button", "children"),
    ],  # text displayed on button
    [Input("data-rotate-collapse-button", "n_clicks")],
    [State("data-rotate-collapse-code", "is_open")],
)
def toggle_pdf_retrieval_collapse9(n_clicks, is_open):
    return update_code_button(n_clicks, is_open)

@callback(
    [
        Output("data-ocr_check-collapse-code", "is_open"),
        Output("data-ocr_check-collapse-button", "children"),
    ],  # text displayed on button
    [Input("data-ocr_check-collapse-button", "n_clicks")],
    [State("data-ocr_check-collapse-code", "is_open")],
)
def toggle_pdf_retrieval_collapse10(n_clicks, is_open):
    return update_code_button(n_clicks, is_open)