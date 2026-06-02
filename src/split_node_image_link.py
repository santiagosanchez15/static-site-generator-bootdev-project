from textnode import TextNode, TextType
from extract_image_links import extract_markdown_images, extract_markdown_links


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    '''split raw markdown and converts to TextNode for images'''

    new_list = [] #create accumulator

    for node in old_nodes:
       
       if node.text_type != TextType.TEXT: # if value is raw text then continue
          new_list.append(node)
          continue
        
       current_text = node.text #keep track of current text 
       images = extract_markdown_images(current_text) #extract current values of image and url

       for image in images: #loop thorugh list of tuples
           image_markdown = f"![{image[0]}]({image[1]})" #build up filter
           sections = current_text.split(image_markdown, 1) #filter up to one condition at a time

           if sections[0] != "": new_list.append(TextNode(sections[0], TextType.TEXT)) #if value of text at given section is not empty then append it to list as raw text
           new_list.append(TextNode(image[0], TextType.IMAGE, image[1])) #append the value of the image for value and url
           current_text = sections[1] #update the current text as the second part of the text and repeat
        
       if current_text != "": new_list.append(TextNode(current_text, TextType.TEXT)) #any leaft overs just append as text


    return new_list
    

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    '''split raw markdown and converts to Textnode for links'''

    new_list = [] # create accumulator

    for node in old_nodes: #loop thorugh list of nodes

        if node.text_type != TextType.TEXT: #if node is not raw text then just append to list
            new_list.append(node)
            continue

        current_text = node.text #keep track of current text
        links = extract_markdown_links(current_text) # get links from given text

        for link in links:
            link_markdown = f"[{link[0]}]({link[1]})" #build up the filter
            sections = current_text.split(link_markdown, 1) #filter up to one iteration

            if sections[0] != '':  #if section not empty add as raw text
                new_list.append(TextNode(sections[0], TextType.TEXT))
            
            new_list.append(TextNode(link[0], TextType.LINK, link[1])) #add links to list
            current_text = sections[1] #update current level
        
        if current_text != '': #if text left, then append as raw text
            new_list.append(TextNode(current_text, TextType.TEXT))

    return new_list