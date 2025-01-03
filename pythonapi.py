from fastapi import FastAPI
from typing import List
import joblib
import uvicorn

app = FastAPI()
full_pl = joblib.load(filename="lightgbm_model.joblib")

@app.get("/")
def home():
    return {'api_availibility': 'OK_model_loaded'}

@app.post('/predict')
def post_data(data: List[float]):
  prediction = full_pl.predict(data)[0]
  if prediction == 1:
    return {'Prediction': 'Donner le crédit'}
  return {'Prediction': 'Ne pas donner le crédit'}
