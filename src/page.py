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

def generate_page(from_path: str, template_path: str, dest_path: str, basepath: str = "/") -> None:
    """
    Generate an HTML page from markdown content using a template.
    Args:
        from_path: Path to the markdown file
        template_path: Path to the HTML template
        dest_path: Path where the generated HTML should be written
        basepath: Base path for URLs in the generated HTML
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
    
    # Replace absolute paths with basepath
    html = html.replace('href="/', f'href="{basepath}')
    html = html.replace('src="/', f'src="{basepath}')
    
    # Create destination directory if it doesn't exist
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    # Write the generated HTML to the destination file
    with open(dest_path, "w") as f:
        f.write(html)

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str, basepath: str = "/") -> None:
    """
    Recursively generate HTML pages from markdown files in a directory.
    Args:
        dir_path_content: Path to the content directory containing markdown files
        template_path: Path to the HTML template
        dest_dir_path: Path where the generated HTML files should be written
        basepath: Base path for URLs in the generated HTML
    """
    # Create the destination directory if it doesn't exist
    os.makedirs(dest_dir_path, exist_ok=True)
    
    # Walk through the content directory
    for root, dirs, files in os.walk(dir_path_content):
        # Calculate the relative path from dir_path_content
        rel_path = os.path.relpath(root, dir_path_content)
        
        # Create corresponding directories in dest_dir_path
        for dir_name in dirs:
            src_dir = os.path.join(root, dir_name)
            dst_dir = os.path.join(dest_dir_path, rel_path, dir_name)
            os.makedirs(dst_dir, exist_ok=True)
            print(f"Created directory: {dst_dir}")
        
        # Process markdown files
        for file_name in files:
            if file_name.endswith(".md"):
                # Get the full paths
                src_file = os.path.join(root, file_name)
                # Replace .md with .html for the destination file
                dst_file = os.path.join(dest_dir_path, rel_path, file_name.replace(".md", ".html"))
                
                # Generate the HTML page
                generate_page(src_file, template_path, dst_file, basepath) 