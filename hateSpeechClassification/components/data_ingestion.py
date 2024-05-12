import os
import sys
from zipfile import ZipFile
from hateSpeechClassification.logger import logging
from hateSpeechClassification.exception import CustomException
from hateSpeechClassification.entity.config_entity import DataIngestionConfig
from hateSpeechClassification.entity.artifact_entity import DataIngestionArtifacts
from hateSpeechClassification.configuration.gcloud_syncer import GCloudSync

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config
        self.gcloud = GCloudSync()

    def get_data_from_gcloud(self) -> None:
        try:
            logging.info('Inside the get_data_from_gcloud method of Data ingestion class')
            os.makedirs(self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR, exist_ok=True)

            self.gcloud.download_data_from_gcloud(
                self.data_ingestion_config.BUCKET_NAME,
                self.data_ingestion_config.ZIP_FILE_NAME,
                self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR
            )

            logging.info('Successfully executed get_data_from_gcloud method of Data ingestion class')
        except Exception as e:
            raise CustomException(e, sys) from e
        
    
    def extract_and_clean(self):
        logging.info('Inside the extract_and_clean method of Data ingestion class')

        try:
            with ZipFile(self.data_ingestion_config.ZIP_FILE_DIR_NAME, 'r') as zip_files:
                zip_files.extractall(self.data_ingestion_config.ZIP_FILE_DIR)

            logging.info("Extracted and cleaned zip files content")
            logging.info('Successfully executed extract_and_clean method of Data ingestion class')

            return self.data_ingestion_config.IMBALANCED_DATA_ARTIFACTS, self.data_ingestion_config.RAW_DATA_ARTIFACTS
        except Exception as e:
            raise CustomException(e, sys) from e      


    def initiate_data_ingestion(self) -> DataIngestionArtifacts:
        logging.info('Inside the initiate_data_ingestion method of Data ingestion class')

        try:
            self.get_data_from_gcloud()
            imbalanced_data_path, raw_data_path = self.extract_and_clean()
            
            data_ingestion_artifacts = DataIngestionArtifacts(
                imbalance_data_path = imbalanced_data_path,
                raw_data_path = raw_data_path
            )

            logging.info(f"Data ingestion artifact: {data_ingestion_artifacts}")

            logging.info('Successfully executed initiate_data_ingestion method of Data ingestion class')

            return data_ingestion_artifacts

        except Exception as e:
            raise CustomException(e, sys) from e

