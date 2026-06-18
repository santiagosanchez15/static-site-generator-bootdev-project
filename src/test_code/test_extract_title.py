import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from extract_title import extract_title


class TestTextNode(unittest.TestCase):

    def test_just_has(self):
        text = '# hello'
        result = extract_title(text)
        self.assertEqual(result, 'hello')

    def test_two_hashes(self):
        text = "## hello"
        self.assertRaises(Exception, extract_title, text)

    def test_new_lines(self):

        text = """hello
what am i doing
# this is the title"""
        result = extract_title(text)
        self.assertEqual(result, "this is the title")



if __name__ == "__main__":
    unittest.main()