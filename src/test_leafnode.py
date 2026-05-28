import unittest
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):

    def test_leaf_to_html(self):

        leaf1 = LeafNode(tag='a', value='hello', props={'href':"bootdev.com"})
        leaf2 = LeafNode(tag='a', value='hello', props={'href':"bootdev.com"})
        
        self.assertEqual(leaf1.to_html(), leaf2.to_html())
        self.assertEqual(leaf1, leaf2)

    def test_leaf_to_html2(self):

        leaf1 = LeafNode(tag='p', value='hello', props={'href':"bootdev.com"})

        self.assertEqual(leaf1.to_html(), '''<p>hello</p>''')

    def test_leaf_html3_link(self):

        leaf1 = LeafNode(tag='a', value='hello', props={'href':"bootdev.com"})

        self.assertEqual(leaf1.to_html(), '''<a href="bootdev.com">hello</a>''')

    def test_leaf_html3_link(self):
        
        leaf1 = LeafNode(tag='b', value='hello', props={'href':"bootdev.com"})
        self.assertEqual(leaf1.to_html(), '''<b>hello</b>''')

    def test_leaf_html3_link(self):

        leaf1 = LeafNode(tag='a', value='hello', props={'href':"bootdev.com"})
        self.assertNotEqual(leaf1.to_html(), '''<a href="google.com">hello</a>''')



if __name__ == "__main__":
    unittest.main()