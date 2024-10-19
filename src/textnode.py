from enum import Enum

class NodeType(Enum):
    HTML = "html"
    LEAF = "leaf"
    TEXT = "text"

class TextNode:
    def __init__(self, text, text_type, value, url = None):
        self.text = text  # The text content of the node
        self.text_type = text_type
        self.url = url  # The URL of the link or image, defaults to None if not provided
    def __eq__(self, other):
        # Check if 'other' is an instance of TextNode
        if not isinstance(other, TextNode):
            return False
        
        # Compare all properties
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"