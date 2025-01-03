# Création de l'API
from fastapi import FastAPI
from typing import List
import joblib
import uvicorn

app = FastAPI()
model_path = "/content/drive/MyDrive/openclassrooms/project_list/project_7/saved_model/lightgbm_model.joblib"

@app.get("/")
def home():
    return {'api_availibility': 'OK', "model_version": model_path}

@app.get('/test')
def get_test():
  model = joblib.load(filename=model_path)
  prediction = model.predict(X.head(1))
  return {'Prediction': prediction[0]}

@app.post('/predict')
def post_data(data: List[float]):
  model = joblib.load(filename=model_path)
  prediction = model.predict(data)[0]
  if prediction == 1:
    return {'Prediction': 'Donner le crédit'}
  return {'Prediction': 'Ne pas donner le crédit'}
