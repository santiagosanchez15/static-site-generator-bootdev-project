from enum import Enum


class BlockType(Enum):

    paragraph= "p"
    heading= "h"
    code = "code" #need to be surrounded with <pre>
    quote= "blockquote"
    unordered_list= "ul" #need to be surrounded with <li>
    ordered_list= "ol" #need to be surrounded with <li>

def block_to_block_type(text:str)-> BlockType:
    '''
    takes SINGLE blockmarkdown as input and returns the BlockType
    input: raw stirng 
    output: Block type that the text is 
    structure of text is determined by the fucntion markdown to blocks
    '''

    if text[0] == '#': # check for heading case
        count = 0
        for i in range(len(text)): #loop through text index
            if count > 6: #edge case more than allowed # return paragraph
                return BlockType.paragraph
            if text[i] == "#":  #found # add one to the count
                count += 1

            elif text[i] == " " and count < 7: # edge case were word is " " and the count is less or equal to 6
                return BlockType.heading
            
            else: #i referece to some other character
                return BlockType.paragraph
        return BlockType.paragraph #loop broken no space found
            
            
    elif len(text) >=4 and text[:4] == "```\n" and text[-3:] == "```": # check for code block by also checking size of text for edge case
        return BlockType.code
    
    elif text[0] == ">": # check for quote initial character is grateer than > 
        split_blocks = text.split("\n") # split newliners to check that initial value is the quote
        for value in split_blocks: # check every value in block
            if value[0] == ">":
                continue
            else: 
                return BlockType.paragraph
        return BlockType.quote
    
    elif text[:2] == "- ": #check of unorrdered list
        split_block = text.split("\n") #split text by newliners and check initial character for every block
        for block in split_block:
            if block[:2] == "- ":
                continue
            else:
                return BlockType.paragraph
        return BlockType.unordered_list
    
    elif text[:3] == "1. ": #check ordered list
        split_block = text.split("\n") #split by newliners

        for i, block in enumerate(split_block, start=1): #give enumerate initial value of 1

            if block.startswith(f"{i}. "): #check that the sequence starts and follows enumerate order
                continue
                
            else: 
                return BlockType.paragraph #didnt match order then its paragraph
        return BlockType.ordered_list
    
    else:
        return BlockType.paragraph