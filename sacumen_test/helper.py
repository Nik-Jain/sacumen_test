import os

def get_file_paths(data_root_directry):
    files_paths = []
    for root, _, files in os.walk(data_root_directry):
        for file in files:
            files_paths.append(os.path.join(root, file))
    return files_paths

def get_file_extension(file_path):
    return file_path.split("\\")[-1].split('.')[-1].lower()

