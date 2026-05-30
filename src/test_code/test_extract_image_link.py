import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from extract_image_links import extract_markdown_images, extract_markdown_links

class TestTextNode(unittest.TestCase):

    def test_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        broken_apart = extract_markdown_images(text)
        
        self.assertEqual(broken_apart, [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')])

    def test_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        broken_apart = extract_markdown_links(text)
        self.assertEqual(broken_apart, [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])

    def test_my_test(self):

        text = "blablabla bla bla ![example](letshopeitworks.com)"
        broken_apart = extract_markdown_images(text)
        self.assertEqual(broken_apart, [("example", "letshopeitworks.com")])


if __name__ == "__main__":
    unittest.main()