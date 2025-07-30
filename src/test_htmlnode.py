import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode(
            tag='p', 
            value='This is a paragraph')
        self.assertEqual(
            "HTMLNode(p, This is a paragraph, children: None, None)", repr(node)
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr2(self):
        node = HTMLNode(
            tag='a', 
            value='This is a link', 
            children=[HTMLNode(tag='p', value='This is a paragraph')], 
            props={"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(
            "HTMLNode(a, This is a link, children: [HTMLNode(p, This is a paragraph, children: None, None)], {'href': 'https://www.google.com', 'target': '_blank'})", repr(node)
        )

    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        html = f' href="https://www.google.com" target="_blank"'
        node = HTMLNode(props=props)
        self.assertEqual(node.props_to_html(), html)

    def test_empty_props(self):
        node = HTMLNode()
        html = ""
        self.assertEqual(node.props_to_html(), html)

    def test_to_html_error(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()