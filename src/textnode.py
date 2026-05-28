from enum import Enum

class TextType(Enum):

    TEXT= 'normal'
    BOLD= 'bold text'
    ITALIC = 'italic text'
    CODE = "`Code text`"
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
