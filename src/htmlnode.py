class HTMLNode:
    
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        html_string = ""
        for key, value in self.props.items():
            sub_str = f'{key}="{value}"'
            html_string += f' {sub_str}'
        
        return html_string
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})'
    
class LeafNode(HTMLNode):
    
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("Invalid HTML: Leaf node is missing a value")
        if self.tag is None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Invalid HTML: Parent node is missing a tag")
        if not self.children:
            raise ValueError("Invalid HTML: Parent node is missing children")
        child_html = ""
        for child in self.children:
            if child.children is None:
                child_html += child.to_html()
            else:
                for grandchild in child.children:
                    child_html += f'<{child.tag}{child.props_to_html()}>{grandchild.to_html()}</{child.tag}>'
        return f'<{self.tag}{self.props_to_html()}>{child_html}</{self.tag}>'
