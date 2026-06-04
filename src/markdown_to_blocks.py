
def markdown_to_blocks(text:str) -> list[str]:
    '''Takes a text and returns a list of strings called in this case a block of strings'''

    block = [part.strip() for part in text.split('\n\n') if part.strip() != ''] # remember to filter for stragglers that strip my leave
    return block

md = """
hello






"""
