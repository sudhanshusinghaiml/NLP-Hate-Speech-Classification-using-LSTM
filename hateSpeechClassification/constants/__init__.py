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


# Model Training Constants
MODEL_TRAINER_ARTIFACTS_DIR = 'ModelTrainerArtifacts'
TRAINED_MODEL_DIR = 'TrainedModel'
TRAINED_MODEL_NAME = 'model.h5'
X_TEST_FILE_NAME = 'x_test.csv'
Y_TEST_FILE_NAME = 'y_test.csv'

X_TRAIN_FILE_NAME = 'x_train.csv'

RANDOM_STATE = 42
EPOCH = 1
BATCH_SIZE = 128
VALIDATION_SPLIT = 0.2


# Model Architecture Constants
MAXIMUM_WORDS = 50000
MAXIMUM_LENGTH = 300
LOSS = 'binary_crossentropy'
METRICS = ['accuracy']
ACTIVATION = 'sigmoid'


# Model Evaluation Constants
MODEL_EVALUATION_ARTIFACTS_DIR = 'ModelEvaluationArtifacts'
BEST_MODEL_DIR = "BestModel"
MODEL_EVALUATION_FILE_NAME = "loss.csv"
MODEL_NAME = 'model.h5'

APP_HOST = "0.0.0.0"
APP_PORT = 8080