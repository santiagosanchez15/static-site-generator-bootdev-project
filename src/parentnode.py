from htmlnode import HTMLNODE

class PARENTNODE(HTMLNODE):

    def __init__(self, tag: str, children:list, props: dict|None=None ):
        super().__init__(tag=tag, children=children, props=props)

    
    def to_html(self) -> str:

        if not self.tag: raise ValueError("Missing required tag")
        if not self.children: raise ValueError("Missing children, list empty")

        string_html = f"<{self.tag}>"

        for children in self.children:

            string_html = string_html + children.to_html()

        return string_html + f"</{self.tag}>"
