from textnode import TextType, TextNode
from split_node_delimiter import split_nodes_delimiter
from split_node_image_link import split_nodes_image, split_nodes_link


def text_to_textnodes(text:str) -> list[TextNode]:
    '''From raw texts returns a list of Textnode that contain the html tag'''
    current_list = [TextNode(text, text_type=TextType.TEXT)] #starts by creating a raw text for everything
    
    for type in TextType: #loop through every texttype

        if type == TextType.IMAGE: #SPECIAL CASE, IMAGE, use split image
            current_list = split_nodes_image(current_list)
        elif type == TextType.LINK:#SPECIAL CASE, LINK use split LINK
            current_list = split_nodes_link(current_list)
        else:
            current_list = split_nodes_delimiter(current_list, delimiter=type.value, text_type=type) #use regular split

   
    return current_list



    