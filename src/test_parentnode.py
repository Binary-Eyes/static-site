import unittest
from htmlnode import *

class TestParentNode(unittest.TestCase):
    def test_with_props(self):
        grandchild_node = LeafNode("b", "grandchild node", {"href": "www.google.com"})
        child_node = ParentNode("span", [grandchild_node])
        root_node = ParentNode("div", [child_node], {"target": "root"})
        expected = '<div target="root"><span><b href="www.google.com">grandchild node</b></span></div>'
        self.assertEqual(expected, root_node.to_html())


    def test_with_grandchild(self):
        grandchild_node = LeafNode("b", "grandchild node")
        child_node = ParentNode("span", [grandchild_node])
        root_node = ParentNode("div", [child_node])
        expected = "<div><span><b>grandchild node</b></span></div>"
        self.assertEqual(expected, root_node.to_html())
    
    def test_with_simple_child(self):
        child_node = LeafNode("span", "child node")
        parent_node = ParentNode("div", [child_node])
        expected = "<div><span>child node</span></div>"
        self.assertEqual(expected, parent_node.to_html())
    
    def test_with_no_children(self):
        node = ParentNode("p", [])
        self.assertRaises(ValueError, node.to_html)