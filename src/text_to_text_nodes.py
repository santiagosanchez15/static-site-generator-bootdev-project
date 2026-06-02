from textnode import TextType, TextNode
from split_node_delimiter import split_nodes_delimiter
from split_node_image_link import split_nodes_image, split_nodes_link


def text_to_textnodes(text:str) -> list[TextNode]:
    '''From raw texts returns a list of Textnode that contain the html tag'''
    current_list = [TextNode(text, text_type=TextType.TEXT)]
    
    for type in TextType:

        if type == TextType.IMAGE:
            current_list = split_nodes_image(current_list)
        elif type == TextType.LINK:
            current_list = split_nodes_link(current_list)
        else:
            current_list = split_nodes_delimiter(current_list, delimiter=type.value, text_type=type)

   
    return current_list



    