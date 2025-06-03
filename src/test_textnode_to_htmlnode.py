import unittest
from textnode import *
from htmlnode import *

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_plain_text_conversion(self):
        text_node = TextNode("simple text node", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertIsNone(html_node.tag)
        self.assertEqual("simple text node", html_node.value)