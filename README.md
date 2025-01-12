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

2. **Modélisation**
  - Tests de différents modèles avec/sans équilibrage de classe
  - Score business custom (coût faux positif = 10x faux négatif)
    ie: le coùt d'un crédit accordé non remboursé est 10x supérieur à un crédit non accordé mais qui est remboursé
  - Choix final : LightGBM

3. **Monitoring**
  - Analyse du data drift sur les 30 features
  - Résultat : Pas de drift global observé, 5 drifts locaux mais pas d'impact sur le modèle

4. **Déploiement d'une API pour le modèle et tests API**
  - Mise à disposition du modèle sur le Cloud
  - Tests de l'API déployé sur Azure Cloud

## Structure du Projet

```
projet/
├── data/          # Données brutes et traitées
├── notebooks/     # Notebooks d'analyse (1 à 4)
├── src/           # Code source
├── tests/         # Tests unitaires
├── api/           # Code API
├── dashboard/     # Interface utilisateur
├── models/        # Modèles entraînés
└── requirements.txt
```


## API
**Endpoint** : https://apigrantcredit.azurewebsites.net  
**Utilisation** : Envoi de l'ID crédit → Retour probabilité de remboursement

## Modèle 
- **Type** : LightGBM
- **Features** : 30 variables sélectionnées
- **Métrique** : Score business custom (FP=10×FN)

## Données
Source : [Lien vers les données]

## Tests
Tests unitaires de l'API disponibles dans `tests/`
