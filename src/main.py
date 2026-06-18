from copy_static import copy_static
from generate_pages_r import generate_pages_recursive

def main():
    
    copy_static(source="static", destination="public")
    generate_pages_recursive(dir_path_content="content", template_path="template.html", dest_dir_path="public")
    
main()