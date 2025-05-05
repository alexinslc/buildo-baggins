from textnode import TextNode, TextType

def main(): 
    # Create a LINK TextNode
    text_node1 = TextNode("This is some anchor text", TextType.LINK, "https://example.com")
    print(text_node1)

main()

