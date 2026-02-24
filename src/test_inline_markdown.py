import unittest

from inline_markdown import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)
from textnode import TextNode, TextType


class TestFunc(unittest.TestCase):
    def test_delimiter(self):
        node = TextNode("This is a text with `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is a text with ", TextType.TEXT, None),
            TextNode("code block", TextType.CODE, None),
            TextNode(" word", TextType.TEXT, None),
        ]

        self.assertEqual(new_nodes, expected)

    def test_extract_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        val = extract_markdown_images(text)

        self.assertEqual(val, expected)

    def test_extract_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev"),
        ]
        val = extract_markdown_links(text)

        self.assertEqual(val, expected)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
        ]

        # print("———————————")
        # print(f"Expected: {expected}")
        # print("———————————")
        # print(f"Actual: {new_nodes}")
        self.assertListEqual(
            expected,
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with an [link desu](https://i.imgur.com/zjjcJKZ.png) and another [second link desu](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("link desu", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second link desu", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
            ),
        ]

        # print("———————————")
        # print(f"Expected: {expected}")
        # print("———————————")
        # print(f"Actual: {new_nodes}")
        self.assertListEqual(
            expected,
            new_nodes,
        )

    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev) **bold text**"
        new_nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode(
                "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
            ),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            TextNode(" ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
        ]

        print("———————————")
        print(f"Expected: {expected}")
        print("———————————")
        print(f"Actual: {new_nodes}")

        self.assertListEqual(expected, new_nodes)


if __name__ == "__main__":
    unittest.main()
