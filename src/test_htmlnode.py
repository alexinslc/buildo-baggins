import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_raw_text_node(self):
        # Test an HTMLNode without a tag (renders as raw text)
        node = HTMLNode(value="Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_node_with_children(self):
        # Test an HTMLNode with children but no value
        parent = HTMLNode(tag="div")
        child1 = HTMLNode(tag="p", value="Child 1")
        child2 = HTMLNode(tag="p", value="Child 2")
        parent.add_child(child1)
        parent.add_child(child2)
        self.assertEqual(
            parent.to_html(),
            '<div><p>Child 1</p><p>Child 2</p></div>'
        )

    def test_props_to_html(self):
        # Test the props_to_html method
        node = HTMLNode(tag="a", props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://example.com" target="_blank"')
        self.assertEqual(
            node.to_html(),
            '<a href="https://example.com" target="_blank"></a>'
        )

if __name__ == "__main__":
    unittest.main()