class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag  # Defaults to None, raw text if None
        self.value = value  # Defaults to None, assumed to have children if None
        self.children = children  # Defaults to None, assumed to have a value if None
        self.props = props  # Defaults to None, no attributes if None

    def add_child(self, child):
        if self.children is None:
            self.children = []
        self.children.append(child)

    def to_html(self):
        # Handle attributes
        attrs = ''
        if self.props:
            attrs = ' '.join(f'{key}="{value}"' for key, value in self.props.items())
            attrs = f' {attrs}'

        # Handle children or value
        if self.children is not None:
            children_html = ''.join(
                child.to_html() if isinstance(child, HTMLNode) else str(child)
                for child in self.children
            )
        else:
            children_html = self.value if self.value is not None else ''

        # Render tag or raw text
        if self.tag:
            return f'<{self.tag}{attrs}>{children_html}</{self.tag}>'
        else:
            return children_html

    def props_to_html(self):
        if self.props is None:
            return ""
        return " ".join(f'{key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"


# LeafNode is a subclass of HTMLNode that represents a node with a tag and a value.
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value.")
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value.")
        if self.tag is None:
            return self.value  # Render as raw text if no tag
        attrs = ''
        if self.props:
            attrs = ' '.join(f'{key}="{value}"' for key, value in self.props.items())
            attrs = f' {attrs}'
        return f'<{self.tag}{attrs}>{self.value}</{self.tag}>'

# ParentNode is a subclass of HTMLNode that represents a node with a tag and children.
# It can have multiple children, which can be either LeafNode or ParentNode.
# It can also have attributes (props).
# The children can be a mix of LeafNode and ParentNode.
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("ParentNode must have a tag.")
        if children is None or not isinstance(children, list):
            raise ValueError("ParentNode must have a list of children.")
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag.")
        if self.children is None:
            raise ValueError("ParentNode must have children.")
        
        # Handle attributes
        attrs = ''
        if self.props:
            attrs = ' '.join(f'{key}="{value}"' for key, value in self.props.items())
            attrs = f' {attrs}'

        # Recursively render children
        children_html = ''.join(
            child.to_html() if isinstance(child, HTMLNode) else str(child)
            for child in self.children
        )

        # Render the parent node
        return f'<{self.tag}{attrs}>{children_html}</{self.tag}>'