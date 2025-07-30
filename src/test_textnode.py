import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a different text node", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_has_url(self):
        node = TextNode("Another text node", TextType.LINK, "https://publicrec.com")
        self.assertTrue(node.url is not None)

    def test_no_url(self):
        node = TextNode("This is a text node", TextType.LINK)
        self.assertTrue(node.url is None)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://publicrec.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://publicrec.com")
        self.assertEqual(node, node2)

    def test_is_text_type(self):
        node = TextNode("This is an italic text node", TextType.IMAGE, "https://www.feasting.com")
        allowed_types = [
            "text",
            "bold",
            "italic",
            "code",
            "link",
            "image"
        ]
        self.assertTrue(node.text_type.value in allowed_types)
    
    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

if __name__ == "__main__":
    unittest.main()