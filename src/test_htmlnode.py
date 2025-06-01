import unittest
from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_html_props(self):
        node = HTMLNode("a", "value", None, {"href": "https://www.google.com", "target": "_blank"})
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(expected, node.props_to_html())

    def test_without_value(self):
        node = HTMLNode("a", None, [HTMLNode(None, "simple text")], None)
        self.assertEqual(len(node.children), 1)

    def test_without_props(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")