import unittest
from textnode import TextNode, TextType

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

if __name__ == "__main__":
    unittest.main()