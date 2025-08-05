import os
from shutil import copy, rmtree

def copy_directories(source='static', destination='public'):
    if not os.path.exists(source):
        raise Exception('Source path does not exist, cannot copy files')
    if not os.path.exists(destination):
        os.mkdir(destination)

    source_files = os.listdir(source)

    for fpath in source_files:
        src_path = os.path.join(source, fpath)
        dst_path = os.path.join(destination, fpath)
        print(f'file path log\nsrc_path: {src_path}\ndst_path: {dst_path}')
        if os.path.isfile(src_path):
            copy(src_path, dst_path)
        if os.path.isdir(src_path):
            copy_directories(src_path, dst_path)
