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
    if block.startswith('#'):
        return BlockType.HEADING
    if block.startswith('```') and block.endswith('```'):
        return BlockType.CODE
    if block.startswith('>'):
        lines = block.split('\n')
        for line in lines:
            if not line.startswith('>'):
                break
        return BlockType.QUOTE
    if block.startswith('- '):
        lines = block.split('\n')
        for line in lines:
            print(f'Line debug: {line}')
            if not line.startswith('- '):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith('1. '):
        lines = block.split('\n')
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