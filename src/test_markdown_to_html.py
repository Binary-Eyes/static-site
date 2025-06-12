import unittest
from markdown import *
from htmlnode import *

class TestMarkdownToHtml(unittest.TestCase):
    def test_multiple_line_paragraph(self):
        markdown = """
this is the first line
this is the second line
"""
        html_node = markdown_to_html_node(markdown)
        html = html_node.to_html()
        expected = "<div><p>this is the first line\nthis is the second line</p></div>"
        self.assertEqual(expected, html)
        
    
    def test_single_line_paragraph(self):
        markdown = """
this is the first test
"""
        html_node = markdown_to_html_node(markdown)
        html = html_node.to_html()
        expected = "<div><p>this is the first test</p></div>"
        self.assertEqual(expected, html)