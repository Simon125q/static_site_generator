import unittest
from block_conversions import markdown_to_blocks, get_block_type, BlockType 

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

    def test_get_block_type(self) -> None:
        input1 = "# Some heading"
        result1 = get_block_type(input1)
        self.assertEqual(result1, BlockType.heading)

        input2 = "#Some not heading"
        result2 = get_block_type(input2)
        self.assertEqual(result2, BlockType.paragraph)

        input3 = "``` Some code block\nwith a lots of code\n```"
        result3 = get_block_type(input3)
        self.assertEqual(result3, BlockType.code)

        input4 = "* unordered\n* list\n- that starts with\n* *"
        result4 = get_block_type(input4)
        self.assertEqual(result4, BlockType.unordered_list)

        input5 = "1. ordered\n2. list\n3. that starts with\n4. this"
        result5 = get_block_type(input5)
        self.assertEqual(result5, BlockType.ordered_list)

        input6 = "1. ordered\n2. list\n4. that starts with\n5. this"
        result6 = get_block_type(input6)
        self.assertEqual(result6, BlockType.paragraph)
