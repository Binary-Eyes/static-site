import unittest
from page import *

class TestTitleExtraction(unittest.TestCase):
    def test_with_header(self):
        markdown = """
# TEST LIST

This is the test list for our tests

- Test first thing
- Test second thing
"""
        expected = "TEST LIST"
        self.assertEqual(expected, extract_title(markdown))
        
    
    def test_without_header(self):
        markdown = """
## no header

# fake header

Another one bytes the dust
"""
        self.assertRaises(Exception, extract_title, markdown)

    
    def test_simple_markdown(self):
        markdown = "# Header"
        expected = "Header"
        self.assertEqual(expected, extract_title(markdown))


    def test_no_header(self):
        markdown = """
This is some markdown
without any headers

- point
- point
"""
        self.assertRaises(Exception, extract_title, markdown)