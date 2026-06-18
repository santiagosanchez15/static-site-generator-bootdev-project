from copy_static import copy_static
from generate_page import generate_page

def main():
    
    copy_static(source="static", destination="public")
    generate_page(from_path='content/index.md', template_path='template.html', dest_path='public/index.html')
main()