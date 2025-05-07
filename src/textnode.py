from enum import Enum, auto
from htmlnode import HTMLNode, LeafNode, ParentNode

class TextType(Enum):
    TEXT = auto()       # Plain text
    BOLD = auto()       # **bold**
    ITALIC = auto()     # _italic_
    CODE = auto()       # `code`
    LINK = auto()       # [text](url)
    IMAGE = auto()      # ![alt](url)

# create TextNode class to represent a text node
class TextNode:
    def __init__(self, text, text_type: TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, value):
       # if all properies are equal, return True
        return (self.text == value.text and
                self.text_type == value.text_type and
                self.url == value.url)

    def __repr__(self):
        return (
            f"TextNode(text='{self.text}', "
            f"text_type={self.text_type.name}, "
            f"url='{self.url}')"
        )

# convert the text node to html
def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Unknown text type: {text_node.text_type}")
    