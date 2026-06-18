
def extract_title(markdown: str):
    markdown = markdown.split('\n')
    for line in markdown:
        if line.startswith('# '):
            return line.lstrip('#').strip()
    
    raise Exception("no h1 header found")

