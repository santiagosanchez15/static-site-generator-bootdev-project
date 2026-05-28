from enum import Enum

class TextType(Enum):

    text= 'normal'
    bold_text= 'bold text'
    italic_text = 'italic text'
    code_text = "`Code text`"
    links = 'link'
    images= 'image'

