from htmlnode import HTMLNODE

class PARENTNODE(HTMLNODE):

    def __init__(self, tag: str, children:list, props: dict|None=None ):
        super().__init__(tag=tag, children=children, props=props)

    
    def to_html(self) -> str:

        if not self.tag: raise ValueError("Missing required tag") #raise value no tag given
        if not self.children: raise ValueError("Missing children, list empty") #raise value no children 

        string_html = f"<{self.tag}>" #builds the tag

        for children in self.children:

            string_html = string_html + children.to_html() #adds children to parent tag

        return string_html + f"</{self.tag}>" #returns parent tag with children plus closure
