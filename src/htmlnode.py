class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("function is not implemented yet")
    
    def props_to_html(self):
        if self.props is None or len(self.props) == 0:
            return ""
        
        props = []
        for key in self.props:
            props.append(f'"{key}"="{self.props[key]}"')
        
        return " " + " ".join(props)
    
    def __repr__(self):
        pass
    
        