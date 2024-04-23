from dash.dcc import Markdown
import logging
from nbconvert.exporters.markdown import MarkdownExporter
from nbconvert.preprocessors import RegexRemovePreprocessor
from pathlib import Path
from typing import Tuple, Union


def file_to_md(file: Union[Path, str]) -> Markdown:
    """Helper function to convert a .py or .ipynb file into Markdown, compatible with Dash. Empty cells, output, and markdown are removed from `.ipynb` files.

    Args:
        file (Union[Path, str]): The `.py` or `.ipynb` file

    Returns:
        Markdown: Markdown displaying the contents of the file
    """
    if str(file[-2:]) == "py":
        with open(file, "r") as f:
            data = f.read()
        return Markdown(f"```python\n{data}```\n")
    else:
        mk = MarkdownExporter()
        mk.exclude_output = False  # remove output
        mk.exclude_markdown = False  # remove notebook content -> this is intended to be provided in paragraphs before the code
        regx = RegexRemovePreprocessor()
        regx.patterns = ["[\S]*\Z"]  # HIDE EMPTY CELLS
        mk.register_preprocessor(regx, enabled=True)  # THE DEFAULT IS FALSE.
        return Markdown(mk.from_filename(filename=file)[0])


def create_fh_logger(file: Union[Path, str]) -> logging.Logger:
    """Creates a standardized file handling logger, primarily for use within the notebooks for long-running analytics. It saves the log to the specified file.

    Args:
        file (Union[Path, str]): The location to save logs

    Returns:
        logging.Logger: A configured logger ready for use
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    file_handler = logging.FileHandler(file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


def update_code_button(n_clicks: int, is_open: bool) -> Tuple[bool, str]:
    """This function reverses the button text and state of a collapsed Notebook. If it's closed with

    Args:
        n_clicks (int): Current value of n_clicks associated with a Button
        is_open (bool): Current value of is_open associated with a Collapse

    Returns:
        Tuple[bool, str]: A new value to provide is_open for a Collapse, a new value to provide to the Button text
    """
    is_open = not is_open if n_clicks else is_open
    text = "Hide Notebook" if is_open else "Show Notebook"
    return is_open, text
