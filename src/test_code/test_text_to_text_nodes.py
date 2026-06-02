import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from text_to_text_nodes import text_to_textnodes
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_bootdev_test(self):
        text = '''This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'''

        given_list = text_to_textnodes(text)

        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ], given_list
        )
    
    def test_no_image_link(self):
        text = '''`i want to code some stuff` i was **having a good time** _until i found out_ that i could **have a better time**'''
        given_list = text_to_textnodes(text)

        self.assertListEqual(
            [
                TextNode("i want to code some stuff", TextType.CODE),
                TextNode(' i was ', text_type=TextType.TEXT),
                TextNode("having a good time", TextType.BOLD),
                TextNode(" ", TextType.TEXT),
                TextNode("until i found out", TextType.ITALIC),
                TextNode(" that i could ", TextType.TEXT),
                TextNode("have a better time", TextType.BOLD)
            ], given_list
        )

if __name__ == "__main__":
    unittest.main()
