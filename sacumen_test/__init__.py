from . import helper
from .gcp import GCP
from .aws import AWS
from .settings import *

def upload_files(root_dir):
    """
    This function iterate thrrough root_dir and upload files of that directory and sub-directories into AWS S3 or google cloud storage based on file type.

    Args:
        root_dir (str): root directory path from where files need to be uploaded

    Returns:
        dict: dictionary with status, message and individual file status grouped into buckets
    """
    # Check if valid root directory provided
    if not os.path.exists(root_dir):
        return {'status': FAIL_STATUS, 
                'message':INVALID_PAH_MESSAGE, 
                'aws_success': [],
                'aws_failure': [],
                'gcp_success': [],
                'gcp_failure': [],
                'unsupported': []}

    aws_success, aws_failure, gcp_success, gcp_failure, unsupported = [], [], [], [], []
    aws = AWS()
    gcp = GCP()
    files_path = helper.get_file_paths(root_dir) # files_path : list of file paths
    for each_file in files_path:
        ext = helper.get_file_extension(each_file) # ext: file extension (pdf, jpeg etc.)
        if ext in AWS_FILE_EXTENSION:
            if aws.upload_file(each_file):
                aws_success.append(each_file)
            else:
                aws_failure.append(each_file)
        elif ext in GCP_FILE_EXTENSION:
            if gcp.upload_file(each_file):
                gcp_success.append(each_file)
            else:
                gcp_failure.append(each_file)
        else:
            unsupported.append(each_file)
    if aws_failure or gcp_failure or unsupported: # If any unsupported file or any failure in upload
        return {'status': FAIL_STATUS, 
                'message':FAILURE_MESSAGE, 
                'aws_success': aws_success,
                'aws_failure': aws_failure,
                'gcp_success': gcp_success,
                'gcp_failure': gcp_failure,
                'unsupported': unsupported}
    else:  # All files uploaded successfully
        return {'status': SUCCESS_STATUS, 
                'message':SUCCESS_MESSAGE, 
                'aws_success': aws_success,
                'aws_failure': aws_failure,
                'gcp_success': gcp_success,
                'gcp_failure': gcp_failure,
                'unsupported': unsupported}
