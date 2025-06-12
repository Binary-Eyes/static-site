import unittest
from markdown import *
from htmlnode import *

class TestMarkdownToHtml(unittest.TestCase):
    def test_with_ordered_list(self):
        markdown = """
### Another List

1. Item1
2. Item2
"""
        html_node = markdown_to_html_node(markdown)
        html = html_node.to_html()
        expected = "<div><h3>Another List</h3><ol><li>Item1</li><li>Item2</li></ol></div>"
        self.assertEqual(expected, html)


    def test_with_unordered_list(self):
        markdown = """
## Todo

- build site
- run project
- profit!
"""
        html_node = markdown_to_html_node(markdown)
        html = html_node.to_html()
        expected = "<div><h2>Todo</h2><ul><li>build site</li><li>run project</li><li>profit!</li></ul></div>"
        self.assertEqual(expected, html)

    
    def test_with_single_header_1(self):
        markdown = """
# Static Site Generator
"""
        html_node = markdown_to_html_node(markdown)
        html = html_node.to_html()
        expected = "<div><h1>Static Site Generator</h1></div>"
        self.assertEqual(expected, html)


    def test_paragraphs(self):
        markdown = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        expected = "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"
        self.assertEqual(expected, html)


    def test_multiple_paragraphs(self):
        markdown = """
it was the best of times

it was the worst of times
"""
        html_node = markdown_to_html_node(markdown)
        html = html_node.to_html()
        expected = "<div><p>it was the best of times</p><p>it was the worst of times</p></div>"
        self.assertEqual(expected, html)

    
    def test_multiple_line_paragraph(self):
        markdown = """
this is the first line
this is the second line
"""
        html_node = markdown_to_html_node(markdown)
        html = html_node.to_html()
        expected = "<div><p>this is the first line this is the second line</p></div>"
        self.assertEqual(expected, html)

    
    def test_single_line_paragraph(self):
        markdown = """
this is the first test
"""
        html_node = markdown_to_html_node(markdown)
        html = html_node.to_html()
        expected = "<div><p>this is the first test</p></div>"
        self.assertEqual(expected, html)


if __name__ == "__main__":
    unittest.main()