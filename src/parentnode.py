from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None or self.children is None:
            raise ValueError

        children = []
        for item in self.children:
            children.append(item.to_html())

        return f"<{self.tag}{self.props_to_html()}>{''.join(children)}</{self.tag}>"
