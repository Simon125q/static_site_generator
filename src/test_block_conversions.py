import unittest
from block_conversions import markdown_to_blocks 

class TestBlockConversions(unittest.TestCase):
    def test_split_blocks(self) -> None:
        input1 = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        result1 = markdown_to_blocks(input1)
        expected1 = ["# This is a heading",  
                        "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                        "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
                    ]
        self.assertEqual(result1, expected1)

        input2 = "\n# This is a heading\n\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item\n"
        result2 = markdown_to_blocks(input2)
        expected2 = ["# This is a heading",  
                        "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                        "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
                    ]
        self.assertEqual(result2, expected2)

