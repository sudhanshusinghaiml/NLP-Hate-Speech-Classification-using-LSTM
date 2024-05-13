import os
import io
import sys
import keras
import pickle
from PIL import Image
from keras.utils import pad_sequences

from hateSpeechClassification.logger import logging
from hateSpeechClassification.exception import CustomException
from hateSpeechClassification.constants import *
from hateSpeechClassification.configuration.gcloud_syncer import GCloudSync
from hateSpeechClassification.entity.config_entity import DataTransformationConfig
from hateSpeechClassification.entity.artifact_entity import DataIngestionArtifacts
from hateSpeechClassification.components.data_transformations import DataTransformation


class PredictionPipeline:
    def __init__(self):
        self.bucket_name = BUCKET_NAME
        self.model_name = MODEL_NAME
        self.model_path = PIPELINE_ARTIFACTS_DIR
        self.gcloud = GCloudSync()
        self.data_transformation = DataTransformation(
            data_transformation_config = DataTransformationConfig, 
            data_ingestion_artifacts = DataIngestionArtifacts
        )


    def get_model_from_gcloud(self) -> str:
        """
        Method Name :   get_model_from_gcloud
        Description :   This method to get best model from google cloud storage
        Output      :   best_model_path
        """
        try:
            logging.info("Inside the get_model_from_gcloud method of PredictionPipeline class")

            # Loading the best model from s3 bucket
            os.makedirs(self.model_path, exist_ok=True)

            best_model_path = os.path.join(self.model_path, self.model_name)

            if not os.path.exists(best_model_path):            
                self.gcloud.download_data_from_gcloud(self.bucket_name, self.model_name, self.model_path)
                logging.info(f"Model {self.model_name} downloaded in the path {self.model_path}")
            else:
                logging.info("Model is already downloaded in the directory")
            
            logging.info("Successfully completed executing get_model_from_gcloud method of PredictionPipeline class")
            
            return best_model_path

        except Exception as e:
            raise CustomException(e, sys) from e
        
    
    def predict(self, best_model_path, text):
        """load image, returns cuda tensor"""
        try:
            logging.info("Inside predict method in PredictionPipeline class")

            best_model_path:str = self.get_model_from_gcloud()
            
            load_model=keras.models.load_model(best_model_path)

            logging.info(f'Text before cleaning - {text}')

            with open('tokenizer.pickle', 'rb') as handle:
                load_tokenizer = pickle.load(handle)
            
            text=self.data_transformation.clean_data(text)

            text = [text]            

            logging.info(f'Text after cleaning - {text}')

            text_sequence = load_tokenizer.texts_to_sequences(text)

            logging.info(f'Text after text to sequence conversion - {text_sequence}')

            padded_sequence = pad_sequences(text_sequence, maxlen=MAXIMUM_LENGTH)

            logging.info(f'Text after padding sequence conversion - {padded_sequence}')

            predicted_result = load_model.predict(padded_sequence)

            logging.info(f'Predicted_result - {predicted_result}')

            if predicted_result>0.5:
                logging.info(f'Classified as Hate and Abusive Speech')
                logging.info("Successfully executed predict method in PredictionPipeline class")
                return "Hate and Abusive Speech"
            else:
                logging.info(f'Classified as No Hate Speech')
                logging.info("Successfully executed predict method in PredictionPipeline class")
                return "No Hate Speech"
            
        except Exception as e:
            raise CustomException(e, sys) from e
        
    
    def run_pipeline(self, text):
        try:

            logging.info("Inside run_pipeline method of PredictionPipeline class")

            best_model_path: str = self.get_model_from_gcloud() 

            predicted_text = self.predict(best_model_path, text)

            logging.info("Successfully executed  run_pipeline method of PredictionPipeline class")

            return predicted_text
        
        except Exception as e:
            raise CustomException(e, sys) from e