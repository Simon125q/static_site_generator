import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self) -> None:
        node = TextNode("This is a text node", "bold", "https://test.com")
        node2 = TextNode("This is a text node", "bold", "https://test.com")
        self.assertEqual(node, node2)

    def test_eq_no_url(self) -> None:
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq_text(self) -> None:
        node = TextNode("This is a text node", "bold", "https://test.com")
        node2 = TextNode("This is a diff text node", "bold", "https://test.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_type(self) -> None:
        node = TextNode("This is a text node", "italic", "https://test.com")
        node2 = TextNode("This is a text node", "bold", "https://test.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self) -> None:
        node = TextNode("This is a text node", "bold", "https://test.com")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
