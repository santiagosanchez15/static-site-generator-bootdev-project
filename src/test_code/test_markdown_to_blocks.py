import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from markdown_to_blocks import markdown_to_blocks


class TestTextNode(unittest.TestCase):
    
    def test_bootdev(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
            """
        blocks = markdown_to_blocks(md)
        
        self.assertListEqual(
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ], blocks
        )
    
    def test_mine(self):
        md = """
this is
together 

this is 

separate 
            """
        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            [
                "this is\ntogether", 
                "this is",
                "separate"
            ], blocks
        )

    def test_lots_spaces(self):
        md = """
hello






"""
        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            [
                'hello'
            ], blocks
        )

if __name__ == "__main__":
    unittest.main()