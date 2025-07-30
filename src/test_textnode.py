import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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

class TestTextToHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_italic(self):
        node = TextNode("This is an italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.value, "This is an italic text node")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'code')
        self.assertEqual(html_node.value, "This is a code node")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, "This is a link node")
        self.assertTrue("href" in html_node.props.keys())

    def test_image(self):
        node = TextNode("This is an image node", TextType.IMAGE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value, '')
        self.assertTrue("src" in html_node.props.keys())
        self.assertTrue("alt" in html_node.props.keys())

if __name__ == "__main__":
    unittest.main()