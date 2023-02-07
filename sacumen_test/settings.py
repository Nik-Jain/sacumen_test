import os

# AWS
AWS_BUCKET_NAME = os.environ['AWS_BUCKET_NAME']
AWS_FILE_EXTENSION = ['jpg', 'png', 'svg', 'webp', 'mp3', 'mp4', 'mpeg4', 'wmv', '3gp', 'webm']
AWS_ACCESS_KEY_ID= os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY= os.environ['AWS_SECRET_ACCESS_KEY']

# GCP
GCP_BUCKET_NAME = os.environ['GCP_BUCKET_NAME']
GCP_FILE_EXTENSION = ['doc', 'docx', 'csv', 'pdf']
GCP_CRED_FILE_PATH = os.environ['GCP_CRED_FILE_PATH']

# Status & Messages
FAIL_STATUS = 'FAIL'
SUCCESS_STATUS = 'SUCCESS'
SUCCESS_MESSAGE = 'All files uploaded sucessfully'
FAILURE_MESSAGE = 'Files upload failed or few files failed. Please check individual file status in response'
INVALID_PAH_MESSAGE = 'Provided path does not exist'