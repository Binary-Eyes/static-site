import unittest
from htmlnode import *

class TestParentNode(unittest.TestCase):
    def test_with_no_children(self):
        node = ParentNode("p", [])
        self.assertRaises(ValueError, node.to_html)