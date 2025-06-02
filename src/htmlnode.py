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
        if self.tag is None or self.tag == "":
            return self.value
        
        start_tag, end_tag = create_tag_pair(self)
        return f"{start_tag}{self.value}{end_tag}"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None or self.tag == "":
            raise ValueError("parent node is missing a tag")
        
        if self.children == None or len(self.children) == 0:
            raise ValueError("parent node is missing its children")
        
        start_tag, end_tag = create_tag_pair(self)
        html = "".join(map(lambda x : x.to_html(), self.children))
        return f"{start_tag}{html}{end_tag}"        


def create_tag_pair(node):
    if node.tag is None or node.tag == "":
        raise Exception("failed to generate tag pair: html node missing tag property")
    
    start_tag = f"<{node.tag}>"
    if node.props is not None and len(node.props) > 0:
        start_tag = f"<{node.tag}{node.props_to_html()}>"

    end_tag = f"</{node.tag}>"
    return start_tag, end_tag
