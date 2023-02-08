import boto3
from .settings import AWS_BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

class AWS():
    """
    This class used for all operations related to AWS cloud
    """
    def __init__(self):
        # Create S3 client using access_key_id and secret_key
        self.s3_client = boto3.client('s3',
                                   aws_access_key_id= AWS_ACCESS_KEY_ID,
                                   aws_secret_access_key= AWS_SECRET_ACCESS_KEY
                                   )
    
    def upload_file(self, file_path):
        """
        Upload file to S3 bucket

        Args:
            file_path (str): file path which needs to be uploaded

        Returns:
            bool: True if file uploaded successfully else False
        """
        try:
            self.s3_client.upload_file(file_path, AWS_BUCKET_NAME, file_path.split('\\')[-1])
        except Exception as e:
            return False
        return True
        