from fastapi import FastAPI
from typing import List
import joblib
import uvicorn

app = FastAPI()
full_pl = joblib.load(filename="lightgbm_model.joblib")

@app.get("/")
def home():
    return {'api_availibility': 'OK_loaded'}


# @app.get("/")
# def home():
#     return {'api_availibility': 'OK_test', 'pipeline_loaded': full_pl}

# @app.get('/test')
# def get_test():
#   prediction = full_pl.predict(X.head(1))
#   return {'Prediction': prediction[0]}

# @app.post('/predict')
# def post_data(data: List[float]):
#   prediction = full_pl.predict(data)[0]
#   if prediction == 1:
#     return {'Prediction': 'Donner le crédit'}
#   return {'Prediction': 'Ne pas donner le crédit'}
