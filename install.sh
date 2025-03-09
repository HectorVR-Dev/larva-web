#!/bin/bash 

echo "Directorio actual: $(pwd)"

# Install the required packages client
apt install nodejs npm
cd ./client || { echo "Error: No se pudo cambiar al directorio"; exit 1; }
npm install || { echo "Error: No se puedo instalar dependecias del cliente"; exit 1; }

# Install the required packages server
cd ../server || { echo "Error: No se pudo cambiar al directorio"; exit 1; }
apt install python3-venv 
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate

# Install the required packages jetson

cd ../jetson
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate

echo "dependencias instaladas correctamente"
exit 0
```