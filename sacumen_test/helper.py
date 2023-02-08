import os

def get_file_paths(data_root_directry):
    """
    This file walk through all fils in provided directory and it's subdirectories and provide path of each file
    
    Args:
        data_root_directry (str): valid directory for which files needs to be uploaded

    Returns:
        list[str]: returns list of file paths
    """
    files_paths = []
    for root, _, files in os.walk(data_root_directry):
        for file in files:
            files_paths.append(os.path.join(root, file))
    return files_paths

def get_file_extension(file_path):
    """
    This function returns file extension of provided file path

    Args:
        file_path (str): path of one file

    Returns:
        str: extension of file ('pdf', 'doc', 'jpg' etc)
    """
    return file_path.split("\\")[-1].split('.')[-1].lower()

