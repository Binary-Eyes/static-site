import unittest

from markdown import *
from textnode import *

class TestMarkdownSplitter(unittest.TestCase):
    def test_simple_text(self):
        root = TextNode("this is a simple text node", TextType.TEXT)
        split = split_nodes_delimiter([root], "", TextType.TEXT)
        self.assertEqual(1, len(split))
        self.assertEqual("this is a simple text node", split[0].text)
