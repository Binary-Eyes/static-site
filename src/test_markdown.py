import unittest

from markdown import *
from textnode import *

class TestMarkdownSplitter(unittest.TestCase):
    def test_text_with_single_code_element(self):
        root = TextNode("the following is a `code snippet` word block", TextType.TEXT)
        split = split_nodes_delimiter([root], "`", TextType.CODE)
        self.assertEqual(3, len(split))
        self.assertEqual("the following is a ", split[0].text)
        self.assertEqual("code snippet", split[1].text)
        self.assertEqual(" word block", split[2].text)
        self.assertEqual(TextType.CODE, split[1].text_type)

    
    def test_simple_text(self):
        root = TextNode("this is a simple text node", TextType.TEXT)
        split = split_nodes_delimiter([root], "", TextType.TEXT)
        self.assertEqual(1, len(split))
        self.assertEqual("this is a simple text node", split[0].text)
