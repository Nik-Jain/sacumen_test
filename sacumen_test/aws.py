import boto3
from .settings import AWS_BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

class AWS():
    def __init__(self):
        self.s3_client = boto3.client('s3',
                                   aws_access_key_id= AWS_ACCESS_KEY_ID,
                                   aws_secret_access_key= AWS_SECRET_ACCESS_KEY
                                   )
    
    def upload_file(self, file_path):
        try:
            self.s3_client.upload_file(file_path, AWS_BUCKET_NAME, file_path.split('\\')[-1])
        except Exception as e:
            return False
        return True
        