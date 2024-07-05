import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        leaf1 = LeafNode("p", "This is a paragraph of text.")
        leaf2 = LeafNode(value="Click me!")
        leaf3 = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        leaf4 = LeafNode(value="Click me!", props={"href": "https://www.google.com"})
        leaf5 = LeafNode(tag="a", props={"href": "https://www.google.com"})
        self.assertEqual(leaf1.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(leaf2.to_html(), "Click me!")
        self.assertEqual(leaf3.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")
        self.assertRaises(ValueError, leaf4.to_html)
        self.assertRaises(ValueError, leaf5.to_html)
