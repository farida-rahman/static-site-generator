import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_default_url(self):
        #checking that the url is None when nothing is entered
        node1 = TextNode("This is a text node", "bold", "https://www.youtube.com/feed/subscriptions")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node1, node2)

    def test_diff_type(self):
        #checking that the url is None when nothing is entered
        node1 = TextNode("This is a text node", "italics")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node1, node2)

class TestTextToHTML(unittest.TestCase):
    def test_unspecified(self):
        with self.assertRaises(Exception) as context:
            TextNode("some text here", None).text_node_to_html()
        self.assertTrue("text type not specified" in str(context.exception))
    
    def test_bold(self):
        node = TextNode("trying to see what this returns", "bold").text_node_to_html()
        self.assertEqual(node.to_html(), '<b>trying to see what this returns</b>')

class TestSplitDelimiters(unittest.TestCase):
    def test_code_split(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = TextNode.split_nodes_delimiter([node], "`", "code")
        result = [
            TextNode("This is text with a ", "text"),
            TextNode("code block", "code"),
            TextNode(" word", "text")
            ]
        self.assertEqual(new_nodes, result)



if __name__ == "__main__":
    unittest.main()