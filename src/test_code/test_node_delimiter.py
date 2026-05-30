import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from textnode import TextNode, TextType, text_node_to_html_node
from split_node_delimiter import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    
    def test_expc1(self):
        
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(text_node_to_html_node(new_nodes[1]).to_html(), "<code>code block</code>")
        
    def test_bold(self):

        node = TextNode("this is a text with a ;google.com; block i really hope it works", TextType.TEXT)
        node2 = TextNode("link block, praying the gods", TextType.LINK, url="google.com")
        new_nodes = split_nodes_delimiter([node, node2], ";", TextType.IMAGE)
        
        self.assertEqual(new_nodes[2].text_type, TextType.IMAGE)
        self.assertEqual(new_nodes[0].text_type, TextType.LINK)
        self.assertEqual(text_node_to_html_node(new_nodes[2]).to_html(), '''<img src="None" alt="google.com">''')
        self.assertEqual(text_node_to_html_node(new_nodes[0]).to_html(), '''<a href="google.com">link block, praying the gods</a>''')

    def test_new_delimiter(self):

        node = TextNode("this is a text with a |google.com| block i really hope it works", TextType.TEXT)
        node2 = TextNode("link block, praying the gods", TextType.LINK, url="google.com")

        self.assertRaises(Exception, split_nodes_delimiter, [node, node2])
        new_nodes = split_nodes_delimiter([node, node2], '|', TextType.BOLD)
        self.assertNotEqual(new_nodes[2].text_type, TextType.ITALIC)
        self.assertEqual(new_nodes[2].text_type, TextType.BOLD)
        print(new_nodes[0].text_type)
        self.assertEqual(new_nodes[0].text_type, TextType.LINK)
        




    


if __name__ == "__main__":
    unittest.main()