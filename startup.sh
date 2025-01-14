echo "---------STARUP FROM GITHUB----------"
echo "------------------------------"
echo "packages installation  FROM GITHUB..."
echo "------------------------------"

apt-get update
apt-get install -y build-essential
apt-get install -y cmake
pip install -r requirements.txt

echo "------------------------------"
echo "packages installation success  FROM GITHUB..."
echo "------------------------------"


uvicorn api.pythonapi:app --host 0.0.0.0 --port 8000 &
APP_PID=$!

sleep 30

echo "------------------------------"
echo "begin API unit tests FROM GITHUB ..."
echo "------------------------------"

pytest tests/ -v

if [ $? -ne 0 ]; then
    echo "------------------------------"
    echo "ERROR: API unit tests failed - stopping deployment  FROM GITHUB..."
    echo "------------------------------"
    kill $APP_PID
    exit 1
fi

kill $APP_PID

echo "------------------------------"
echo "API unit tests success ..."
echo "------------------------------"
