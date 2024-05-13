import os
import sys
import re
import string
import pandas as pd
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from sklearn.model_selection import train_test_split
from hateSpeechClassification.logger import logging
from hateSpeechClassification.exception import CustomException
from hateSpeechClassification.entity.config_entity import DataTransformationConfig
from hateSpeechClassification.entity.artifact_entity import DataIngestionArtifacts, DataTransformationArtifacts




class DataTransformation:
    def __init__(self, data_transformation_config: DataTransformationConfig, data_ingestion_artifacts: DataIngestionArtifacts):
        self.data_transformation_config = data_transformation_config
        self.data_ingestion_artifacts = data_ingestion_artifacts


    def clean_imbalanced_data(self):
        try:
            logging.info("Inside clean_imbalanced_data method from DataTransformation class")

            imbalance_data=pd.read_csv(self.data_ingestion_artifacts.imbalance_data_path)

            imbalance_data.drop(self.data_transformation_config.ID, axis=self.data_transformation_config.AXIS, inplace = self.data_transformation_config.INPLACE)
            
            logging.info("Successfully executed clean_imbalanced_data method from DataTransformation class")
            
            return imbalance_data
        except Exception as e:
            raise CustomException(e, sys) from e
        

    def clean_raw_data(self):
        try:
            logging.info('Inside clean_raw_data method from DataTransformation class')
            raw_data = pd.read_csv(self.data_ingestion_artifacts.raw_data_path)

            raw_data.drop(self.data_transformation_config.COLUMNS_TO_BE_DROPPED,axis = self.data_transformation_config.AXIS, inplace = self.data_transformation_config.INPLACE)

            # raw_data[raw_data[self.data_transformation_config.CLASS]==0][self.data_transformation_config.CLASS]=1
            
            # replace the value of 0 to 1
            raw_data[self.data_transformation_config.CLASS].replace({0:1},inplace=self.data_transformation_config.INPLACE)

            # Let's replace the value of 2 to 0.
            raw_data[self.data_transformation_config.CLASS].replace({2:0}, inplace = self.data_transformation_config.INPLACE)

            # Let's change the name of the 'class' to label
            raw_data.rename(columns={self.data_transformation_config.CLASS:self.data_transformation_config.LABEL},inplace =self.data_transformation_config.INPLACE)

            logging.info("Successfully executed clean_raw_data method from DataTransformation class")

            return raw_data
        
        except Exception as e:
            raise CustomException(e, sys) from e
        

    def concat_raw_and_imbalanced_data(self):

        try:
            logging.info("Inside concat_raw_and_imbalanced_data method from DataTransformation Class")
            # Let's concatinate both the data into a single data frame.
            frame = [self.clean_raw_data(), self.clean_imbalanced_data()]
            df = pd.concat(frame)
            print(df.head())

            logging.info('Successfully completed concat_raw_and_imbalanced_data method from DataTransformation Class')
            return df

        except Exception as e:
            raise CustomException(e, sys) from e
            

    def clean_data(self, words):

        try:
            # Let's apply stemming and stopwords on the data
            stemmer = nltk.SnowballStemmer("english")
            stopword = set(stopwords.words('english'))
            words = str(words).lower()
            words = re.sub('\[.*?\]', '', words)
            words = re.sub('https?://\S+|www\.\S+', '', words)
            words = re.sub('<.*?>+', '', words)
            words = re.sub('[%s]' % re.escape(string.punctuation), '', words)
            words = re.sub('\n', '', words)
            words = re.sub('\w*\d\w*', '', words)
            words = [word for word in words.split(' ') if words not in stopword]
            words=" ".join(words)
            words = [stemmer.stem(word) for word in words.split(' ')]
            words=" ".join(words)

            # logging.info("Successfully completed clean_data method from DataTransformation Class")
            return words 

        except Exception as e:
            raise CustomException(e, sys) from e
        
        
    def initiate_data_transformation(self) -> DataTransformationArtifacts:
        try:
            logging.info("Inside initiate_data_transformation method from DataTransformation Class")

            self.clean_imbalanced_data()

            self.clean_raw_data()

            df = self.concat_raw_and_imbalanced_data()

            logging.info("Calling clean_data method from DataTransformation Class")
            df[self.data_transformation_config.TWEET] = df[self.data_transformation_config.TWEET].apply(self.clean_data)
            logging.info("Successfully completed clean_data method from DataTransformation Class")

            os.makedirs(self.data_transformation_config.DATA_TRANSFORMATION_ARTIFACTS_DIR, exist_ok=True)

            df.to_csv(self.data_transformation_config.TRANSFORMED_FILE_PATH, index=False, header=True)

            data_transformation_artifact = DataTransformationArtifacts(transformed_data_path= self.data_transformation_config.TRANSFORMED_FILE_PATH)
            
            logging.info("Successfully completed initiate_data_transformation method from DataTransformation Class")

            return data_transformation_artifact

        except Exception as e:
            raise CustomException(e, sys) from e    