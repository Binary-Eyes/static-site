import unittest
from htmlnode import *

class TestLeafNode(unittest.TestCase):
    def test_with_tag(self):
        node = LeafNode("p", "it is the best of days")
        expected = "<p>it is the best of days</p>"
        self.assertEqual(expected, node.to_html())
    
    def test_tag_empty(self):
        text = "node with empty tag"
        node = LeafNode("", text)
        self.assertEqual(text, node.to_html())        
    
    def test_tag_none(self):
        text = "node with tag.none"
        node = LeafNode(None, text)
        self.assertEqual(text, node.to_html())
    
    def test_invalid_node(self):
        create = lambda : LeafNode("a", None)
        self.assertRaises(ValueError, create)