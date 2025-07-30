from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    node = TextNode('The quick brown fox jumps over the lazy dog', TextType.LINK, 'https://www.feasting.com')
    print(node)

    html = HTMLNode(props={
        "href": "https://www.google.com",
        "target": "_blank",
    })
    print(html.props_to_html())

if __name__ == "__main__":
    main()