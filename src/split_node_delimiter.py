from textnode import text_node_to_html_node, TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter:str, text_type: TextType) -> list[TextNode]:
    '''Splits the node by the delimiter given and returns a list of new nodes'''

    new_list = [] #creates accumulator

    for node in old_nodes: #loop through the list of nodes given
        if node.text_type != TextType.TEXT: # if the type of node is not text then ignore and append to list go to next node
            new_list.append(node)
            continue

        text = node.text.split(delimiter) #split the text by given delimiter
        if len(text) % 2 == 0: raise Exception('No closing delimiter was found') # if its even then that means that there was no closing value

        for i, part in enumerate(text): #remember enumerate starts at 0 linked to value (part)

            if part == '': continue #if empty becasue of split then go to next
            if i % 2 == 0: #if even this means that is just text add to list 
                new_list.append(TextNode(text=part, text_type=TextType.TEXT))
            else: #odd i means that the value acquaried add to list
                new_list.append(TextNode(text=part, text_type=text_type))
        
    return new_list
        

