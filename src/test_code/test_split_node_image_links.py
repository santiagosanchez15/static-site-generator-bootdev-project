import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#The most imortant thing that i learned form this project is the unit testing and how much it helps you understand how your function works
import unittest
from split_node_image_link import split_nodes_image, split_nodes_link
from textnode import TextType, TextNode

class TestTextNode(unittest.TestCase):
    def test_bootdev_test(self):
        node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_empty_list(self):
        new_nodes = split_nodes_image([])
        self.assertListEqual([], new_nodes)

    def test_split_links(self):
        node = TextNode(
            "This is a text with a link to link to the text [click here to win a thousand dollars](https.mihouse.com) and maybe another one if it doesnt work[bootdev](bootdev.com)",
            TextType.TEXT,
        )
        false_node = TextNode(
            'this is just a text', text_type=TextType.BOLD
        )
        new_nodes = split_nodes_link([node,false_node ])

        self.assertListEqual(
            [
                TextNode("This is a text with a link to link to the text ", text_type=TextType.TEXT),
                TextNode('click here to win a thousand dollars', text_type=TextType.LINK, url='https.mihouse.com'),
                TextNode(" and maybe another one if it doesnt work", text_type=TextType.TEXT),
                TextNode("bootdev", text_type=TextType.LINK, url="bootdev.com"),
                TextNode("this is just a text", text_type=TextType.BOLD)

            ], 
            new_nodes
        )

if __name__ == "__main__":
    unittest.main()