from fastapi import FastAPI
from typing import List
import joblib
import uvicorn
import lightgbm
import pandas as pd
import imblearn

app = FastAPI()
full_pl = joblib.load(filename="lightgbm_model.joblib")
data = pd.read_parquet("aggregated_df_30_variables.pq", engine='auto')
X = data.drop(columns = ['TARGET'])

@app.get("/")
def home():
    return {'api_availibility': 'OK_model_loaded'}

@app.post('/predict')
def post_data():
    prediction = full_pl.predict(X.iloc[0])
    if prediction == 1:
        return {'Prediction': 'Donner le crédit'}
    return {'Prediction': 'Ne pas donner le crédit'}
