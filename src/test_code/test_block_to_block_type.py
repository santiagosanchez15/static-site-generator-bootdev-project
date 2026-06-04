import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from block_types import block_to_block_type, BlockType
from markdown_to_blocks import markdown_to_blocks

class TestTextNode(unittest.TestCase):

    def test_blocktype_paragraph(self):
        
        text = "hello hwo are you"
        block_given = block_to_block_type(text)
        self.assertEqual(block_given, BlockType.paragraph)

    def test_block_heading(self):

        text = "###### hello hwo are you"
        block_given = block_to_block_type(text)
        self.assertEqual(block_given, BlockType.heading)

    def test_block_heading_2(self):
        
        text = "### hello"
        block_given = block_to_block_type(text)
        self.assertEqual(block_given, BlockType.heading)

    def test_block_heading_3(self):

        text = "#######"
        block_given = block_to_block_type(text)
        self.assertEqual(block_given, BlockType.paragraph)

    def test_block_heading_4(self):

        text = "####hello"
        block_given = block_to_block_type(text)
        self.assertEqual(block_given, BlockType.paragraph)

    def test_code_block(self):

        text = "```\n im going to code some stuff```"
        block_given = block_to_block_type(text)
        self.assertEqual(block_given, BlockType.code)

    def test_code_block2(self):

        text = "``\n im going to code some stuff```"
        block_given = block_to_block_type(text)
        self.assertEqual(block_given, BlockType.paragraph)
    
    def test_quote(self):

        text = "> this is a quote"
        block_given = block_to_block_type(text)
        self.assertEqual(block_given, BlockType.quote)

    def test_no_quote(self):

        text = '< this is not a quote #####'
        block_given = block_to_block_type(text)
        self.assertEqual(block_given, BlockType.paragraph)

    def test_unordered_list(self):

        text = """- hello this is an unordered list
- this continues the list"""
        block_given = block_to_block_type(text)
        self.assertEqual(block_given, BlockType.unordered_list)

    def test_not_unordered_list(self):

        text = """- hello this is an unordered list
this continues the list"""
        block_given = block_to_block_type(text)
        self.assertEqual(block_given, BlockType.paragraph)

    def test_ordered_list(self):

        text = """1. this is the first item
2. this is the second item
3. this is the third item"""
        block_given = block_to_block_type(text)
        self.assertEqual(block_given, BlockType.ordered_list)

        def test_not_ordered_list(self):

            text = """1. this is the first item
2. this is the second item
3. this is the third item"""
            block_given = block_to_block_type(text)
            self.assertEqual(block_given, BlockType.paragraph)    
        





if __name__ == "__main__":
    unittest.main()