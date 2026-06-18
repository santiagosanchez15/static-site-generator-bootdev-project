import os
from generate_page import generate_page
from pathlib import Path
def generate_pages_recursive(dir_path_content:str, template_path:str, dest_dir_path:str, basepath:str) -> None:
    '''generate pages recursive by given a path and writing everything to the destination path from the template file'''

    if not os.path.exists(dir_path_content): raise ValueError("Not existant source, maybe typo")
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    
    list_entries = os.listdir(dir_path_content) # get list entries in the directory

    for entry in list_entries:

        path = os.path.join(dir_path_content, entry) # get the path of the entry
        dest_final_path = os.path.join(dest_dir_path, entry) #get path of new entry
        
        if os.path.isfile(path): #if file then copy everythign into the dest_dir from template
            dest_final_path = str(Path(dest_final_path).with_suffix(".html"))
            generate_page(from_path=path, template_path=template_path, dest_path=dest_final_path, basepath=basepath) #generates page on given destination
        else:
            generate_pages_recursive(dir_path_content=path, template_path=template_path, dest_dir_path=dest_final_path, basepath=basepath)
            