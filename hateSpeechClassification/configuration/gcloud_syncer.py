import os

class GCloudSync:

    def upload_data_to_gcloud(self, gcp_bucket_url, filepath, filename):

        command = f"gsutil cp {filepath}/{filename} gs://{gcp_bucket_url}"
        os.system(command)


    def download_data_from_gcloud(self, gcp_bucket_url, filename, destination_path):

        command = f"gsutil cp gs://{gcp_bucket_url}/{filename} {destination_path}/{filename}"
        os.system(command)