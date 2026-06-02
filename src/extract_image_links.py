
import re

def extract_markdown_images(text:str) -> list[tuple[str,str]]:
    '''gets alt and src for image from text and returns list of tuples (alt, src)'''

    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text) #FIX ME needs to be improven so false structure is not taken into account

def extract_markdown_links(text:str) -> list[tuple[str,str]]:
    '''gets the href and the url for the link given in plain text by given sequence predetermined by markwdown'''

    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text) #FIX ME needs to be improven so false structure is not taken into account


