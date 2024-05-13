import os
import sys
import pickle
import pandas as pd
from hateSpeechClassification.logger import logging
from hateSpeechClassification.constants import * 
from hateSpeechClassification.exception import CustomException
from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer

from keras.utils import pad_sequences
from hateSpeechClassification.entity.config_entity import ModelTrainingConfig
from hateSpeechClassification.entity.artifact_entity import ModelTrainingArtifacts, DataTransformationArtifacts
from hateSpeechClassification.ml.model import ModelArchitecture

class ModelTraining:
    def __init__(self, data_transformation_artifacts: DataTransformationArtifacts, model_trainer_config: ModelTrainingConfig):
        self.data_transformation_artifacts = data_transformation_artifacts
        self.model_trainer_config = model_trainer_config

    def data_splitting(self, csv_path):
        try:
            logging.info("Inside the data_splitting function of ModelTraining Class")
            logging.info("Reading the data")
            df = pd.read_csv(csv_path, index_col=False)
            logging.info("Splitting the data into X and Y")
            x = df[TWEET]
            y = df[LABEL]

            logging.info("Applying train_test_split on the data")
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= VALIDATION_SPLIT, random_state = RANDOM_STATE)

            print(len(x_train),len(y_train))
            print(len(x_test),len(y_test))
            print(type(x_train),type(y_train))
            logging.info("Successfully completed data_splitting function of ModelTraining Class")

            return x_train, x_test, y_train, y_test

        except Exception as e:
            raise CustomException(e, sys) from e
        


    def tokenizing(self, x_train):
        try:
            logging.info("Applying tokenization on the data")
            
            tokenizer = Tokenizer(num_words = self.model_trainer_config.MAXIMUM_WORDS)
            
            tokenizer.fit_on_texts(x_train)
            
            sequences = tokenizer.texts_to_sequences(x_train)
            
            # logging.info(f"converting text to sequences: {sequences}")
            sequences_matrix = pad_sequences(sequences, maxlen=self.model_trainer_config.MAXIMUM_LENGTH)
            
            # logging.info(f" The sequence matrix is: {sequences_matrix}")
            return sequences_matrix, tokenizer
        except Exception as e:
            raise CustomException(e, sys) from e
        


    def initiate_model_training(self) -> ModelTrainingArtifacts:
        """
        Method Name :   initiate_model_trainer
        Description :   This function initiates a model trainer steps
        
        Output      :   Returns model trainer artifact
        On Failure  :   Write an exception log and then raise an exception
        """

        try:
            logging.info("Inside initiate_model_training method of ModelTrainer class")
            x_train, x_test, y_train, y_test = self.data_splitting(csv_path = self.data_transformation_artifacts.transformed_data_path)
            
            model_architecture = ModelArchitecture()   

            model = model_architecture.get_model()

            logging.info(f"X_train size is : {x_train.shape}")

            logging.info(f"X_test size is : {x_test.shape}")

            sequences_matrix, tokenizer = self.tokenizing(x_train)


            logging.info("Model Training started")

            model.fit(sequences_matrix, y_train, 
                        batch_size=self.model_trainer_config.BATCH_SIZE, 
                        epochs = self.model_trainer_config.EPOCH, 
                        validation_split=self.model_trainer_config.VALIDATION_SPLIT, 
                        )
            
            logging.info("Model training finished")

            with open('tokenizer.pickle', 'wb') as handle:
                pickle.dump(tokenizer, handle, protocol = pickle.HIGHEST_PROTOCOL)
            os.makedirs(self.model_trainer_config.TRAINED_MODEL_DIR, exist_ok=True)
            logging.info("Completed - Tokenizer saved")

            logging.info("Completed - Model saved")
            model.save(self.model_trainer_config.TRAINED_MODEL_PATH)
            x_test.to_csv(self.model_trainer_config.X_TEST_DATA_PATH)
            y_test.to_csv(self.model_trainer_config.Y_TEST_DATA_PATH)
            x_train.to_csv(self.model_trainer_config.X_TRAIN_DATA_PATH)

            model_trainer_artifacts = ModelTrainingArtifacts(
                trained_model_path = self.model_trainer_config.TRAINED_MODEL_PATH,
                x_test_path = self.model_trainer_config.X_TEST_DATA_PATH,
                y_test_path = self.model_trainer_config.Y_TEST_DATA_PATH)
            logging.info("Returning the ModelTrainingArtifacts")
            return model_trainer_artifacts

        except Exception as e:
            raise CustomException(e, sys) from e