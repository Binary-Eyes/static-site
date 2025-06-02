import unittest
from htmlnode import *

class TestLeafNode(unittest.TestCase):
    def test_with_tag(self):
        node = LeafNode("p", "it is the best of days")
        expected = "<p>it is the best of days</p>"
        self.assertEqual(expected, node.to_html())
    
    def test_tag_empty(self):
        node = LeafNode("", "raw text leaf node")
        self.assertEqual("raw text leaf node", node.to_html())        
    
    def test_tag_none(self):
        node = LeafNode(None, "raw text leaf node")
        self.assertEqual("raw text leaf node", node.to_html())
    
    def test_invalid_node(self):
        create = lambda : LeafNode("a", None)
        self.assertRaises(ValueError, create)