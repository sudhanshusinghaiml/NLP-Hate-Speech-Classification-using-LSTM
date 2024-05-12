import sys
from hateSpeechClassification.logger import logging
from hateSpeechClassification.exception import CustomException
from hateSpeechClassification.components.data_ingestion import DataIngestion
from hateSpeechClassification.components.data_transformations import DataTransformation
from hateSpeechClassification.components.data_validator import DataValidation

from hateSpeechClassification.entity.config_entity import DataIngestionConfig, DataTransformationConfig, DataValidationConfig
from hateSpeechClassification.entity.artifact_entity import DataIngestionArtifacts, DataTransformationArtifacts, DataValidationArtifacts


class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_transformation_config = DataTransformationConfig()
        self.data_validation_config = DataValidationConfig()

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


    def start_data_validation(self, data_ingestion_artifacts: DataIngestionArtifacts) -> DataValidationArtifacts:
        logging.info("Inside start_data_validation method of TrainPipeline class")
        try:
            data_validation = DataValidation(
                data_ingestion_artifacts = data_ingestion_artifacts,
                data_validation_config = self.data_validation_config
            )

            data_validation_artifacts = data_validation.initiate_data_validation()
            
            logging.info("Successfully completed start_data_validation method of TrainPipeline class")

            return data_validation_artifacts

        except Exception as e:
            raise CustomException(e, sys) from e


    def start_data_transformation(self, data_ingestion_artifacts: DataIngestionArtifacts) -> DataTransformationArtifacts:
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

            data_validation_artifacts = self.start_data_validation(
                data_ingestion_artifacts = data_ingestion_artifacts
            )

            data_transformation_artifacts = self.start_data_transformation(
                data_ingestion_artifacts = data_ingestion_artifacts
            )

            logging.info('Successfully completed run_pipeline method of TrainingPipeline class')
        except Exception as e:
            raise CustomException(e, sys) from e