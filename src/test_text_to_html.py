import unittest
from textnode import TextNode, TextType
from markdown_conversions import text_node_to_html_node

class TestConvertsions(unittest.TestCase):
    def test_text_to_html(self) -> None:
        node1 = TextNode("This is a text node", TextType.text)
        node2 = TextNode("This is a text node", TextType.bold)
        node3 = TextNode("This is a text node", TextType.italic)
        node4 = TextNode("This is a text node", TextType.code)
        node5 = TextNode("This is a text node", TextType.link, "https://test.com")
        node6 = TextNode("This is a text node", TextType.image, "https://test.com")
        node7 = TextNode("This is a text node", "eerror", "https://test.com")
        exp1 = "This is a text node"
        exp2 = "<b>This is a text node</b>"
        exp3 = "<i>This is a text node</i>"
        exp4 = "<code>This is a text node</code>"
        exp5 = "<a href=\"https://test.com\">This is a text node</a>"
        exp6 = "<img src=\"https://test.com\" alt=\"This is a text node\"></img>"
        self.assertEqual(text_node_to_html_node(node1).to_html(), exp1)
        self.assertEqual(text_node_to_html_node(node2).to_html(), exp2)
        self.assertEqual(text_node_to_html_node(node3).to_html(), exp3)
        self.assertEqual(text_node_to_html_node(node4).to_html(), exp4)
        self.assertEqual(text_node_to_html_node(node5).to_html(), exp5)
        self.assertEqual(text_node_to_html_node(node6).to_html(), exp6)
        self.assertRaises(Exception, text_node_to_html_node, node7)
