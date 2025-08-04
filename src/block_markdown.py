from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import text_node_to_html_node
from inline_markdown import text_to_textnodes

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_html_node(markdown):
    blocks_list = markdown_to_blocks(markdown)
    parent_node = ParentNode('div', children=None, props=None)
    all_html_nodes = []
    for block in blocks_list:
        block_type = block_to_block_type(block)
        block_text = text_to_textnodes(block)
        if block_type == BlockType.PARAGRAPH:
            children = text_to_children(block)
            html_node = HTMLNode('p',children=children)
            all_html_nodes.append(html_node)
        if block_type == BlockType.HEADING:
            htag, hbody = heading_block_to_html(block)
            html_node = HTMLNode(tag={htag}, value={hbody})
        if block_type == BlockType.QUOTE:
            html_node = HTMLNode(tag='blockquote')
        if block_type == BlockType.CODE:
            pass
        if block_type == BlockType.UNORDERED_LIST:
            children = text_to_children(block)
            html_node = HTMLNode(tag='ul', children=children)
            all_html_nodes.append(html_node)
        if block_type == BlockType.ORDERED_LIST:
            html_node = HTMLNode(tag='ol')
        #based on block_type, create an HTMLNode with tag, children, props
    parent_node.children = all_html_nodes
    return parent_node

def text_to_children(text):
    children = []
    text_nodes = text_to_textnodes(text)
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children


def heading_block_to_html(block):
    heading_count = block.split()[0].count('#')
    if heading_count > 6:
        raise ValueError("Invalid heading, only headings up to h6 are accepted")
    if heading_count == 0:
        raise ValueError("Heading block passed but not heading delimiters found")
    heading_tag = f'h{heading_count}'
    # heading_body = block.split(' ',1)[1]
    return heading_tag #, heading_body


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
