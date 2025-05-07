import re

def extract_markdown_images(text):
    """
    Extracts markdown image syntax from the given text.
    Returns a list of tuples containing alt text and URLs.
    """
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)

def extract_markdown_links(text):
    """
    Extracts markdown link syntax from the given text.
    Returns a list of tuples containing anchor text and URLs.
    """
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)