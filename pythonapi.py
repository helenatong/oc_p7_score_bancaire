from fastapi import FastAPI, HTTPException
import joblib
import uvicorn
import lightgbm
import pandas as pd
import imblearn
import logging

# Chargement des données
model_path = "lightgbm_model.joblib"
data_path = "aggregated_df_30_variables.pq"

full_pl = joblib.load(filename=model_path)
data = pd.read_parquet(data_path, engine='auto')
data.drop(columns=['TARGET'], inplace=True)

# Création de l'API
app = FastAPI()
@app.get("/")
def home():
    return {'api_availibility': 'OK'}

@app.post('/predict')
def post_data(id: int):
    try:
        if id not in data['SK_ID_CURR'].values:
            raise HTTPException(status_code=404, detail=f"ID {id} non trouvé")
            return (f"ID {id} non trouvé")
        chosen_data = data[data['SK_ID_CURR'] == id].drop(columns=['SK_ID_CURR'])
        prediction = full_pl.predict(chosen_data)
        proba = full_pl.predict_proba(chosen_data)
        result = {
            'client_id': id,
            'probabilité_de_remboursement': round(float(proba[0][1]), 2),  # Probabilité de la classe positive
            'prediction': 'Donner le crédit' if prediction[0] == 1 else 'Ne pas donner le crédit'
        }
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
