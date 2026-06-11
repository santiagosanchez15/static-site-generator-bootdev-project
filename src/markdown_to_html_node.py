"""
pseudocode:

- first split the text into different blocks, you can do that with the markdown to blocks function 
- second: loop through each block and get the block type, depending on block type handle initial tag
- third: need to get the inside tags, therefore, need one that takes text and i get list of leafnodes, you can do that by using text_to_textnodes
"""
#MAIN FUNCTION
from block_types import block_to_block_type, BlockType # get block type from text
from markdown_to_blocks import markdown_to_blocks #break text form different newliners into a list

#HELPER1 FUNCTION
from text_to_text_nodes import text_to_textnodes #function get correct node for given list of nodes -> list of text nodes

#HELPER2 FUNCTION
from textnode import text_node_to_html_node # -> gets the leaf node
from htmlnode import LeafNode # use to_html will return text to string 
from parentnode import PARENTNODE


def markdown_to_html_node( text:str) -> PARENTNODE:
    '''Takes a markdown text (string) and returns a single HTMLNODE parent full other child'''

    blocks = markdown_to_blocks(text) #returns list of blocks turning the text into blocks
    current_children = [block_to_htmlnode(blocktype=block_to_block_type(block), text=block) for block in blocks]

    return PARENTNODE(tag="div", children= current_children, props= None)


def text_to_children(block:str) -> list[LeafNode]:
    '''Takes a text (block) and returns a list of LeafNode which will become children of HTMLNODE'''
    leafs_nodes = []
    text_Nodes = text_to_textnodes(block)
    for node in text_Nodes: #loop through each textnode
        current_leaf = text_node_to_html_node(node) #create a leaf
        leafs_nodes.append(current_leaf) #append to the list of children
    
    return leafs_nodes
    

def block_to_htmlnode(blocktype: BlockType, text: str) -> PARENTNODE:
    '''returns htmlnode from given blocktype and text'''

    if blocktype == BlockType.code: #check if blocktype is 
        code_block = LeafNode(tag="code", value=text[4:-3], props=None)
        return PARENTNODE(tag="pre", children=[code_block], props=None)
    
    elif blocktype == BlockType.unordered_list: #create tag for unorganized list
        cleaned_text = [x[2:] for x in text.split("\n")]
        list_lists = [PARENTNODE(tag='li', children=text_to_children(filtered)) for filtered in cleaned_text]
        return PARENTNODE(tag="ul", children=list_lists)

    elif blocktype == BlockType.ordered_list: #check ordered list
        cleaned_lists = []
        for i, block in enumerate(text.split("\n"), start=1):
            cleaned_block = block.replace(f"{i}. ", "")
            cleaned_lists.append(PARENTNODE(tag="li", children=text_to_children(cleaned_block)))
        return PARENTNODE(tag="ol", children=cleaned_lists)
    
    elif blocktype == BlockType.heading: #check heading case
        num_hash = len(text.split(" ")[0])
        current_children = text_to_children(block=text[num_hash + 1:])
        return PARENTNODE(tag=f"h{num_hash}", children=current_children)

    elif blocktype == BlockType.quote: #check quote case
        cleaned_quotes = " ".join([current[1:].strip() for current in text.split("\n")])
        current_children = text_to_children(block=cleaned_quotes) 
        return PARENTNODE(tag="blockquote", children=current_children )

    else: #check qparagraphuote case
        cleaned_paragraph = " ".join(text.split("\n"))
        current_children = text_to_children(block=cleaned_paragraph) #get list of children from current text 
        return PARENTNODE(tag="p", children=current_children )


