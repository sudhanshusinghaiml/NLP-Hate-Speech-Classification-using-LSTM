import os
from datetime import datetime



# Common Constants
TIMESTAMP: str = datetime.now().strftime('%m_%d_%Y_%H_%M_%S')
ARTIFACTS_DIR = os.path.join("artifacts", TIMESTAMP)
BUCKET_NAME = 'hate-speech-0905-2024-storage'
ZIP_FILE_NAME = 'dataset.zip'



# Data Ingestion Constants
DATA_INGESTION_ARTIFACTS_DIR = 'DataIngestionArtifacts'
DATA_INGESTION_IMBALANCE_DATA_FILE = 'imbalanced_data.csv'
DATA_INGESTION_RAW_DATA_FILE = 'raw_data.csv'



# Data Validator Constants
RAW_UNNAMED = 'Unnamed: 0'
RAW_COUNT = 'count'
RAW_HATESPEECH = 'hate_speech'
RAW_OFFENSIVE_LNG = 'offensive_language'
RAW_NEITHER = 'neither'
RAW_CLASS = 'class'
RAW_TWEET = 'tweet'

IMB_ID = 'id'
IMB_LABEL = 'label'
IMB_TWEET = 'tweet'



# Data Transformation Constants
DATA_TRANSFORMATION_ARTIFACTS_DIR = 'DataTransformationArtifacts'
TRANSFORMED_DATA_FILE = 'HateSpeechDataFinal.csv'
DATA_DIR = "data"
ID = 'id'
AXIS = 1
INPLACE = True
COLUMNS_TO_BE_DROPPED = ['Unnamed: 0','count','hate_speech','offensive_language','neither']
CLASS = 'class'
LABEL = 'label'
TWEET = 'tweet'


# Model Trainer Constants

