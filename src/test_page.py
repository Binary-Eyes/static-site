import unittest
from page import *

class TestTitleExtraction(unittest.TestCase):
    def test_simple_markdown(self):
        markdown = "# Header"
        pass


    def test_no_header(self):
        markdown = """
This is some markdown
without any headers

- point
- point
"""
        self.assertRaises(Exception, extract_title, markdown)