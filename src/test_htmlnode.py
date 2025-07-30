import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Visit my website", 
                        props={"href": "https://github.com/wolfazoid", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://github.com/wolfazoid" target="_blank">Visit my website</a>')

    def test_leaf_value_required(self):
        with self.assertRaises(TypeError):
            node = LeafNode('p')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        grandchild_node1 = LeafNode("b", "grandchild1")
        child_node1 = ParentNode("span", [grandchild_node1])
        grandchild_node2 = LeafNode("i", "grandchild2")
        child_node2 = ParentNode("a", [grandchild_node2])
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild1</b></span><a><i>grandchild2</i></a></div>",
        )
    
    def test_to_html_with_children_props(self):
        child_node = LeafNode("a", "child link", props={"href": "https://github.com/wolfazoid", "target": "_blank"})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), '<div><a href="https://github.com/wolfazoid" target="_blank">child link</a></div>')

    def test_to_html_with_grandchildren_props(self):
        grandchild_node = LeafNode("a", "grandchild link", props={"href": "https://github.com/wolfazoid", "target": "_blank"})
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span><a href="https://github.com/wolfazoid" target="_blank">grandchild link</a></span></div>',
        )

    def test_to_html_with_leafs(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_parent_no_child_error(self):
        node = ParentNode("b", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_no_tag_error(self):
        child_node = LeafNode("span", "child")
        node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()