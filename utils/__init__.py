from nbconvert.exporters.markdown import MarkdownExporter

def reverse_code_text(text):
    if text == '' or text == 'Hide Notebook':
        return 'Show Notebook'
    else:
        return 'Hide Notebook'
    
def notebook_to_md(filename):
    mk = MarkdownExporter()
    mk.exclude_output = True
    mk.exclude_markdown = True
    return mk.from_filename(filename=filename)[0]