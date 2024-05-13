import sys
from hateSpeechClassification.logger import logging
from hateSpeechClassification.exception import CustomException
from hateSpeechClassification.components.data_ingestion import DataIngestion
from hateSpeechClassification.components.data_transformations import DataTransformation
from hateSpeechClassification.components.data_validator import DataValidation
from hateSpeechClassification.components.model_trainer import ModelTraining
from hateSpeechClassification.components.model_evaluation import ModelEvaluation

from hateSpeechClassification.entity.config_entity import DataIngestionConfig, DataTransformationConfig, DataValidationConfig, ModelTrainingConfig, ModelEvaluationConfig
from hateSpeechClassification.entity.artifact_entity import DataIngestionArtifacts, DataTransformationArtifacts, DataValidationArtifacts, ModelTrainingArtifacts, ModelEvaluationArtifacts


class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_transformation_config = DataTransformationConfig()
        self.data_validation_config = DataValidationConfig()
        self.model_training_config = ModelTrainingConfig()
        self.model_evaluation_config = ModelEvaluationConfig()

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
        

    def start_model_training(self, data_transformation_artifacts: DataTransformationArtifacts) -> ModelTrainingArtifacts:
        try:
            logging.info("Inside the start_model_trainer method of TrainPipeline class")

            model_trainer = ModelTraining(
                data_transformation_artifacts=data_transformation_artifacts,
                model_training_config=self.model_training_config
            )

            model_training_artifacts = model_trainer.initiate_model_training()
            logging.info("Successfully completed start_model_trainer method of TrainPipeline class")
            
            return model_training_artifacts

        except Exception as e:
            raise CustomException(e, sys) 


    def start_model_evaluation(self, model_training_artifacts: ModelTrainingArtifacts, data_transformation_artifacts: DataTransformationArtifacts) -> ModelEvaluationArtifacts:
        try:
            logging.info("Inside the start_model_evaluation method of TrainPipeline class")

            model_evaluation = ModelEvaluation(
                model_evaluation_config = self.model_evaluation_config,
                model_training_artifacts= model_training_artifacts,
                data_transformation_artifacts = data_transformation_artifacts
            )

            model_evaluation_artifacts = model_evaluation.initiate_model_evaluation()
            logging.info("Successfully completed the start_model_evaluation method of TrainPipeline class")

            return model_evaluation_artifacts

        except Exception as e:
            raise CustomException(e, sys) from e


    def run_pipeline(self):
        try:
            logging.info('Inside run_pipeline method of TrainingPipeline class')

            data_ingestion_artifacts = self.start_data_ingestion()

            data_validation_artifacts = self.start_data_validation(
                data_ingestion_artifacts = data_ingestion_artifacts
            )

            data_transformation_artifacts = self.start_data_transformation(
                data_ingestion_artifacts = data_ingestion_artifacts
            )

            model_training_artifacts = self.start_model_training(
                data_transformation_artifacts=data_transformation_artifacts
            )

            model_evaluation_artifacts = self.start_model_evaluation(
                model_training_artifacts=model_training_artifacts,
                data_transformation_artifacts=data_transformation_artifacts
            ) 

            if not model_evaluation_artifacts.is_model_accepted:
                raise Exception("Trained model is not better than the best model")
            
            # model_pusher_artifacts = self.start_model_pusher()

            logging.info('Successfully completed run_pipeline method of TrainingPipeline class')
        except Exception as e:
            raise CustomException(e, sys) from e