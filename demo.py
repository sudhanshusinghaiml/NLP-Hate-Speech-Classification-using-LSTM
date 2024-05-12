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

# importing pandas as pd
import pandas as pd

# Creating the DataFrame
df = pd.DataFrame({'Weight': [45, 88, 56, 15, 71],
				'Name': ['Sam', 'Andrea', 'Alex', 'Robin', 'Kia'],
				'Age': [14, 25, 55, 8, 21]})

# Set the index
columns_set = set(df.columns)

# Print the DataFrame
for col in df.columns:
    if col in columns_set:
        print(col)