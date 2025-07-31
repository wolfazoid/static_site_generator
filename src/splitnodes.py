from textnode import TextType, TextNode

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
            for i, sub in enumerate(sub_nodes):
                print(f'\ni: {i}\nsub: {sub}')
            if node.text.find(delimiter) != 0:
                nodes_list.append(TextNode(sub_nodes[0], TextType.TEXT))
            if sub_nodes[-1] == '':
                sub_nodes.pop(-1)
            for i in range(1, len(sub_nodes)):
                if i % 2 == 0:
                    nodes_list.append(TextNode(sub_nodes[i], TextType.TEXT))
                else:
                    nodes_list.append(TextNode(sub_nodes[i], text_type))


    return nodes_list
