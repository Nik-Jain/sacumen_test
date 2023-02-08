from google.cloud import storage
from .settings import GCP_BUCKET_NAME, GCP_CRED_FILE_PATH

class GCP():
    """
    This class used for all operations related to Ggoogle cloud platform
    """
    def __init__(self):
        self.storage_client = storage.Client.from_service_account_json(GCP_CRED_FILE_PATH)
        self.bucket = self.storage_client.bucket(GCP_BUCKET_NAME)
        
    def upload_file(self, file_path):
        """
        Upload file to Google cloud storage bucket

        Args:
            file_path (str): file path which needs to be uploaded

        Returns:
            bool: True if file uploaded successfully else False
        """
        try:
            blob = self.bucket.blob(file_path.split('\\')[-1])
            blob.upload_from_filename(file_path)
        except Exception as e:
            return False
        return True
