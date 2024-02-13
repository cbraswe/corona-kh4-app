
from dash.dcc import Markdown
import logging
from nbconvert.exporters.markdown import MarkdownExporter
from nbconvert.preprocessors import RegexRemovePreprocessor

def reverse_code_text(text):
    """This reverses the text of buttons intended to show/hide notebooks. If show notebook is the text, then it returns hide notebook.

    :param text: The current text associated with the button
    :type text: str
    :return: The new text associated with the button
    :rtype: str
    """
    if text == "" or text == "Hide Notebook":
        return "Show Notebook"
    else:
        return "Hide Notebook"

def notebook_to_md(filename):
    """This uses nbconvert, which requires Jupyter (tough dependency), to convert an `ipynb` file to a `markdown` file. This can be used in sections to include embed code directly.

    :param filename: The filename of the notebook to convert
    :type filename: str
    :return: Markdown that can be directly provided to dash.dcc.Markdown
    :rtype: str
    """
    if filename[-2:] == 'py':
        with open(filename, 'r') as f:
            data = f.read()
        return Markdown(f"```python\n{data}```\n")
    else:
        mk = MarkdownExporter()
        mk.exclude_output = True # remove output 
        mk.exclude_markdown = True # remove notebook content -> this is intended to be provided in paragraphs before the code
        regx = RegexRemovePreprocessor()
        regx.patterns = ["[\S]*\Z"] # HIDE EMPTY CELLS
        mk.register_preprocessor(regx, enabled=True) #THE DEFAULT IS FALSE.
        return Markdown(mk.from_filename(filename=filename)[0])

def create_fh_logger(file):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
    file_handler = logging.FileHandler(file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

def update_code_button(n_clicks, is_open, button_text):
    if n_clicks:
        return not is_open, reverse_code_text(button_text)
    return is_open, reverse_code_text(button_text)
