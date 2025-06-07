import unittest
from markdown import *

class TestExtractions(unittest.TestCase):
    def test_image(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        images = extract_markdown_images(text)
        self.assertEqual(1, len(images))
        self.assertEqual("image", images[0][0])
        self.assertEqual("https://i.imgur.com/zjjcJKZ.png", images[0][1])

    
    def test_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        links = extract_markdown_links(text)
        self.assertEqual(2, len(links))
        self.assertEqual("to boot dev", links[0][0])