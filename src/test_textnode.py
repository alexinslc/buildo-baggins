import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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
        self.assertNotEqual(node1, node2)

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

    def test_text(self):
         node = TextNode("This is a text node", TextType.TEXT)
         html_node = text_node_to_html_node(node)
         self.assertEqual(html_node.tag, None)
         self.assertEqual(html_node.value, "This is a text node")
    
    def test_bold(self):
         node = TextNode("This is bold text", TextType.BOLD)
         html_node = text_node_to_html_node(node)
         self.assertEqual(html_node.tag, "b")
         self.assertEqual(html_node.value, "This is bold text")

    def test_italic(self):
         node = TextNode("This is italic text", TextType.ITALIC)
         html_node = text_node_to_html_node(node)
         self.assertEqual(html_node.tag, "i")
         self.assertEqual(html_node.value, "This is italic text")

    def test_code(self):
         node = TextNode("This is code text", TextType.CODE)
         html_node = text_node_to_html_node(node)
         self.assertEqual(html_node.tag, "code")
         self.assertEqual(html_node.value, "This is code text")

    def test_link(self):
            node = TextNode("This is a link", TextType.LINK, "http://example.com")
            html_node = text_node_to_html_node(node)
            self.assertEqual(html_node.tag, "a")
            self.assertEqual(html_node.value, "This is a link")
            self.assertEqual(html_node.props["href"], "http://example.com")

    def test_image(self):
            node = TextNode("This is an image", TextType.IMAGE, "http://example.com/image.png")
            html_node = text_node_to_html_node(node)
            self.assertEqual(html_node.tag, "img")
            self.assertEqual(html_node.value, "")
            self.assertEqual(html_node.props["src"], "http://example.com/image.png")
            self.assertEqual(html_node.props["alt"], "This is an image")


if __name__ == "__main__":
    unittest.main()
