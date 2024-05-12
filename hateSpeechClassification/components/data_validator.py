import os
import sys
import pandas as pd
from hateSpeechClassification.logger import logging
from hateSpeechClassification.entity.config_entity import DataValidationConfig
from hateSpeechClassification.entity.artifact_entity import DataIngestionArtifacts, DataValidationArtifacts
from hateSpeechClassification.exception import CustomException



class DataValidation:

    def __init__(self, data_ingestion_artifacts: DataIngestionArtifacts, data_validation_config: DataValidationConfig):
        self.data_ingestion_artifacts = data_ingestion_artifacts
        self.data_validation_config = data_validation_config

    def initiate_data_validation(self):
        try:
            imbalance_data_validated = True
            raw_data_validated = True
            logging.info("Inside validate_columns method from DataValidator class")

            imbalance_data=pd.read_csv(self.data_ingestion_artifacts.imbalance_data_path)
            raw_data = pd.read_csv(self.data_ingestion_artifacts.raw_data_path)

            for column in imbalance_data.columns:
                if column not in self.data_validation_config.IMBALANCED_COLUMNS_SET:
                    raise ValueError(f"Column validation failed: {column}")
 
            for column in raw_data.columns:
                if column not in self.data_validation_config.RAWDATA_COLUMNS_SET:
                    raise ValueError(f"Column validation failed: {column}")


            data_validation_artifacts = DataValidationArtifacts(
                    imbalance_dataset_columns = list(self.data_validation_config.IMBALANCED_COLUMNS_SET),
                    raw_dataset_columns = list(self.data_validation_config.RAWDATA_COLUMNS_SET)
            )

            logging.info("Successfully completed validate_columns method from DataValidator class")
            return data_validation_artifacts  
        except Exception as e:
            raise CustomException(e, sys) from e