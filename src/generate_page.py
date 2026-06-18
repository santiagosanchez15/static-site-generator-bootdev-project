from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
from os.path import dirname
from os import makedirs

def generate_page(from_path:str, template_path:str, dest_path:str):
    '''generates page from the start path to the destination path and uses the template path'''

    print(f"Generating page from {from_path} to {dest_path} using {template_path}") # print message
    with open(from_path, "r") as f: #read content from path
        markdown_content = f.read() 

    with open(template_path, "r") as template: #read templates content
        template_content = template.read()

    node = markdown_to_html_node(markdown_content) #get the node
    html = node.to_html() #get the html code
    title = extract_title(markdown_content) #get title of page
    template_content = template_content.replace('''{{ Title }}''', f"{title}") #replace title with the one found
    template_content = template_content.replace("""{{ Content }}""", f"{html}") #replace content with the html created

    directory = dirname(dest_path)
    makedirs(name=directory,exist_ok=True) #Creates directory if doesnt exist, if exists, because of exist_ok then no exceptino raise otherwise raised
    with open(dest_path, "w") as dst: #write the new file
        dst.write(template_content)
    
    