import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from markdown_to_html_node import markdown_to_html_node

class TestTextNode(unittest.TestCase):

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    
    def test_unorder_list_block(self):
        md="""
- hello how are you
- how is everything going
"""     
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, 
                         "<div><ul><li>hello how are you</li><li>how is everything going</li></ul></div>")
        
    def test_ordered_list_block(self):
        md="""
1. hello how are you
2. how is everything going
"""  
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, 
                         "<div><ol><li>hello how are you</li><li>how is everything going</li></ol></div>")
        
    def test_quotes_block(self):
        md="""
> hello how are you
> how is everything going
"""  
        node = markdown_to_html_node(md)
        html = node.to_html()
        
        self.assertEqual(html, 
                         "<div><blockquote>hello how are you how is everything going</blockquote></div>")
    
    def test_quotes_block2(self):
        md="""
>hello how are you
>how is everything going
"""  
        node = markdown_to_html_node(md)
        html = node.to_html()
        
        self.assertEqual(html, 
                         "<div><blockquote>hello how are you how is everything going</blockquote></div>")
        
    def test_headings_block(self):
        md = """
###### this should be a heading of 6
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, 
                         "<div><h6>this should be a heading of 6</h6></div>")
    
    def test_headings_block(self):
        md = """
####### this should not be a heading
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, 
                         "<div><p>####### this should not be a heading</p></div>")


if __name__ == "__main__":
    unittest.main()