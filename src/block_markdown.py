from enum import Enum
from htmlnode import HTMLNode

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    block = block.strip()
    lines = block.split('\n')
    if block.startswith(('# ', '## ', '### ', '#### ', '##### ', '###### ')):
        return BlockType.HEADING
    if block.startswith('```') and block.endswith('```'):
        return BlockType.CODE
    if block.startswith('>'):
        for line in lines:
            if not line.startswith('>'):
                break
        return BlockType.QUOTE
    if block.startswith('- '):
        for line in lines:
            if not line.startswith('- '):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith('1. '):
        line_count = 1
        for line in lines:
            if not line.startswith(f'{line_count}. '):
                return BlockType.PARAGRAPH
            line_count += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    
    blocks = markdown.split('\n\n')
    blocks_list = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        blocks_list.append(block)

    return blocks_list

def markdown_to_html_node(markdown):
    blocks_list = markdown_to_blocks(markdown)
    for block in blocks_list:
        block_type = block_to_block_type(block)

def block_type_to_tag(block_type):
    # Set tag based on block type
    pass

def link_to_props(block):
    # Convert link to props dictionary
    # Return HTMLNode with props and tag
    pass

def image_to_props(block):
    # convert image to props dictionary
    # Return HTMLNode with props and tag
    pass

def block_to_html_node(block, block_type):
    # Identify block type
    # send appropriate tag to HTML Node based on block type
    pass