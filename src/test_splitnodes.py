import unittest
from splitnodes import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_with_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])

    def test_split_with_bold(self):
        node = TextNode("This is **bold text** in a sentence", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(" in a sentence", TextType.TEXT),
        ])

    def test_split_with_italic(self):
        node = TextNode("This is _italic text_ in a sentence", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC),
            TextNode(" in a sentence", TextType.TEXT),
        ])

    def test_unmatched_delimiter(self):
        node = TextNode("This is **bold text in a sentence", TextType.TEXT)
        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(str(context.exception), "Unmatched delimiter '**' in text: This is **bold text in a sentence")

    def test_no_delimiters(self):
        node = TextNode("This is plain text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [node])

    def test_mixed_nodes(self):
        nodes = [
            TextNode("This is **bold text**", TextType.TEXT),
            TextNode(" and this is plain text", TextType.TEXT),
            TextNode("This is a link", TextType.LINK, "http://example.com"),
        ]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode("", TextType.TEXT),
            TextNode(" and this is plain text", TextType.TEXT),
            TextNode("This is a link", TextType.LINK, "http://example.com"),
        ])

if __name__ == "__main__":
    unittest.main()