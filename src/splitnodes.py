from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes_list = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            sub_nodes = node.text.split(delimiter)
            nodes_list.append(TextNode(sub_nodes[0], TextType.TEXT))
            for i in range(1,len(sub_nodes)):
                if i % 2 == 0:
                    nodes_list.append(TextNode(sub_nodes[i], TextType.TEXT))
                else:
                    nodes_list.append(TextNode(sub_nodes[i], text_type))
    return nodes_list
