import unittest
from textnode import *

class TestTextNode(unittest.TestCase):
    def test_equal(self):
        node1 = TextNode("bold node", TextType.BOLD)
        node2  = TextNode("bold node", TextType.BOLD)
        self.assertEqual(node1, node2)
    
    def test_different_text(self):
        node1 = TextNode("bold node 1", TextType.BOLD)
        node2 = TextNode("bold node 2", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_different_type(self):
        node1 = TextNode("text node", TextType.TEXT)
        node2 = TextNode("text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_with_url(self):
        node1 = TextNode("image node", TextType.IMAGE, "//image.png")
        node2 = TextNode("image node", TextType.IMAGE, "//image.png")
        self.assertEqual(node1, node2)

    def test_with_none_url(self):
        node1 = TextNode("url node", TextType.LINK, "www.link.com")
        node2 = TextNode("url node", TextType.LINK, None)
        self.assertNotEqual(node1, node2)