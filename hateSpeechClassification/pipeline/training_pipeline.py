import sys
from hateSpeechClassification.logger import logging
from hateSpeechClassification.exception import CustomException
from hateSpeechClassification.components.data_ingestion import DataIngestion
from hateSpeechClassification.components.data_transformations import DataTransformation

from hateSpeechClassification.entity.config_entity import DataIngestionConfig, DataTransformationConfig
from hateSpeechClassification.entity.artifact_entity import DataIngestionArtifacts, DataTransformationArtifacts


class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_transformation_config = DataTransformationConfig()

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


    def start_data_transformation(self, data_ingestion_artifacts = DataIngestionArtifacts) -> DataTransformationArtifacts:
        logging.info("Inside start_data_transformation method of TrainPipeline class")
        try:
            data_transformation = DataTransformation(
                data_ingestion_artifacts = data_ingestion_artifacts,
                data_transformation_config=self.data_transformation_config
            )

            data_transformation_artifacts = data_transformation.initiate_data_transformation()
            
            logging.info("Successfully completed start_data_transformation method of TrainPipeline class")
            return data_transformation_artifacts

        except Exception as e:
            raise CustomException(e, sys) from e


    def run_pipeline(self):
        logging.info('Insider run_pipeline method of TrainingPipeline class')
        try:
            data_ingestion_artifacts = self.start_data_ingestion()

            data_transformation_artifacts = self.start_data_transformation(
                data_ingestion_artifacts = data_ingestion_artifacts
            )

            logging.info('Successfully completed run_pipeline method of TrainingPipeline class')
        except Exception as e:
            raise CustomException(e, sys) from e