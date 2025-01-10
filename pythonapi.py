from fastapi import FastAPI, HTTPException
import logging
from typing import List
import joblib
import uvicorn
import lightgbm
import pandas as pd
import imblearn



# Configuration du logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI()

# Logging du chargement des données
try:
    logger.info("Début du chargement du modèle")
    full_pl = joblib.load(filename="/content/drive/MyDrive/openclassrooms/project_list/project_7/saved_model/lightgbm_model.joblib")
    logger.info("Modèle chargé avec succès")

    logger.info("Début du chargement des données")
    data = pd.read_parquet("/content/drive/MyDrive/openclassrooms/project_list/project_7/data/aggregated_df_30_variables.pq", engine='auto')
    logger.info("Données chargées avec succès")
    X = data.drop(columns=['TARGET'])
    logger.info(f"Shape des données: {X.shape}")
except Exception as e:
    logger.error(f"Erreur lors du chargement: {str(e)}")
    raise

@app.get("/")
def home():
    logger.info("Accès à la page d'accueil")
    return {'api_availibility': 'OK_model_loaded'}

@app.post('/predict')
def post_data():
    try:
        logger.info("Début de la prédiction")
        prediction = full_pl.predict(X.iloc[0].values.reshape(1, -1))
        logger.info(f"Prédiction effectuée: {prediction}")
        
        result = {'Prediction': 'Donner le crédit' if prediction == 1 else 'Ne pas donner le crédit'}
        logger.info(f"Réponse envoyée: {result}")
        return result
        
    except Exception as e:
        logger.error(f"Erreur lors de la prédiction: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
        
# from fastapi import FastAPI, HTTPException
# from typing import List
# import joblib
# import uvicorn
# import lightgbm
# import pandas as pd
# import imblearn

# app = FastAPI()
# full_pl = joblib.load(filename="lightgbm_model.joblib")
# data = pd.read_parquet("aggregated_df_30_variables.pq", engine='auto')
# X = data.drop(columns = ['TARGET'])

# @app.get("/")
# def home():
#     return {'api_availibility': 'OK_model_loaded'}

# @app.post('/predict')
# def post_data():
#     # prediction = full_pl.predict(X.iloc[0].to_dict())
#     prediction = full_pl.predict(X.iloc[0].values.reshape(1, -1))
#     if prediction == 1:
#         return {'Prediction': 'Donner le crédit'}
#     return {'Prediction': 'Ne pas donner le crédit'}

#         raise HTTPException(
#             status_code=500,
#             detail=f"Erreur lors de la prédiction: {str(e)}"
#         )
