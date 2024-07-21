import unittest
from page_generator import extract_title

class TestPageGenerator(unittest.TestCase):
    def test_extract_title(self) -> None:
        input1 = "# heading\n\n# other heading"
        result1 = extract_title(input1)
        expected1 = "heading"
        self.assertEqual(result1, expected1)

        input2 = "> not heading\n\n# this is heading"
        result2 = extract_title(input2)
        expected2 = "this is heading"
        self.assertEqual(result2, expected2)

        input3 = "not a heading\n\n* also not a heading"
        self.assertRaises(Exception, extract_title, input3)
