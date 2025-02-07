from fastapi import FastAPI, HTTPException
import joblib
import uvicorn
import lightgbm
import pandas as pd
import imblearn

# Chargement des données
model_path = "models/lightgbm_model.joblib"
data_train_path = "data/aggregated_df_30_variables.pq"
data_test_path = "data/df_test_processed.pq"

full_pl = joblib.load(filename=model_path)
data_train = pd.read_parquet(data_train_path, engine='auto')
data_test = pd.read_parquet(data_test_path, engine='auto')

data = pd.concat([data_train, data_test], ignore_index=True)

data.drop(columns=['TARGET'], inplace=True)
proba_threshold = 0.53

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
        chosen_data = data[data['SK_ID_CURR'] == id].drop(columns=['SK_ID_CURR'])
        matrix_proba = full_pl.predict_proba(chosen_data)
        proba = round(float(matrix_proba[0][1]), 2) # Probabilité de la classe positive de l'id
        result = {
            'client_id': id,
            'probabilité_de_remboursement': proba,  
            'prediction': 'Donner le crédit' if proba >= proba_threshold else 'Ne pas donner le crédit'
        }
        return result
    except HTTPException as http_ex:
        raise http_ex
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
