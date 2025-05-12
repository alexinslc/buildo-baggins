from block import block_to_block_type
from blocktype import BlockType
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from splitnodes import split_nodes_delimiter

def split_markdown_into_blocks(markdown: str) -> list[str]:
    """Split markdown into blocks, removing empty blocks and stripping whitespace."""
    blocks = markdown.split("\n\n")
    return [block.strip() for block in blocks if block.strip()]

def text_to_children(text: str) -> list[HTMLNode]:
    """Convert text with inline markdown to a list of HTMLNodes."""
    # Start with a single text node
    nodes = [TextNode(text, TextType.TEXT)]
    
    # Split by bold
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    
    # Split by italic
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    
    # Split by code
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    
    # Convert all nodes to HTML
    return [text_node_to_html_node(node) for node in nodes]

def block_to_html_node(block: str) -> HTMLNode:
    """Convert a single markdown block to an HTMLNode."""
    block_type = block_to_block_type(block)
    
    if block_type == BlockType.PARAGRAPH:
        # Replace newlines with spaces in paragraphs
        text = " ".join(block.split("\n"))
        return ParentNode("p", text_to_children(text))
    
    elif block_type == BlockType.HEADING:
        heading_level = 0
        for char in block:
            if char == "#":
                heading_level += 1
            else:
                break
        text = block[heading_level:].strip()
        return ParentNode(f"h{heading_level}", text_to_children(text))
    
    elif block_type == BlockType.CODE:
        # Remove the backticks and create a code block
        # Ensure there's a trailing newline
        code = block[3:-3].strip() + "\n"
        return ParentNode("pre", [LeafNode("code", code)])
    
    elif block_type == BlockType.QUOTE:
        # Remove the > from each line
        lines = [line[1:].strip() for line in block.split("\n")]
        text = "\n".join(lines)
        return ParentNode("blockquote", text_to_children(text))
    
    elif block_type == BlockType.UNORDERED_LIST:
        # Remove the - from each line
        items = [line[1:].strip() for line in block.split("\n")]
        list_items = [ParentNode("li", text_to_children(item)) for item in items]
        return ParentNode("ul", list_items)
    
    elif block_type == BlockType.ORDERED_LIST:
        # Remove the number and . from each line
        items = [line[line.find(".")+1:].strip() for line in block.split("\n")]
        list_items = [ParentNode("li", text_to_children(item)) for item in items]
        return ParentNode("ol", list_items)
    
    else:
        raise ValueError(f"Unknown block type: {block_type}")

def markdown_to_html_node(markdown: str) -> HTMLNode:
    """
    Convert a markdown document to a single parent HTMLNode.
    Args:
        markdown: A string containing markdown text
    Returns:
        A ParentNode containing all the markdown blocks as HTML
    """
    blocks = split_markdown_into_blocks(markdown)
    html_nodes = [block_to_html_node(block) for block in blocks]
    return ParentNode("div", html_nodes) 