class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        # Initialize tag: if None, this node will be treated as raw text.
        self.tag = tag

        # Initialize value: If not provided, it will be set to None by default.
        self.value = value

        # Initialize children: If no children are provided, initialize to an empty list.
        self.children = children if children is not None else []

        # Initialize props: If no attributes are provided, initialize to an empty dictionary.
        self.props = props if props is not None else {}

class HTMLNode:
    def__init__(self, tag, value, children=None, props=None):
# Initialize the tag name (e.g., "p", "a", "h1")

        if tag is None:
            return self
        self.tag = tag
    
    # Initialize the value of the tag (e.g., text content inside the tag)
        if value is None:
            value = value(children)
        self.value = value

    # Initialize children, which is a list of HTMLNode objects
    # Default to an empty list if not provided
        if children is None:
            children = [value]
        self.children = children

    # Initialize props, which is a dictionary representing HTML tag attributes
    # Default to an empty dictionary if not provided
        if props is None:
            props = {}
        self.props = props