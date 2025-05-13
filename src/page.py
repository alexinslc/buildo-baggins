import os
from markdown import markdown_to_html_node

def extract_title(markdown: str) -> str:
    """
    Extract the title (h1 header) from markdown text.
    Raises an exception if no h1 header is found.
    """
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No h1 header found in markdown")

def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    """
    Generate an HTML page from markdown content using a template.
    Args:
        from_path: Path to the markdown file
        template_path: Path to the HTML template
        dest_path: Path where the generated HTML should be written
    """
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Read the markdown file
    with open(from_path, "r") as f:
        markdown = f.read()
    
    # Read the template file
    with open(template_path, "r") as f:
        template = f.read()
    
    # Convert markdown to HTML
    html_node = markdown_to_html_node(markdown)
    content = html_node.to_html()
    
    # Extract the title
    title = extract_title(markdown)
    
    # Replace placeholders in template
    html = template.replace("{{ Title }}", title)
    html = html.replace("{{ Content }}", content)
    
    # Create destination directory if it doesn't exist
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    # Write the generated HTML to the destination file
    with open(dest_path, "w") as f:
        f.write(html) 