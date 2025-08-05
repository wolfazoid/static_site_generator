import unittest
import os

from generate_pages import extract_title, generate_page

class TestGeneratePages(unittest.TestCase):
    def test_generate_page(self):
        self.assertTrue(
            os.path.exists('./public/Tolkien Fan Club.html')
        )

    def test_extract_title(self):
        md = """
# Here's a title

And some other text to go along with it."""
        title = extract_title(md)
        self.assertEqual(
            "Here's a title",
            title
            )
        
    def test_multiple_h1(self):
        md = """
# Here's a title

# And some other text to go along with it."""
        title = extract_title(md)
        self.assertEqual(
            "Here's a title",
            title
            )
        
    def test_ignore_lead(self):
        md = """
## Here's an early h2

# a late h1"""
        title = extract_title(md)
        self.assertEqual(
            "a late h1",
            title
            )
        
    def test_no_header(self):
        md = """
Here's a title

And some other text to go along with it."""
        with self.assertRaises(Exception):
            title = extract_title(md)
    

if __name__ == "__main__":
    unittest.main()