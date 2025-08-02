from textnode import TextType, TextNode
import re

def extract_markdown_images(text):
    matches = re.findall(r"\!\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            nodes_list.append(node)
        elif delimiter not in node.text:
                nodes_list.append(node)
        else:
            if node.text.count(delimiter) % 2 != 0:
                raise Exception("Invalid markdown: missing closing delimiter")
            sub_nodes = node.text.split(delimiter)
            for i in range(len(sub_nodes)):
                if sub_nodes[i] == "":
                    continue
                if i % 2 == 0:
                    nodes_list.append(TextNode(sub_nodes[i], TextType.TEXT))
                else:
                    nodes_list.append(TextNode(sub_nodes[i], text_type))


    return nodes_list