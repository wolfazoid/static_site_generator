import os
from shutil import rmtree

from copy_directories import copy_directories
# from textnode import TextNode, TextType
# from htmlnode import HTMLNode
# from inline_markdown import extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link

source = './static'
destination = './public'

def main():
    print("Cleaning out destination")
    if os.path.exists(destination):
        rmtree(destination)
    copy_directories(source, destination)

if __name__ == "__main__":
    main()