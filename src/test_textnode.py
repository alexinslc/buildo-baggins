import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_textnode_inequality_different_text(self):
            # Test inequality when text is different
            node1 = TextNode("Hello", TextType.TEXT, "http://example.com")
            node2 = TextNode("Hi", TextType.TEXT, "http://example.com")
            self.assertNotEqual(node1, node2)

    def test_textnode_inequality_different_text_type(self):
        # Test inequality when text_type is different
        node1 = TextNode("Hello", TextType.TEXT, "http://example.com")
        node2 = TextNode("Hello", TextType.BOLD, "http://example.com")

    def test_textnode_inequality_different_url(self):
        # Test inequality when url is different
        node1 = TextNode("Hello", TextType.TEXT, "http://example.com")
        node2 = TextNode("Hello", TextType.TEXT, "http://example.org")
        self.assertNotEqual(node1, node2)

    def test_textnode_equality_with_none_url(self):
        # Test equality when url is None
        node1 = TextNode("Hello", TextType.TEXT, None)
        node2 = TextNode("Hello", TextType.TEXT, None)
        self.assertEqual(node1, node2)

    def test_textnode_inequality_with_one_none_url(self):
        # Test inequality when one url is None
        node1 = TextNode("Hello", TextType.TEXT, None)
        node2 = TextNode("Hello", TextType.TEXT, "http://example.com")
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()
