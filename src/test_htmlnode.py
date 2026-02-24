import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "p", "test", "childrens", {"data": "test", "data-active": "true"}
        )
        self.assertEqual(node.props_to_html(), ' data="test" data-active="true"')


if __name__ == "__main__":
    unittest.main()
