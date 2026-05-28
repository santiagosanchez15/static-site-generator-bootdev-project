
class HTMLNODE:

    def __init__(self, tag: str|None = None, value: str|None = None, children: list["HTMLNODE"]| None = None, props: dict[str:str]|None = None):
        '''Constructor for thr HTMLNODES, raise to None if no value given,
        constrains:
        
        -If no tag -> raw text
        -If no value -> assume there are children 
        -If no children -> assume there is value 
        -If no props -> no attributes
        '''
        self.tag = tag
        self.value = value
        self.children = children 
        self.props = props

    def add_html(self):

        raise NotImplementedError # child classes will override this method
    
    def props_to_html(self):

        if self.props is None: return ""

        props_str = " ".join(f'''{key}="{value}"''' for key, value in self.props.items())

        return props_str

    def __repr__(self):

        return f"tag=({self.tag}), value=({self.value}), children=({self.children}), props=({self.props})"
    
    def __eq__(self, other):

        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props
            


class LeafNode(HTMLNODE):

    def __init__(self, tag: str|None, value: str, props: dict[str:str]|None = None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        '''returns markup to html depending on tag based on infromation provided'''

        #handle edge cases 
        if not self.value: raise ValueError #all leafs should have a value
        if not self.tag: return self.value  #returns raw text

        if self.tag == 'a':
            return f'''<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>'''

        else: 
            return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self):

        return f"tag=({self.tag}), value=({self.value}), props=({self.props})"
    
    def __eq__(self, other):

        return self.tag == other.tag and self.value == other.value and self.props == other.props

