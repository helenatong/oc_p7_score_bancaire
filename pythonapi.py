from fastapi import FastAPI, HTTPException
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

# @app.post('/predict')
# def post_data():
#     # prediction = full_pl.predict(X.iloc[0].to_dict())
#     prediction = full_pl.predict(X.iloc[0].values.reshape(1, -1))
#     if prediction == 1:
#         return {'Prediction': 'Donner le crédit'}
#     return {'Prediction': 'Ne pas donner le crédit'}

@app.post('/predict')
async def post_data():
    try:
        # Ajoutons des logs pour voir où ça casse
        logger.info("Début de la prédiction")
        logger.info(f"Shape de X: {X.shape}")
        logger.info(f"Données d'entrée: {X.iloc[0].values}")
        
        prediction = full_pl.predict(X.iloc[0].values.reshape(1, -1))
        logger.info(f"Prédiction effectuée: {prediction}")
        
        result = {'Prediction': 'Donner le crédit' if prediction == 1 else 'Ne pas donner le crédit'}
        logger.info(f"Résultat final: {result}")
        return result
        
    except Exception as e:
        logger.error(f"Erreur détaillée: {str(e)}")
        logger.error(f"Type d'erreur: {type(e)}")
        # Retournons une erreur plus détaillée
        raise HTTPException(
            status_code=500,
            detail=f"Erreur lors de la prédiction: {str(e)}"
        )
