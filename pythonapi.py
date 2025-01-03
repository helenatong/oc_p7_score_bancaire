from fastapi import FastAPI
import uvicorn

app = FastAPI()
MODEL_PATH = os.path.join("models", "lightgbm_model.joblib")
model = joblib.load(filename=model_path)

@app.get("/")
def home():
    return {'api_availibility': 'OK', "model_name": MODEL_PATH}

@app.get('/test')
def get_test():
  prediction = model.predict(X.head(1))
  return {'Prediction': prediction[0]}

@app.post('/predict')
def post_data(data: List[float]):
  prediction = model.predict(data)[0]
  if prediction == 1:
    return {'Prediction': 'Donner le crédit'}
  return {'Prediction': 'Ne pas donner le crédit'}
