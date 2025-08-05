from textnode import TextNode, TextType
from htmlnode import HTMLNode
from inline_markdown import extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link
import os
from shutil import copy, rmtree

def copy_directories(source='static', destination='public'):
    if not os.path.exists(source):
        raise Exception('Source path does not exist, cannot copy files')
    if os.path.exists(destination):
        rmtree(destination)

    for fpath in source_files:
        src_path = os.path.join(source,fpath)
        dst_path = f'{destination}/{fpath}'
        print(f'file path log\nsrc_path: {src_path}\ndst_path: {dst_path}')
        if os.path.isfile(src_path):
            copy(src_path, dst_path)
        if os.path.isdir(src_path):
            next_src = os.path.join(src_path)
            copy_directories(src_path, dst_path)

def main():
    copy_directories(source='static',destination='public')

if __name__ == "__main__":
    main()