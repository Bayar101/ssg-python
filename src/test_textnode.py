import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("this is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("This is a text node", TextType.LINK, "test.com")
        node2 = TextNode("this is a text node", TextType.LINK, "text.com")
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)

        expected = None
        val = html_node.tag
        expected1 = "This is a text node"
        val1 = html_node.value

        self.assertEqual(val, expected)
        self.assertEqual(val1, expected1)

    def test_text_link(self):
        node = TextNode("This is a text node", TextType.LINK, "test.com")
        html_node = text_node_to_html_node(node)

        expected = "a"
        val = html_node.tag
        expected1 = '<a href="test.com">This is a text node</a>'
        val1 = html_node.to_html()

        # print(f"Expected: {expected}")
        # print(f"Val: {val}")
        # print(f"Expected1: {expected1}")
        # print(f"Val1: {val1}")
        self.assertEqual(val, expected)
        self.assertEqual(val1, expected1)

    def test_text_image(self):
        node = TextNode(
            "This is a text node",
            TextType.IMAGE,
            "test.com",
        )
        html_node = text_node_to_html_node(node)

        expected = "img"
        val = html_node.tag
        expected1 = '<img src="test.com" alt="This is a text node"></img>'
        val1 = html_node.to_html()

        # print(f"Expected: {expected}")
        # print(f"Val: {val}")
        # print(f"Expected1: {expected1}")
        # print(f"Val1: {val1}")
        self.assertEqual(val, expected)
        self.assertEqual(val1, expected1)


if __name__ == "__main__":
    unittest.main()
