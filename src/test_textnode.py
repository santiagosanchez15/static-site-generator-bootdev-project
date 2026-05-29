import unittest
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2not(self):
        node3 = TextNode('random text', TextType.TEXT, url="http://localhost:8888")
        node4 = TextNode('hello', TextType.IMAGE, 'http://localhost:8888')

        self.assertNotEqual(node3, node4)

    def test_eq3(self):
        
        node = TextNode('checking', TextType.TEXT)
        node2 = TextNode('checking', TextType.TEXT)

        self.assertEqual(node, node2)

    def test_eq4(self):

        node = TextNode('wow', TextType.TEXT)
        node2 = TextNode('checking', TextType.TEXT)

        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        
        node = TextNode(text='hello', text_type=TextType.BOLD)
        new_leaf = text_node_to_html_node(node)
        self.assertEqual(new_leaf.to_html(), '''<b>hello</b>''')
        self.assertEqual(new_leaf.tag, 'b')
        self.assertEqual(new_leaf.children, None)

    def test_image(self):
        node = TextNode(text= 'hello im an image', text_type=TextType.IMAGE, url="bootdeve.com")
        new_leaf = text_node_to_html_node(node)
        self.assertEqual(new_leaf.to_html(),'''<img src="bootdeve.com" alt="hello im an image">''')

    def test_link(self):

        node = TextNode(text='Hello this is a link', text_type=TextType.LINK, url='anamazinglinkihopeigetanewjobsoon.ong')
        new_leaf = text_node_to_html_node(node)
        self.assertEqual(new_leaf.to_html(), '''<a href="anamazinglinkihopeigetanewjobsoon.ong">Hello this is a link</a>''')

    def test_italics(self):

        node = TextNode(text='hello', text_type=TextType.ITALIC)
        new_leaf = text_node_to_html_node(node)
        self.assertEqual(new_leaf.to_html(), "<i>hello</i>")

    def test_code(self):
        node = TextNode(text='hello', text_type=TextType.CODE)
        new_leaf = text_node_to_html_node(node)
        self.assertEqual(new_leaf.to_html(), "<code>hello</code>")

    def test_exception(self):
        node = TextNode(text='hello', text_type='p')
        self.assertRaises(Exception, text_node_to_html_node, node)


if __name__ == "__main__":
    unittest.main()