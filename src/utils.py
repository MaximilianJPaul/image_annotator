import os
import glob
from pprint import pprint

def get_project_root():
    path = os.getcwd()
    return path


def get_project_root_basename():
    path = os.getcwd()
    return os.path.basename(path)


def folder_exists(project_root, target_name):
    search_pattern = os.path.join(project_root, '**', target_name)
    found_dirs = glob.glob(search_pattern, recursive=True)
    return len(found_dirs) > 0


def list_files(project_root, target_name):
    if not folder_exists(project_root, target_name):
        return []
    
    search_pattern = os.path.join(project_root, '**', target_name)
    found_dirs = glob.glob(search_pattern, recursive=True)

    if len(found_dirs) > 1:
        print(f"Found more than one directory with name {target_name}")
        pprint(found_dirs)
        return []
    
    target_dir = found_dirs[0]
    files = []

    for file in os.listdir(target_dir):
        if os.path.isfile(os.path.join(target_dir, file)):
            files.append(file)

    files = sorted(files)
    return files


