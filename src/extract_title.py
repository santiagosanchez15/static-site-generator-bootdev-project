
def extract_title(markdown: str):
    '''Extracts title form h1 only getting all the text, raises exception if not'''
    markdown = markdown.split('\n')
    for line in markdown:
        if line.startswith('# '):
            return line.lstrip('#').strip()
    
    raise Exception("no h1 header found")

