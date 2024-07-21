import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode
import leafnode
from markdown_conversions import markdown_to_html_node
from parentnode import ParentNode
from textnode import TextNode

class TestMarkdownConversions(unittest.TestCase):
    def test_markdown_to_html_node(self) -> None:
        input1 = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        result1 = markdown_to_html_node(input1)
        expected1 = HTMLNode(tag = "div", 
                             value = None, 
                             children = [
                                LeafNode("h1", value="This is a heading"),
                                ParentNode("p", children=[
                                        LeafNode(None, value="This is a paragraph of text. It has some "),
                                        LeafNode("b", value="bold"),
                                        LeafNode(None, value=" and "),
                                        LeafNode("i", value="italic"),
                                        LeafNode(None, value=" words inside of it.")
                                    ]),
                                ParentNode("ul", children=[
                                        LeafNode("li", "This is the first list item in a list block"),
                                        LeafNode("li", "This is a list item"),
                                        LeafNode("li", "This is another list item")
                                    ])
                             ])
        self.assertEqual(str(result1), str(expected1))

        input2 = "#### This is a heading\n\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it and [link_name](https//test_link.com).\n\n> This is the first quote in a quote block\n>This is a quote item\n> This is another quote item\n"
        result2 = markdown_to_html_node(input2)
        expected2 = HTMLNode(tag = "div", 
                             value = None, 
                             children = [
                                LeafNode("h4", value="This is a heading"),
                                ParentNode("p", children=[
                                        LeafNode(None, value="This is a paragraph of text. It has some "),
                                        LeafNode("b", value="bold"),
                                        LeafNode(None, value=" and "),
                                        LeafNode("i", value="italic"),
                                        LeafNode(None, value=" words inside of it and "),
                                        LeafNode("a", value="link_name", props={"href": "https//test_link.com"}),
                                        LeafNode(None, value=".")
                                    ]),
                                LeafNode("blockquote", value=" This is the first quote in a quote block\nThis is a quote item\n This is another quote item")
                             ])
        self.assertEqual(str(result2), str(expected2))

        input3 = "##### This is a **bold** heading\n\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it and ![img name](https//test_img_link.com)\n\n1. This is the first *list* in a list block\n2. This is a list item with [link](https//example.com)\n3. This is another list item\n"
        result3 = markdown_to_html_node(input3)
        expected3 = HTMLNode(tag = "div", 
                             value = None, 
                             children = [
                                ParentNode("h5", children=[
                                        LeafNode(None, value="This is a "),
                                        LeafNode("b", value="bold"),
                                        LeafNode(None, value=" heading")
                                    ]),
                                ParentNode("p", children=[
                                        LeafNode(None, value="This is a paragraph of text. It has some "),
                                        LeafNode("b", value="bold"),
                                        LeafNode(None, value=" and "),
                                        LeafNode("i", value="italic"),
                                        LeafNode(None, value=" words inside of it and "),
                                        LeafNode("img", value="", props={"src": "https//test_img_link.com", "alt": "img name"})
                                    ]),
                                ParentNode("ol", children=[
                                        ParentNode("li", children=[
                                            LeafNode(None, value="This is the first "),
                                            LeafNode("i", value="list"),
                                            LeafNode(None, value=" in a list block")
                                        ]),
                                        ParentNode("li", children=[
                                            LeafNode(None, value="This is a list item with "),
                                            LeafNode("a", value="link", props={"href": "https//example.com"})
                                        ]),
                                        LeafNode("li", value="This is another list item")
                                    ])
                             ])
        self.assertEqual(str(result3), str(expected3))
