class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""

        items = map(lambda x : f'{x[0]}="{x[1]}"', self.props.items())
        return " " + " ".join(list(items))

    def __repr__(self):
        return f"{self.tag}\n{self.value}\n{self.props}\n{self.children}"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)
        if value is None:
            raise ValueError("leaf node must have a value")
        
    def to_html(self):
        if self.tag is None or "":
            return self.value