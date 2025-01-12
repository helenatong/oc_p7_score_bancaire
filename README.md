# Projet de Scoring Crédit - Prêt à dépenser

## Description du Projet
Outil de scoring crédit développé pour la banque "Prêt à dépenser" permettant de :
- Calculer la probabilité de remboursement d'un crédit
- Classifier la demande (crédit accordé/refusé)
- Aider à la décision d'octroi de crédit

## Notebooks
1. **Préparation des données** 
  - Agrégation des tables sources
  - Sélection des 30 variables les plus corrélées

2. **Préprocessing et Modélisation**
  - Merge des différents datasets et choix des variables features
  - Préprocessing des variables
  - Tests de différents modèles avec/sans équilibrage de classe
  - Score business custom (coût faux positif = 10x faux négatif)
    ie: le coùt d'un crédit accordé non remboursé est 10x supérieur à un crédit non accordé mais qui est remboursé
  - Choix final : LightGBM

3. **Déploiement d'une API pour le modèle et tests API**
  - Mise à disposition du modèle sur le Cloud
  - Tests de l'API déployé sur Azure Cloud

## Structure du Projet

```
projet/
├── api/             # Code API
├── data/            # Dataset issue du prétraitement, utilisé pour l'entrainement et pour l'API
├── models/          # Modèles entraînés .joblib utilisé pour l'API
├── notebooks/       # Notebooks de préprocessing et de modélisation
├── requirements.txt # Version des packages pour le déploiement de l'API sur le Cloud
├── packages.txt     # Liste des versions des packages utilisés dans le projet
└── startup.sh/      # Installation des packages nécessaire pour l'API déployée sur le Cloud
```

## API
**Endpoint** : https://apigrantcredit.azurewebsites.net  
**Utilisation** : Envoi de l'ID crédit → Retour probabilité de remboursement

## Modèle 
- **Type** : LightGBM
- **Features** : 30 variables sélectionnées
- **Métrique** : Score business custom (FP=10×FN)

## Données
Source : https://www.kaggle.com/c/home-credit-default-risk/data
