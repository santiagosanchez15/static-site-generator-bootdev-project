from textnode import text_node_to_html_node, TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter:str, text_type: TextType) -> list[TextNode]:
    '''Splits the node by the delimiter given and returns a list of new nodes'''

    new_list = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue

        text = node.text.split(delimiter)
        if len(text) % 2 == 0: raise Exception('No closing delimiter was found')

        for i, part in enumerate(text):

            if part == '': continue
            if i % 2 == 0: 
                new_list.append(TextNode(text=part, text_type=TextType.TEXT))
            else:
                new_list.append(TextNode(text=part, text_type=text_type))
        
    return new_list
        

