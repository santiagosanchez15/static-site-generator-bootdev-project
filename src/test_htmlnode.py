import unittest
from htmlnode import HTMLNODE

class TestTextNode(unittest.TestCase):

    def test_eqnode(self):

        node = HTMLNODE(tag='p', value='test1', props={'href':'google.com'})
        node2 = HTMLNODE(tag='p', value='test1', props={'href':'google.com'})

        self.assertEqual(node, node2)

    def test_eqnot(self):

        node = HTMLNODE(tag='p',value='test1', props={'href':'google.com'})
        node2 = HTMLNODE(tag='p', value='test1', props={'href':'google.com'})
        node3 = HTMLNODE(tag='p', value='test1', props={'href':'google.com'}, children=[node2, node])

        self.assertNotEqual(node3, node2)

    def test_eq3samechildren(self):

        node = HTMLNODE(tag='p',value='test1', props={'href':'google.com'})
        node2 = HTMLNODE(tag='p', value='test1', props={'href':'google.com'}, children=[node])
        node3 = HTMLNODE(tag='p', value='test1', props={'href':'google.com'}, children=[node])

        self.assertEqual(node3, node2)

    def test_eqDesc(self):

        node = HTMLNODE(tag='p',value='test1', props={'href':'google.com'})
        node2 = HTMLNODE(tag='p', value='test1', props={'href':'google.com'}, children=[node])

        self.assertEqual(node.props_to_html(), '''href="google.com"''')
        self.assertEqual(node.props_to_html(), node2.props_to_html())

    def test_eqnot_samedict(self):

        node = HTMLNODE(tag='p',value='test1', props={'href':'google.com'})
        node2 = HTMLNODE(tag='p', value='test1', props={'href':'bootdev.com'}, children=[node])

        self.assertNotEqual(node.props_to_html(), node2.props_to_html())

    def test_eq_large_props(self):

        node = HTMLNODE(tag='p',value='test1', props={'href':'google.com', 'imgsrc':"bootdev.com"})
        self.assertEqual(node.props_to_html(), '''href="google.com" imgsrc="bootdev.com"''')




        

if __name__ == "__main__":
    unittest.main()