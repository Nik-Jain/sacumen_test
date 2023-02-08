import pytest
import os

from ..sacumen_test import upload_files
from ..sacumen_test import settings, helper


BASE_DIR = os.path.dirname(os.path.realpath(__file__))
TEST_DATA_PATH = os.path.join(BASE_DIR, 'data')

def test_aws_bucket_name():
    assert len(settings.AWS_BUCKET_NAME) > 1

def test_aws_access_key_id():
    assert len(settings.AWS_ACCESS_KEY_ID) > 1

def test_aws_secret_access_key():
    assert len(settings.AWS_SECRET_ACCESS_KEY) > 1
    
def test_gcp_bucket_name():
    assert len(settings.GCP_BUCKET_NAME) > 1

def test_gcp_cred_file_path():
    assert len(settings.GCP_CRED_FILE_PATH) > 1

def test_get_file_extension():
    assert helper.get_file_extension(os.path.join(TEST_DATA_PATH,'dummy.pdf')) == 'pdf'

def test_get_file_paths():
    assert helper.get_file_paths(TEST_DATA_PATH) == [os.path.join(TEST_DATA_PATH,'dummy.pdf'), 
                                                     os.path.join(TEST_DATA_PATH, 'file-sample_100kB.doc'), 
                                                     os.path.join(TEST_DATA_PATH, 'image2.jpg'), 
                                                     os.path.join(TEST_DATA_PATH, 'image3.jpeg'), 
                                                     os.path.join(TEST_DATA_PATH, 'sample3.json'), 
                                                     os.path.join(TEST_DATA_PATH, 'inner\\file-sample_500kB.doc'), 
                                                     os.path.join(TEST_DATA_PATH, 'inner\\file_example_MP3_700KB.mp3'), 
                                                     os.path.join(TEST_DATA_PATH, 'inner\\file_example_MP4_480_1_5MG.mp4'), 
                                                     os.path.join(TEST_DATA_PATH, 'inner\\image1.jpeg'), 
                                                     os.path.join(TEST_DATA_PATH, 'inner\\sample.pdf'), 
                                                     os.path.join(TEST_DATA_PATH, 'inner\\sample1.json')]
def test_upload_files():
    assert upload_files(TEST_DATA_PATH) == {'status': 'FAIL', 
                                            'message': 'Files upload failed or few files failed. Please check individual file status in response', 
                                            'aws_success': [os.path.join(TEST_DATA_PATH, 'image2.jpg'), os.path.join(TEST_DATA_PATH, 'inner\\file_example_MP3_700KB.mp3'), os.path.join(TEST_DATA_PATH, 'inner\\file_example_MP4_480_1_5MG.mp4')], 
                                            'aws_failure': [], 
                                            'gcp_success': [os.path.join(TEST_DATA_PATH, 'dummy.pdf'), os.path.join(TEST_DATA_PATH, 'file-sample_100kB.doc'), os.path.join(TEST_DATA_PATH, 'inner\\file-sample_500kB.doc'), os.path.join(TEST_DATA_PATH, 'inner\\sample.pdf')], 
                                            'gcp_failure': [], 
                                            'unsupported': [os.path.join(TEST_DATA_PATH, 'image3.jpeg'), os.path.join(TEST_DATA_PATH, 'sample3.json'), os.path.join(TEST_DATA_PATH, 'inner\\image1.jpeg'), os.path.join(TEST_DATA_PATH, 'inner\\sample1.json')]}

def test_invalid_root_path():
    assert upload_files(os.path.join(BASE_DIR, 'dummy')) == {'status': settings.FAIL_STATUS, 
                'message':settings.INVALID_PAH_MESSAGE, 
                'aws_success': [],
                'aws_failure': [],
                'gcp_success': [],
                'gcp_failure': [],
                'unsupported': []}

