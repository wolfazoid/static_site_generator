import os
from shutil import rmtree
import sys

from copy_directories import copy_directories
from generate_pages import generate_pages_recursive
# from textnode import TextNode, TextType
# from htmlnode import HTMLNode
# from inline_markdown import extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link

dir_path_static = './static'
dir_path_public = './public'
dir_path_content = './content'
template_path = './template.html'

def main():
    print("Cleaning out destination")
    if os.path.exists(dir_path_public):
        rmtree(dir_path_public)

    print("Copying source files to destination directory")
    copy_directories(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_pages_recursive(
        dir_path_content,
        template_path,
        dir_path_public
    )

if __name__ == "__main__":
    main()