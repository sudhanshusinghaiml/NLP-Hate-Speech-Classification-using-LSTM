import uvicorn
import sys

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response

from hateSpeechClassification.pipeline.training_pipeline import TrainingPipeline
from hateSpeechClassification.pipeline.prediction_pipeline import PredictionPipeline
from hateSpeechClassification.exception import CustomException
from hateSpeechClassification.constants import *

HateSpeechClassificationapp = FastAPI()

@HateSpeechClassificationapp.get('/', tags=['authentication'])
async def index():
    return RedirectResponse(url='/docs')


@HateSpeechClassificationapp.get('/train')
async def training():
    try:
        training_pipeline = TrainingPipeline()

        training_pipeline.run_pipeline()

        return Response("Training Successful !!")

    except Exception as e:
        raise CustomException(e, sys) from e
    


@HateSpeechClassificationapp.post('/predict')
async def predict_route(text):
    try:

        prediction_pipeline = PredictionPipeline()
        text = prediction_pipeline.run_pipeline(text)
        return text
    except Exception as e:
        raise CustomException(e, sys) from e
    

if __name__ == '__main__':
    uvicorn.run(HateSpeechClassificationapp, host = APP_HOST, port = APP_PORT)