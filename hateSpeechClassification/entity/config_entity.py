from dataclasses import dataclass
from hateSpeechClassification.constants import *
import os

@dataclass
class DataIngestionConfig:
    def __init__(self):
        self.BUCKET_NAME = BUCKET_NAME
        self.ZIP_FILE_NAME = ZIP_FILE_NAME
        self.DATA_INGESTION_ARTIFACTS_DIR: str = os.path.join(os.getcwd(),ARTIFACTS_DIR, DATA_INGESTION_ARTIFACTS_DIR)
        self.IMBALANCED_DATA_ARTIFACTS: str = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR, DATA_INGESTION_IMBALANCE_DATA_FILE)
        self.RAW_DATA_ARTIFACTS: str = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR, DATA_INGESTION_RAW_DATA_FILE)
        self.ZIP_FILE_DIR: str = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR)
        self.ZIP_FILE_DIR_NAME: str = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR, self.ZIP_FILE_NAME)


@dataclass
class DataValidationConfig:
    def __init__(self):
        self.IMBALANCED_COLUMNS_SET = {IMB_ID, IMB_LABEL, IMB_TWEET}
        self.RAWDATA_COLUMNS_SET = {RAW_UNNAMED, RAW_COUNT, RAW_HATESPEECH, RAW_OFFENSIVE_LNG, RAW_NEITHER, RAW_CLASS, RAW_TWEET}



@dataclass
class DataTransformationConfig:
    def __init__(self):
        self.DATA_TRANSFORMATION_ARTIFACTS_DIR = os.path.join(os.getcwd(), ARTIFACTS_DIR, DATA_TRANSFORMATION_ARTIFACTS_DIR)
        self.TRANSFORMED_FILE_PATH = os.path.join(self.DATA_TRANSFORMATION_ARTIFACTS_DIR, TRANSFORMED_DATA_FILE)
        self.ID = ID
        self.AXIS = AXIS
        self.INPLACE = INPLACE 
        self.COLUMNS_TO_BE_DROPPED = COLUMNS_TO_BE_DROPPED
        self.CLASS = CLASS
        self.LABEL = LABEL
        self.TWEET = TWEET


@dataclass
class ModelTrainingConfig:
    def __init__(self):
        self.TRAINED_MODEL_DIR: str = os.path.join(os.getcwd(), ARTIFACTS_DIR, MODEL_TRAINER_ARTIFACTS_DIR)
        self.TRAINED_MODEL_PATH: str = os.path.join(self.TRAINED_MODEL_DIR, TRAINED_MODEL_NAME)
        self.X_TEST_DATA_PATH: str = os.path.join(self.TRAINED_MODEL_DIR, X_TEST_FILE_NAME)
        self.Y_TEST_DATA_PATH: str = os.path.join(self.TRAINED_MODEL_DIR, Y_TEST_FILE_NAME)
        self.X_TRAIN_DATA_PATH: str = os.path.join(self.TRAINED_MODEL_DIR, X_TRAIN_FILE_NAME)
        self.RANDOM_STATE = RANDOM_STATE
        self.EPOCH = EPOCH
        self.BATCH_SIZE = BATCH_SIZE
        self.VALIDATION_SPLIT = VALIDATION_SPLIT
        self.MAXIMUM_WORDS = MAXIMUM_WORDS
        self.MAXIMUM_LENGTH = MAXIMUM_LENGTH
        self.LOSS = LOSS
        self.METRICS = METRICS
        self.ACTIVATION = ACTIVATION
        self.LABEL = LABEL
        self.TWEET = TWEET



@dataclass
class ModelEvaluationConfig:
    def __init__(self):
        self.MODEL_EVALUATION_MODEL_DIR: str = os.path.join(os.getcwd(),ARTIFACTS_DIR, MODEL_EVALUATION_ARTIFACTS_DIR)
        self.BEST_MODEL_DIR_PATH: str = os.path.join(self.MODEL_EVALUATION_MODEL_DIR,BEST_MODEL_DIR)
        self.BUCKET_NAME = BUCKET_NAME 
        self.MODEL_NAME = MODEL_NAME