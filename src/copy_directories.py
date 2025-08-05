import os
from shutil import copy, rmtree

def copy_directories(source, destination):
    if not os.path.exists(source):
        raise Exception('Source path does not exist, cannot copy files')
    if not destination:
        raise Exception("Destination not given, can't copy file contents")
    if not os.path.exists(destination):
        os.mkdir(destination)

    for fpath in os.listdir(source):
        src_path = os.path.join(source, fpath)
        dst_path = os.path.join(destination, fpath)
        print(f'file path log\nsrc_path: {src_path}\ndst_path: {dst_path}')
        if os.path.isfile(src_path):
            copy(src_path, dst_path)
        else:
            copy_directories(src_path, dst_path)
