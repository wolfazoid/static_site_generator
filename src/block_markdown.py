from htmlnode import HTMLNode

def markdown_to_blocks(markdown):
    
    blocks = markdown.split('\n\n')
    blocks_list = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        blocks_list.append(block)

    return blocks_list