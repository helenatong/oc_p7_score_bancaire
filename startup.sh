apt-get update
apt-get install -y build-essential
apt-get install -y cmake
pip install -r requirements.txt

echo "------------------------------"
echo "------------------------------"
echo "OK packages installation ..."
echo "------------------------------"
echo "------------------------------"


uvicorn api.pythonapi:app --host 0.0.0.0 --port 8000 &
APP_PID=$!

sleep 30

pytest tests/ -v

if [ $? -ne 0 ]; then
    echo "------------------------------"
    echo "------------------------------"
    echo "Tests failed - stopping deployment ..."
    echo "------------------------------"
    echo "------------------------------" 
    kill $APP_PID  # Arrête l'application
    exit 1
fi

kill $APP_PID
echo "------------------------------"
echo "------------------------------"
echo "API unit tests success ..."
echo "------------------------------"
echo "------------------------------"

