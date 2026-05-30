from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):

    TEXT= 'normal'
    BOLD= '**'
    ITALIC = '_'
    CODE = "`code text`"
    LINK = 'link'
    IMAGE= 'image'

class TextNode:

    def __init__(self, text: str, text_type: TextType, url: str|None = None):

        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        '''Compares current TextNode, to other'''
        
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        
        return False
    
    def __repr__(self):
        '''Returns description of attributes of the current TextNode '''
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    '''Converts textnode to an leafnode'''
    if text_node.text_type not in TextType: raise Exception("text type not supported to leaf node")
    text_dict = {TextType.BOLD: 'b', TextType.ITALIC: 'i', TextType.CODE:"code", TextType.LINK:'a', TextType.IMAGE:'img'}

    if text_node.text_type == TextType.LINK:
        return LeafNode(tag=text_dict[text_node.text_type], value=text_node.text,props={'href':text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode(text_dict[text_node.text_type], value=' ', props={'src':text_node.url, 'alt':text_node.text})
    elif text_node.text_type == TextType.TEXT: 
        return LeafNode(tag=None, value=text_node.text)
    else:
        return LeafNode(tag = text_dict[text_node.text_type], value = text_node.text)