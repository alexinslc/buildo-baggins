from textnode import TextNode, TextType
from extractmarkdown import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            # Add non-text nodes as-is
            new_nodes.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)
        if not images:
            # No images, add the original node
            new_nodes.append(node)
            continue

        for alt_text, url in images:
            # Split the text before and after the image
            sections = text.split(f"![{alt_text}]({url})", 1)
            if sections[0].strip():
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            text = sections[1] if len(sections) > 1 else ""

        if text.strip():
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            # Add non-text nodes as-is
            new_nodes.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)
        if not links:
            # No links, add the original node
            new_nodes.append(node)
            continue

        for anchor_text, url in links:
            # Split the text before and after the link
            sections = text.split(f"[{anchor_text}]({url})", 1)
            if sections[0].strip():
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
            text = sections[1] if len(sections) > 1 else ""

        if text.strip():
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes