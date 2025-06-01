import unittest
from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_html_props(self):
        node = HTMLNode("a", "value", None, {"href": "https://www.google.com", "target": "_blank"})
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(expected, node.props_to_html())