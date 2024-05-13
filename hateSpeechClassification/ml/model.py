# Create Model Architecture

# Creating model architecture.
from hateSpeechClassification.entity.config_entity import ModelTrainingConfig
from hateSpeechClassification.logger import logging
from keras.models import Sequential
from keras.optimizers import RMSprop
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.layers import LSTM, Activation, Dense, Dropout, Input, Embedding, SpatialDropout1D
from hateSpeechClassification.constants import *



class ModelArchitecture:

    def __init__(self):
        pass

    
    def get_model(self):
        model = Sequential()
        model.add(Embedding(MAXIMUM_WORDS, 100, input_length = MAXIMUM_LENGTH))
        model.add(SpatialDropout1D(0.2))
        model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))
        model.add(Dense(1, activation=ACTIVATION))
        model.summary()
        logging.info(f'Model Summary -\n{model.summary}')    
        model.compile(loss=LOSS, optimizer = RMSprop(), metrics = METRICS)

        return model