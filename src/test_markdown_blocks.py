import unittest
from markdown import *

class TestBlockType(unittest.TestCase):
    def test_code_block(self):
        text = "```this is a code block```"
        type = block_to_block_type(text)
        self.assertEqual(MarkdownBlockType.CODE, type)
        
    
    def test_heading(self):
        text = "## This is a heading!"
        type = block_to_block_type(text)
        self.assertEqual(MarkdownBlockType.HEADING, type)


class TestMarkdownBlocks(unittest.TestCase):
    def test_simple_markdown_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(3, len(blocks))
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )