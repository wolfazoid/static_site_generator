from textnode import TextNode, TextType
from htmlnode import HTMLNode
from inline_markdown import extract_markdown_images, extract_markdown_links

def main():
    node = TextNode('The quick brown fox jumps over the lazy dog', TextType.LINK, 'https://www.feasting.com')
    print(node)

    html = HTMLNode(props={
        "href": "https://www.google.com",
        "target": "_blank",
    })
    print(html.props_to_html())

    text = f'''This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)
    \nThis is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"'''

    print(extract_markdown_images(text))
    print(extract_markdown_links(text))


if __name__ == "__main__":
    main()