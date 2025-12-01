import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_getting_empty_props(self):
        node = HTMLNode(props={})
        props = node.props_to_html()
        self.assertEqual(props, "")
    
    def test_getting_none_props(self):
        node = HTMLNode()
        props = node.props_to_html()
        self.assertEqual(props, "")

    def test_getting_simple_props(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }

        node = HTMLNode(props=props)
        expected = ' "href"="https://www.google.com" "target"="_blank"'
        self.assertEqual(node.props_to_html(), expected)