from textnode import TextNode, TextType
from htmlnode import HTMLNode
from inline_markdown import extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link
import os
from shutil import copy, rmtree

def copy_directories(source='static', destination='public'):
    if not os.path.exists(source):
        raise Exception('Source path does not exist, cannot copy files')
    if not os.path.exists(destination):
        print(f'Destination directory does not exist, creating new directory named "{destination}"')
        os.mkdir(destination)

    # Clean up destination directory
    if len(os.listdir(destination)) > 0:
        for fpath in os.listdir(destination):
            full_path = f'{destination}/{fpath}'
            if os.path.isfile(full_path):
                os.remove(full_path)
            elif os.path.isdir(full_path):
                rmtree(full_path)
    
    source_files = os.listdir(source)

    for fpath in source_files:
        src_path = os.path.join(source,fpath)
        dst_path = f'{destination}/{fpath}'
        print(f'file path log\nsrc_path: {src_path}\ndst_path: {dst_path}')
        if os.path.isfile(src_path):
            copy(src_path, dst_path)
        if os.path.isdir(src_path):
            next_src = os.path.join(src_path)
            copy_directories(src_path, dst_path)
    # Copy all files, subdirectories, nested files from source dir
        # Base Case:
        # Found a file, copy it
        # If is directory, 
        #   get all files and folders in directory
        #   extend the path to any sub folders
        #   check any subfolders for files
        # 
    # paste into destination director
    pass

def main():
    copy_directories(source='not_a_place',destination='a_new_dest')

if __name__ == "__main__":
    main()