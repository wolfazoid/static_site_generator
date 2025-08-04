import unittest

from block_markdown import markdown_to_blocks, block_to_block_type, BlockType

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    
    def test_empty_line(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line


- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    
    def test_tabbing(self):
        md = """
    This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line


- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_empty_md(self):
        md = """"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [],
        )

    
    def test_no_double_linebreak(self):
        md = """
This is **bolded** paragraph
This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line
- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph\nThis is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line\n- This is a list\n- with items",
            ],
        )


    def test_block_to_paragraph(self):
        block = """
This is **bolded** paragraph
"""
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type,
            BlockType.PARAGRAPH,
        )

    def test_block_to_quote(self):
        block = """> This is **bolded** quote
> This is more quote text 
"""
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type,
            BlockType.QUOTE,
        )

    def test_block_to_code(self):
        block = """
```> This is **bolded** code
> This is more code 
and a random line to test
```
"""
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type,
            BlockType.CODE,
        )

    def test_block_to_ul(self):
        block = """
- ```> This is **bolded** code
- > This is more code 
- and a random line to test
"""
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type,
            BlockType.UNORDERED_LIST,
        )

    def test_block_to_ol(self):
        block = """
1. > This is **bolded** code
2. > This is more code 
3. and a random line to test
"""
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type,
            BlockType.ORDERED_LIST,
        )

    def test_block_bad_ol(self):
        block = """
1. > This is **bolded** code
2. > This is more code 
5. and a random line to test
"""
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type,
            BlockType.PARAGRAPH,
        )

    def test_block_bad_ul(self):
        block = """
- This is **bolded** code
This is more code 
- and a random line to test
"""
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type,
            BlockType.PARAGRAPH,
        )

    def test_block_to_heading(self):
        block = """# This is a heading"""
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type,
            BlockType.HEADING,
        )

    def test_block_to_h2(self):
        block = """## This is an h2"""
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type,
            BlockType.HEADING,
        )

    def test_block_to_h7(self):
        block = """####### This is not an accepted heading"""
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type,
            BlockType.PARAGRAPH,
        )

if __name__ == "__main__":
    unittest.main()