from textnode import TextNode, TextType
from htmlnode import HTMLNode, ParentNode, LeafNode

def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise Exception("Invalid Text Type")


    if text_node.text_type.value == 'text':
        return LeafNode(
            tag=None, 
            value=text_node.text
            )
    elif text_node.text_type.value == 'bold':
        return LeafNode(
            tag='b', 
            value=text_node.text
            )
    elif text_node.text_type.value == 'italic':
        return LeafNode(
            tag='i', 
            value=text_node.text
            )
    elif text_node.text_type.value == 'code':
        return LeafNode(
            tag='code', 
            value=text_node.text
            )
    elif text_node.text_type.value == 'link':
        return LeafNode(
            tag='a', 
            value=text_node.text, 
            props={"href": text_node.url}
            )
    elif text_node.text_type.value == 'image':
        return LeafNode(
            tag='img', 
            value="", 
            props={
                "src": text_node.url,
                "alt": text_node.text,
            })
