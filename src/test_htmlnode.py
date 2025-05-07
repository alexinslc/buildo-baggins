import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

    # LeafNode tests

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_no_tag(self):
        node = LeafNode(None, "Raw text")
        self.assertEqual(node.to_html(), "Raw text")

    def test_leaf_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

    def test_leaf_with_props(self):
        node = LeafNode("img", "", {"src": "image.png", "alt": "An image"})
        self.assertEqual(node.to_html(), '<img src="image.png" alt="An image"></img>')

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
        ]
        parent_node = ParentNode("p", children)
        self.assertEqual(
            parent_node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i></p>",
        )

    def test_to_html_with_no_tag(self):
        with self.assertRaises(ValueError) as context:
            ParentNode(None, [])
        self.assertEqual(str(context.exception), "ParentNode must have a tag.")

    def test_to_html_with_no_children(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("div", None)
        self.assertEqual(str(context.exception), "ParentNode must have a list of children.")

    def test_nested_parent_nodes(self):
        grandchild = LeafNode("i", "italic text")
        child = ParentNode("span", [grandchild])
        parent = ParentNode("div", [child, LeafNode(None, "Normal text")])
        self.assertEqual(
            parent.to_html(),
            "<div><span><i>italic text</i></span>Normal text</div>",
        )

if __name__ == "__main__":
    unittest.main()