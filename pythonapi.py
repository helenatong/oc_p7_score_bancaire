from fastapi import FastAPI
from typing import List
import joblib
import uvicorn

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, roc_auc_score, confusion_matrix
import imblearn, sklearn
from imblearn.over_sampling import SMOTE
from imblearn.over_sampling import RandomOverSampler
from sklearn import set_config
from imblearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

app = FastAPI()
full_pl = joblib.load(filename="Naive_model_no_modification.joblib")

@app.get("/")
def home():
    return {'api_availibility': 'OK_test', 'pipeline_loaded': full_pl}

@app.get('/test')
def get_test():
  prediction = full_pl.predict(X.head(1))
  return {'Prediction': prediction[0]}

@app.post('/predict')
def post_data(data: List[float]):
  prediction = full_pl.predict(data)[0]
  if prediction == 1:
    return {'Prediction': 'Donner le crédit'}
  return {'Prediction': 'Ne pas donner le crédit'}
