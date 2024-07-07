import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_basic_to_html(self) -> None:
        node1 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        html_result1 = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        node2 = ParentNode(
            "h1",
            [
                LeafNode("b", "Bold text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        html_result2 = "<h1><b>Bold text</b><i>italic text</i>Normal text</h1>"
        self.assertEqual(node1.to_html(), html_result1)
        self.assertEqual(node2.to_html(), html_result2)

    def test_exceptions_to_html(self) -> None:
        node1 = ParentNode(
            children = 
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        node2 = ParentNode("p", [])
        node3 = ParentNode(tag = "p")
        self.assertRaises(ValueError, node1.to_html)
        self.assertRaises(ValueError, node2.to_html)
        self.assertRaises(ValueError, node3.to_html)

    def test_nested_to_html(self) -> None:
        node1 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                ParentNode(
                    "h1",
                    [
                        LeafNode("i", "Italic text"),
                        LeafNode(None, "Normal text")
                    ]
                ),
                LeafNode(None, "Normal text"),
            ],
        )
        html_result1 = "<p><b>Bold text</b>Normal text<h1><i>Italic text</i>Normal text</h1>Normal text</p>"
        node2 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                ParentNode(
                    "h1",
                    [
                        LeafNode("i", "Italic text"),
                        ParentNode(
                            "div",
                            [
                                LeafNode(None, "Normal text"),
                                LeafNode("i", "Italic text")
                            ]
                        ),
                        LeafNode(None, "Normal text"),
                        LeafNode("b", "Bold text")
                    ]
                ),
                LeafNode(None, "Normal text"),
            ],
        )
        html_result2 = "<p><b>Bold text</b>Normal text<h1><i>Italic text</i><div>Normal text<i>Italic text</i></div>Normal text<b>Bold text</b></h1>Normal text</p>"
        self.assertEqual(node1.to_html(), html_result1)
        self.assertEqual(node2.to_html(), html_result2)




