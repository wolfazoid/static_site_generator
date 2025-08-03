from textnode import TextType, TextNode
import re

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
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

def split_nodes_image(old_nodes):
    nodes_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            nodes_list.append(node)
            continue
        
        original_text = node.text
        image_nodes = extract_markdown_images(original_text)
        if len(image_nodes) == 0:
            nodes_list.append(node)
            continue

        for image in image_nodes:
            image_alt = image[0]
            image_link = image[1]
            sections = original_text.split(f'![{image_alt}]({image_link})', 1)

            if len(sections) != 2:
                raise ValueError("Invalid markdown: missing closing delimiter in image markdown")
            if sections[0] != "":
                nodes_list.append(TextNode(sections[0], TextType.TEXT))
                nodes_list.append(TextNode(image_alt, TextType.IMAGE, image_link))
            original_text = sections[1]
        if original_text != "":
            nodes_list.append(TextNode(original_text, TextType.TEXT))

    return nodes_list

# def split_nodes_image(old_nodes):
#     nodes_list = []
#     for node in old_nodes:
#         if node.text.count("[") != node.text.count("]") or node.text.count("(") != node.text.count(")"):
#             raise Exception("Invalid markdown: missing closing delimiter")
        
#         initial_sub_nodes = node.text.split('!')
#         final_sub_nodes = []
#         for part in initial_sub_nodes:
#             sub_node = part.split(')')
#             final_sub_nodes.extend(sub_node)

#         for i in range(len(final_sub_nodes)):
#             if final_sub_nodes[i] == "":
#                 continue
#             if i % 2 == 0:
#                 nodes_list.append(TextNode(final_sub_nodes[i], TextType.TEXT))
#             else:
#                 markdown = '!' + final_sub_nodes[i] + ')'
#                 image_md = extract_markdown_images(markdown)
#                 nodes_list.append(TextNode(image_md[0][0], TextType.IMAGE, image_md[0][1]))

#     return nodes_list


def split_nodes_link(old_nodes):
    nodes_list = []
    for node in old_nodes:
        if node.text.count("[") != node.text.count("]") or node.text.count("(") != node.text.count(")"):
            raise Exception("Invalid markdown: missing closing delimiter")
        
        initial_sub_nodes = node.text.split('[')
        final_sub_nodes = []
        for part in initial_sub_nodes:
            sub_node = part.split(')')
            final_sub_nodes.extend(sub_node)

        for i in range(len(final_sub_nodes)):
            if final_sub_nodes[i] == "":
                continue
            if i % 2 == 0:
                nodes_list.append(TextNode(final_sub_nodes[i], TextType.TEXT))
            else:
                markdown = '[' + final_sub_nodes[i] + ')'
                link_md = extract_markdown_links(markdown)
                nodes_list.append(TextNode(link_md[0][0], TextType.LINK, link_md[0][1]))

    return nodes_list