from enum import Enum

from leafnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type=TextType.TEXT, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
    type = text_node.text_type
    text = text_node.text
    url = text_node.url

    if type is TextType.TEXT:
        return LeafNode(None, text)
    elif type is TextType.BOLD:
        return LeafNode("b", text)
    elif type is TextType.ITALIC:
        return LeafNode("i", text)
    elif type is TextType.CODE:
        return LeafNode("code", text)
    elif type is TextType.LINK:
        return LeafNode("a", text, {"href": url})
    elif type is TextType.IMAGE:
        return LeafNode("img", "", {"src": url, "alt": text})

    raise Exception("Not supported type")
