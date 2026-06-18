from copy_static import copy_static
from generate_pages_r import generate_pages_recursive
import sys

def main():
    basepath = sys.argv[1] if len(sys.argv) >=2 else "/"
    copy_static(source="static", destination="docs")
    generate_pages_recursive(dir_path_content="content", template_path="template.html", dest_dir_path="docs",basepath=basepath)

main()