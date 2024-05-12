import sys
from hateSpeechClassification.logger import logging
from hateSpeechClassification.exception import CustomException
from hateSpeechClassification.components.data_ingestion import DataIngestion

from hateSpeechClassification.entity.config_entity import DataIngestionConfig
from hateSpeechClassification.entity.artifact_entity import DataIngestionArtifacts


class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def start_data_ingestion(self) -> DataIngestionArtifacts:
        logging.info('Inside start_data_ingestion method of TrainingPipeline class')
        try:
            logging.info("Getting the data from GCLoud Storage bucket")
            data_ingestion = DataIngestion(data_ingestion_config = self.data_ingestion_config)

            data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
            
            logging.info("Saved the train and validation data from GCLoud Storage")
            logging.info("Successfully executed start_data_ingestion method of TrainPipeline class")

            return data_ingestion_artifacts
        
        except Exception as e:
            raise CustomException(e, sys) from e



    def run_pipeline(self):
        logging.info('Insider run_pipeline method of TrainingPipeline class')
        try:
            data_ingestion_artifacts = self.start_data_ingestion()

            logging.info('Successfully completed run_pipeline method of TrainingPipeline class')
        except Exception as e:
            raise CustomException(e, sys) from e