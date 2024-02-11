
import logging
from nbconvert.exporters.markdown import MarkdownExporter


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
    mk = MarkdownExporter()
    mk.exclude_output = True
    mk.exclude_markdown = True
    return mk.from_filename(filename=filename)[0]

def create_fh_logger(file):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
    file_handler = logging.FileHandler(file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
