from google.cloud import storage
from .settings import GCP_BUCKET_NAME, GCP_CRED_FILE_PATH

class GCP():
    def __init__(self):
        self.storage_client = storage.Client.from_service_account_json(GCP_CRED_FILE_PATH)
        self.bucket = self.storage_client.bucket(GCP_BUCKET_NAME)
        
    def upload_file(self, file_path):
        try:
            blob = self.bucket.blob(file_path.split('\\')[-1])
            blob.upload_from_filename(file_path)
        except Exception as e:
            return False
        return True
