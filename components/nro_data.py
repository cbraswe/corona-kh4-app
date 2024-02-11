from dash import callback, html, Input, Output, State
from dash.dcc import Markdown
import dash_bootstrap_components as dbc
from utils import reverse_code_text
name = "Analyzing NRO data"

mkdown_retrieving_pdfs = Markdown(
    '''```python
    import bs4
    from datetime import datetime
    from pathlib import Path 
    import requests
    output_folder = Path.cwd() / 'nro_declassified' / 'pdfs'
    base_url = 'https://www.nro.gov'
    # first need a listing of all available PDFs to download
    r = requests.get(f'{base_url}/foia-home/foia-declassified-major-nro-programs-and-projects/CAL-Library-Listing/')
    # then we want to find all data tagged with a table row indicator (our listing is a table)
    soup = bs4.BeautifulSoup(r.text,'lxml')
    rows = soup.find_all('tr') # find the table rows
    # then we want to iterate over each table row to get the links to the pdf, a name, and an id
    # and save the PDF
    # if the first portion of the PDf name is an iso format date, then windows sorting will be in chronological order (helpful!!)
    for row in rows:
        cells = row.find_all('td') 
        if len(cells) == 7: # there are other tables on the page but ours is 7 cells wide
            id = cells[0].text
            link = cells[1].find('a')
            if link is not None:
                link = link.get('href') 
                ext = link.split('.')[-1]
            name = cells[2].text
            for char in '<>:"/\|?*,.-': # not allowed in a windows file name
                name = name.replace(char, '') 
            name = name[:60] # low value bcuz there is also a windows length concern
            date = cells[3].text
            date = date.replace('(Estimated)', '') # text randomly included with date
            date = date.strip()
            try:
                date = datetime.strptime(date, '%m/%d/%Y').date().isoformat()
            except:
                date = datetime.utcnow().date().isoformat() # junk 
            if link is not None:
                file_name = f'{date}{name}_{id}.{ext}'
                # sends the request for the PDF 
                r = requests.get(f'{base_url}{link}')
                if r.ok:
                    # saves the PDF in our output folder
                    with open (output_folder / file_name, 'wb') as f:
                        f.write(r.content)
                else:
                    print(id)
    pdfs = list(output_folder.glob("*pdf")) # we can retrieve the PDFs afterwards
    # lastly we can check if we are missing any files
    # since the naming structure was {date}_name[:60]_{primarykey}.pdf
    # as of 2/11/24, there should be 6 missing PDFs. they do not have links
    have = [int(str(file).replace('.pdf', '').split('_')[-1]) for file in pdfs]
    want = range(1, 2359, 1)
    missing = [str(i) for i in want if i not in have]
    print(f'The following IDs do not have associated PDFs downloaded in this file system: {(",").join(missing)}')
    '''
)

layout = dbc.Container(
    children=[
        html.Hr(),
        html.H1("NRO Extraction, Analysis & Modeling"),
        html.Br(),
        html.H2('NRO Data Retrieval'),
        html.Br(),
        html.P('The first step is to obtain the data... (MORE TEXT HERE)'),
        dbc.Button('', id='data-retrieval-collapse-button', n_clicks=0),
        dbc.Collapse(mkdown_retrieving_pdfs, id='data-retrieval-collapse-code'),
        html.Br(),
        html.P(""),
    ],
    id="nro-data",
    class_name="offset",
)

@callback(
    [Output("data-retrieval-collapse-code", "is_open"),
    Output('data-retrieval-collapse-button', 'children')],
    [Input("data-retrieval-collapse-button", "n_clicks")],
    [State("data-retrieval-collapse-code", "is_open"), State('data-retrieval-collapse-button', 'children')],
)
def toggle_pdf_retrieval_collapse(n_clicks, is_open, button_text):
    if n_clicks:
        return not is_open, reverse_code_text(button_text)
    return is_open, reverse_code_text(button_text)