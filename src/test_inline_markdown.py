import unittest

from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextType, TextNode


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code_split(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])

    def test_bold_split(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ])

    def test_delimitter_first(self):
        node = TextNode("**This is text** with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is text", TextType.BOLD),
            TextNode(" with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ])
    
    def test_uneven_delimitter(self):
        node = TextNode("**This is text** with a **bold block word", TextType.TEXT)
        with self.assertRaises(Exception):
            new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_inline_delimitter(self):
        node = TextNode("**This is a node _with an inner delimiter_**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("**This is a node ", TextType.TEXT),
            TextNode("with an inner delimiter", TextType.ITALIC),
            TextNode("**", TextType.TEXT),
        ])

    def test_italic_split(self):
        node = TextNode("This is text with _italic text_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC),
        ])
    
    def test_embedded(self):
        node = TextNode("This**messed**up", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This", TextType.TEXT),
            TextNode("messed", TextType.BOLD),
            TextNode("up", TextType.TEXT),
        ])

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://www.boot.dev/lessons/ab12db79-fc4e-46f1-81d2-4694e7f3b8f6)"
        )
        self.assertListEqual([("link", "https://www.boot.dev/lessons/ab12db79-fc4e-46f1-81d2-4694e7f3b8f6")], matches)
    
    def test_boots(self):
        matches = extract_markdown_links(
            "[this link](https://example.com) and [another](https://test.com)"
        )
        self.assertListEqual([("this link", "https://example.com"), ("another", "https://test.com")], matches)

    def test_extraction_without_url(self):
        matches = extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link]"
        )
        self.assertListEqual([], matches)

    def test_image_without_alt(self):
        matches = extract_markdown_images(
            "This is text with an ![](https://i.imgur.com/zjjcJKZ.png) and a [link]"
        )
        self.assertListEqual([("","https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_split_link(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_multiple_consecutive_images(self):
        node = TextNode(
            "![first](https://example.com/1.png)![second](https://example.com/2.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("first", TextType.IMAGE, "https://example.com/1.png"),
                TextNode(
                    "second", TextType.IMAGE, "https://example.com/2.png"
                ),
            ],
            new_nodes,
        )

    
    def test_image_at_beginning(self):
        node = TextNode(
            "![image](https://example.com/pic.png) some text after",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://example.com/pic.png"),
                TextNode(
                    " some text after", TextType.TEXT,
                ),
            ],
            new_nodes,
        )


    def test_exclamation_in_text(self):
        node = TextNode(
            "Wow! This is exciting! ![image](https://example.com/pic.png) Amazing!",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode(
                    "Wow! This is exciting! ", TextType.TEXT,
                ),
                TextNode("image", TextType.IMAGE, "https://example.com/pic.png"),
                TextNode(" Amazing!", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_link_at_beginning(self):
        node = TextNode(
            "[link](https://example.com/pic.png) some text after",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://example.com/pic.png"),
                TextNode(
                    " some text after", TextType.TEXT,
                ),
            ],
            new_nodes,
        )

    def test_multiple_consecutive_links(self):
        node = TextNode(
            "[first](https://example.com/1.png)[second](https://example.com/2.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("first", TextType.LINK, "https://example.com/1.png"),
                TextNode(
                    "second", TextType.LINK, "https://example.com/2.png"
                ),
            ],
            new_nodes,
        )

    def test_text_to_textnodes(self):
        text = 'This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ])


if __name__ == "__main__":
    unittest.main()