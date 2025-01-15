import pytest
import requests

API_URL = "https://apigrantcredit2.azurewebsites.net"

# Test de connexion à l'API
def test_home_connexion():
  response = requests.get(API_URL)
  assert response.status_code == 200
  assert response.json() == {'api_availibility': 'OK'}

# Tests de prédictions
@pytest.mark.parametrize("id,expected_proba,expected_output", [
    (100002, 0.85, "Donner le crédit"),
    (100006, 0.28, "Ne pas donner le crédit")
])
def test_credit_prediction(id, expected_proba, expected_output):
    response = requests.post(f"{API_URL}/predict", params={"id": id})
    result = response.json()

    assert response.status_code == 200
    assert result['client_id'] == id
    assert result['probabilité_de_remboursement'] == expected_proba
    assert result['prediction'] == expected_output

# Tests d'erreur
def test_client_id_not_found():
  id = 100000
  response = requests.post(API_URL+"/predict", params={"id": id})
  assert response.status_code == 404
  assert response.json()['detail'] == f"ID {id} non trouvé"

def test_missing_id():
  response = requests.post(API_URL+"/predict")
  assert response.status_code == 422
  assert response.json()['detail'][0]['type'] == 'value_error.missing'
