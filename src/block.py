from blocktype import BlockType

def block_to_block_type(block: str) -> BlockType:
    """
    Determine the type of a markdown block.
    Args:
        block: A string containing a single markdown block
    Returns:
        BlockType enum value representing the type of block
    """
    lines = block.split("\n")
    
    # Check for code block
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    # Check for heading
    if block.startswith("#"):
        heading_level = 0
        for char in block:
            if char == "#":
                heading_level += 1
            else:
                break
        if 1 <= heading_level <= 6 and block[heading_level:].startswith(" "):
            return BlockType.HEADING
    
    # Check for quote block
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    
    # Check for unordered list
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    
    # Check for ordered list
    if all(line.startswith(f"{i+1}. ") for i, line in enumerate(lines)):
        return BlockType.ORDERED_LIST
    
    # Default to paragraph
    return BlockType.PARAGRAPH 