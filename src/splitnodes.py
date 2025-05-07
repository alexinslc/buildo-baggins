from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            # Add non-text nodes as-is
            new_nodes.append(node)
            continue

        # Split the text node by the delimiter
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError(f"Unmatched delimiter '{delimiter}' in text: {node.text}")

        for i, part in enumerate(parts):
            if i % 2 == 0:
                # Even index: plain text - always include these nodes even if empty
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                # Odd index: text with the specified text_type - only include if non-empty
                if part.strip():  # Skip empty delimited sections
                    new_nodes.append(TextNode(part, text_type))

    return new_nodes