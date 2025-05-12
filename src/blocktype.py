from enum import Enum, auto

class BlockType(Enum):
    PARAGRAPH = auto()      # Regular paragraph text
    HEADING = auto()        # # Heading text
    CODE = auto()          # ```code block```
    QUOTE = auto()         # > Quote text
    UNORDERED_LIST = auto() # - List item
    ORDERED_LIST = auto()   # 1. List item 