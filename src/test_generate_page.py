import unittest

from generate_page import extract_title, generate_page, get_file_content


class TestFunc(unittest.TestCase):
    def test_generate_page(self):
        page = generate_page("content/index.md", "template.html", "public/index.html")

        print(page)

    def test_extract(self):
        from_content = get_file_content("content/index.md")
        val = extract_title(from_content)
        print(val)
