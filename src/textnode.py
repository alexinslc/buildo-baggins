from enum import Enum, auto

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
