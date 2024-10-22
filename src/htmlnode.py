class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        if not self.children:
            if self.tag:
                return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
            else:
                return self.value  # Render as raw text if there's no tag

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
            # Call the parent class constructor with no children allowed.
            # Ensure `children` is always set to an empty list and `value` is required.
        super().__init__(tag=tag, value=value, children=[], props=props)
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value.")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
