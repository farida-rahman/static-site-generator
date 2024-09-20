import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHtmlNode(unittest.TestCase):
    def test_defaults_eq(self):
        node1 = HTMLNode(value="test text inside tags")
        node2 = HTMLNode(value="test text inside tags")
        self.assertEqual(node1, node2)
    
    def test_props(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        statement = HTMLNode.props_to_html(node) == ' href="https://www.google.com" target="_blank"'
        self.assertTrue(statement)

    def test_tags(self):
        node1 = HTMLNode(tag="p")
        node2 = HTMLNode(tag="a")
        self.assertNotEqual(node1, node2)

class TestLeafNode(unittest.TestCase):
    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_same(self):
        node = LeafNode("p", "test value", props={"href": "https://www.google.com"})
        node2 = LeafNode("p", "test value", props={"href": "https://www.google.com"})
        self.assertEqual(node, node2)
    
    def test_diff(self):
        node = LeafNode("p", "test value", props={"href": "https://www.google.com"})
        node2 = LeafNode("a", "test value", props={"href": "https://www.google.com"})
        self.assertNotEqual(node, node2)
    
class TestParentNode(unittest.TestCase):
    def test_tag_is_None(self):
        with self.assertRaises(ValueError) as context:
            ParentNode(None, [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]).to_html()
        self.assertTrue("needs tag" in str(context.exception))

    def test_children_is_Empty(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("p", []).to_html()
        self.assertTrue("need to define children" in str(context.exception))
    
    def test_happy_path(self):
        node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ]).to_html()
        self.assertEqual(node, "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
    
    def test_nested(self):
        node = ParentNode(
            "div", [
                ParentNode(
                    "section", [
                        LeafNode("h1", "Title"),
                        LeafNode("p", "Some text")
                    ]
                ),
                LeafNode("footer", "Footer text")
                ]
        ).to_html()
        self.assertEqual(node, "<div><section><h1>Title</h1><p>Some text</p></section><footer>Footer text</footer></div>")

if __name__ == "__main__":
    unittest.main()