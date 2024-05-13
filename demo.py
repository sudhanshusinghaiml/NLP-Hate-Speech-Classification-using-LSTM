from hateSpeechClassification.logger import logging
from hateSpeechClassification.exception import CustomException
import sys
from hateSpeechClassification.configuration.gcloud_syncer import GCloudSync

# logging.info("Welcome to our Project - Hate Speech Classification")
#


### Checking the Custom Exception
# try:
#     a = 7 / 0
# 
# except Exception as e:
#     raise CustomException(e, sys) from e


### Testing the file upload and download to Google Cloud
# googleCloud = GCloudSync()
# googleCloud.download_data_from_gcloud('hate-speech-0905-2024-storage', 'dataset.zip', 'data')