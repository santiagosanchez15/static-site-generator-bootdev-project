from textnode import TextNode, TextType
from extract_image_links import extract_markdown_images, extract_markdown_links


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    '''split raw markdown and converts to TextNode for images'''

    new_list = []

    for node in old_nodes:
       
       if node.text_type != TextType.TEXT: 
          new_list.append(node)
          continue
        #need to change pretty much everything for underneath using the new functions, 
       current_text = node.text
       images = extract_markdown_images(current_text)

       for image in images:
           image_markdown = f"![{image[0]}]({image[1]})"
           sections = current_text.split(image_markdown, 1)

           if sections[0] != "": new_list.append(TextNode(sections[0], TextType.TEXT))
           new_list.append(TextNode(image[0], TextType.IMAGE, image[1]))
           current_text = sections[1]
        
       if current_text != "": new_list.append(TextNode(current_text, TextType.TEXT))


    return new_list
    

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    '''split raw markdown and converts to Textnode for links'''

    new_list = []

    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue

        current_text = node.text
        links = extract_markdown_links(current_text)

        for link in links:
            link_markdown = f"[{link[0]}]({link[1]})"
            sections = current_text.split(link_markdown, 1)

            if sections[0] != '': 
                new_list.append(TextNode(sections[0], TextType.TEXT))
            
            new_list.append(TextNode(link[0], TextType.LINK, link[1]))
            current_text = sections[1]
        
        if current_text != '':
            new_list.append(TextNode(current_text, TextType.TEXT))

    return new_list