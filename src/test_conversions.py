import unittest
from conversions import split_nodes_delimiter
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







        
