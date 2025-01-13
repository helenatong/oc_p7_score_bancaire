apt-get update
apt-get install -y build-essential
apt-get install -y cmake
pip install -r requirements.txt
uvicorn api.pythonapi:app --host 0.0.0.0 --port 8000
pytest tests/ -v
if [ $? -ne 0 ]; then
    echo "Tests failed - stopping deployment"
    exit 1
fi
