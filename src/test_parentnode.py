from parentnode import PARENTNODE
from htmlnode import LeafNode
import unittest

class TestTextNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = PARENTNODE("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = PARENTNODE("span", [grandchild_node])
        parent_node = PARENTNODE("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_no_children(self):

        self.assertRaises(ValueError, PARENTNODE('p',[]).to_html)
    
    def test_to_html_no_tag(self):

        child_node = LeafNode("span", "child")
        parent_node = PARENTNODE("div", [child_node])
        self.assertRaises(ValueError, PARENTNODE('',[child_node]).to_html)
        

if __name__ == "__main__":
    unittest.main()