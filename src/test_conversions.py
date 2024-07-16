import unittest
from conversions import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextType, TextNode

class TestConversions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
        
    def setUp(self):
        self.node1 = TextNode("This is text with a **bolded phrase** in the middle", TextType.text, None)
        self.res1 = [
            TextNode("This is text with a ", TextType.text),
            TextNode("bolded phrase", TextType.bold),
            TextNode(" in the middle", TextType.text),
        ]
        self.node2 = TextNode("This is text with a `code block` word", TextType.text, None)
        self.res2 = [
            TextNode("This is text with a ", TextType.text),
            TextNode("code block", TextType.code),
            TextNode(" word", TextType.text),
        ]        
        self.node3 = TextNode("*code block*", TextType.text, None)
        self.res3 = [
            TextNode("", TextType.text),
            TextNode("code block", TextType.italic),
            TextNode("", TextType.text),
        ]        
        self.node4 = TextNode("This is text with a **bolded phrase** in the middle and this is **bolded phrase**", TextType.text, None)
        self.res4 = [
            TextNode("This is text with a ", TextType.text),
            TextNode("bolded phrase", TextType.bold),
            TextNode(" in the middle and this is ", TextType.text),
            TextNode("bolded phrase", TextType.bold),
            TextNode("", TextType.text),
        ]
        self.node5 = TextNode("This `code block` and this `code block` is text with a `code block` word", TextType.text, None)
        self.res5 = [
            TextNode("This ", TextType.text),
            TextNode("code block", TextType.code),
            TextNode(" and this ", TextType.text),
            TextNode("code block", TextType.code),
            TextNode(" is text with a ", TextType.text),
            TextNode("code block", TextType.code),
            TextNode(" word", TextType.text),
        ]        

    def tearDown(self):
        pass
        
    def test_single_nodes_spliting(self) -> None:
        self.assertEqual(split_nodes_delimiter([self.node1], "**", TextType.bold), self.res1) 
        self.assertEqual(split_nodes_delimiter([self.node2], "`", TextType.code), self.res2) 
        self.assertEqual(split_nodes_delimiter([self.node3], "*", TextType.italic), self.res3) 
    
    def test_node_spliting_whith_multi_splits(self) -> None:
        self.assertEqual(split_nodes_delimiter([self.node4], "**", TextType.bold), self.res4) 
        self.assertEqual(split_nodes_delimiter([self.node5], "`", TextType.code), self.res5) 

    def test_multi_nodes_spliting(self) -> None:
        self.assertEqual(split_nodes_delimiter([self.node1, self.node2, self.node3],
                         "`", TextType.code), [self.node1] + self.res2 + [self.node3])
        self.assertEqual(split_nodes_delimiter(
                          [self.node1, self.node2, self.node3, self.node4, self.node5],
                          "**", TextType.bold),
                          self.res1 + [self.node2] + [self.node3] + self.res4 + [self.node5])
        self.assertEqual(split_nodes_delimiter(
                          [self.node1, self.node2, self.node3, self.node4, self.node5],
                          "`", TextType.code),
                          [self.node1] + self.res2 + [self.node3] + [self.node4] + self.res5)

    def test_extract_markdown_imgs(self) -> None:
        text1 = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result1 = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extract_markdown_images(text1), result1)
        text2 = "This is text without any images"
        result2 = []
        self.assertEqual(extract_markdown_images(text2), result2)

    def test_extract_markdown_urls(self) -> None:
        text1 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result1 = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extract_markdown_links(text1), result1)
        text2 = "This is text with a link [to boot dev](https://www.boot.dev) and thisis img ![youtube](https://www.youtube.com/img)"
        result2 = [("to boot dev", "https://www.boot.dev")]
        self.assertEqual(extract_markdown_links(text2), result2)
        text3 = "[to boot dev](https://www.boot.dev)"
        result3 = [("to boot dev", "https://www.boot.dev")]
        self.assertEqual(extract_markdown_links(text3), result3)
        text4 = "dev](https://www.boot.dev)"
        result4 = []
        self.assertEqual(extract_markdown_links(text4), result4)

    def test_split_nodes_image(self) -> None:
        node1 = TextNode(
            "This is text with a image ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.text,
        )
        node2 = TextNode(
            "![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.text,
        )
        node3 = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.text,
        )
        node4 = TextNode(
            "![to boot dev](https://www.boot.dev)",
            TextType.text,
        )
        result1 = split_nodes_image([node1])
        expected1 = [
            TextNode("This is text with a image ", TextType.text),
            TextNode("to boot dev", TextType.image, "https://www.boot.dev"),
            TextNode(" and ", TextType.text),
            TextNode(
                "to youtube", TextType.image, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertEqual(result1, expected1)

        result2 = split_nodes_image([node1, node2, node3, node4])
        expected2 = [
            TextNode("This is text with a image ", TextType.text),
            TextNode("to boot dev", TextType.image, "https://www.boot.dev"),
            TextNode(" and ", TextType.text),
            TextNode(
                "to youtube", TextType.image, "https://www.youtube.com/@bootdotdev"
            ),
            TextNode("to boot dev", TextType.image, "https://www.boot.dev"),
            TextNode(" and ", TextType.text),
            TextNode(
                "to youtube", TextType.image, "https://www.youtube.com/@bootdotdev"
            ),
            TextNode(
                "This is text with a link [to boot dev](https://www.boot.dev) and ",
                     TextType.text
            ),
            TextNode(
                "to youtube", TextType.image, "https://www.youtube.com/@bootdotdev"
            ),
            TextNode("to boot dev", TextType.image, "https://www.boot.dev")
        ]
        self.assertEqual(result2, expected2)

    def test_split_nodes_link(self) -> None:
        node1 = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.text,
        )
        node2 = TextNode(
            "[to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.text,
        )
        node3 = TextNode(
            "This is text with a image ![to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.text,
        )
        node4 = TextNode(
            "[to boot dev](https://www.boot.dev)",
            TextType.text,
        )
        result1 = split_nodes_link([node1])
        expected1 = [
            TextNode("This is text with a link ", TextType.text),
            TextNode("to boot dev", TextType.link, "https://www.boot.dev"),
            TextNode(" and ", TextType.text),
            TextNode(
                "to youtube", TextType.link, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertEqual(result1, expected1)

        result2 = split_nodes_link([node1, node2, node3, node4])
        expected2 = [
            TextNode("This is text with a link ", TextType.text),
            TextNode("to boot dev", TextType.link, "https://www.boot.dev"),
            TextNode(" and ", TextType.text),
            TextNode(
                "to youtube", TextType.link, "https://www.youtube.com/@bootdotdev"
            ),
            TextNode("to boot dev", TextType.link, "https://www.boot.dev"),
            TextNode(" and ", TextType.text),
            TextNode(
                "to youtube", TextType.link, "https://www.youtube.com/@bootdotdev"),
            TextNode(
                "This is text with a image ![to boot dev](https://www.boot.dev) and ",
                     TextType.text
            ),
            TextNode(
                "to youtube", TextType.link, "https://www.youtube.com/@bootdotdev"
            ),
            TextNode("to boot dev", TextType.link, "https://www.boot.dev")
        ]
        self.assertEqual(result2, expected2)

    def test_text_to_textnodes(self) -> None:
        input1 = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        result1 = text_to_textnodes(input1)
        expected1 = [
                TextNode("This is ", TextType.text),
                TextNode("text", TextType.bold),
                TextNode(" with an ", TextType.text),
                TextNode("italic", TextType.italic),
                TextNode(" word and a ", TextType.text),
                TextNode("code block", TextType.code),
                TextNode(" and an ", TextType.text),
                TextNode("obi wan image", TextType.image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and a ", TextType.text),
                TextNode("link", TextType.link, "https://boot.dev"),
            ]
        self.assertEqual(result1, expected1)

        
