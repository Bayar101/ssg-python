import re
from enum import Enum

from htmlnode import HTMLNode
from inline_markdown import text_to_textnodes
from parentnode import ParentNode
from textnode import TextNode, TextType, text_node_to_html_node


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    list = []

    for block in markdown.split("\n\n"):
        item = block.strip()
        if len(item) > 0:
            list.append(item)

    return list


def block_to_block_type(block):
    # Heading: 1–6 # followed by space and text
    if re.fullmatch(r"#{1,6}\s+.+", block):
        return BlockType.HEADING

    # Code block: ```\n ... \n```
    if re.fullmatch(r"```\n[\s\S]*?\n```", block):
        return BlockType.CODE

    lines = block.split("\n")

    # Quote block: every line starts with >
    if all(re.fullmatch(r">\s?.+", line) for line in lines):
        return BlockType.QUOTE

    # Unordered list: every line starts with "- "
    if all(re.fullmatch(r"-\s.+", line) for line in lines):
        return BlockType.UNORDERED_LIST

    # Ordered list: must start at 1 and increment by 1
    ordered_match = True
    for index, line in enumerate(lines, start=1):
        if not re.fullmatch(rf"{index}\.\s.+", line):
            ordered_match = False
            break

    if ordered_match:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


def block_type_to_tag(type):
    if type is BlockType.HEADING:
        return "h"
    if type is BlockType.CODE:
        return "code"
    if type is BlockType.QUOTE:
        return "q"
    if type is BlockType.UNORDERED_LIST:
        return "li"
    if type is BlockType.ORDERED_LIST:
        return "ol"

    return "p"


def text_to_children(text):
    list = text_to_textnodes(text)

    return list


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []

    for block in blocks:
        type = block_to_block_type(block)
        tag = block_type_to_tag(type)

        if type == BlockType.CODE:
            node = text_node_to_html_node(block)
            nodes.append(node)
            continue

        children = text_to_children(block)
        node = HTMLNode(tag, None, children)
        nodes.append(node)

    parent_node = ParentNode("div", nodes)

    return parent_node
