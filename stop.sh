#!/bin/bash

cd ./client || { echo "Error: No se pudo cambiar al directorio"; exit 1; }
./stop.sh

cd ../server || { echo "Error: No se pudo cambiar al directorio"; exit 1; }
./stop.sh

cd ../jetson || { echo "Error: No se pudo cambiar al directorio"; exit 1; }
./stop.sh

cd ..

disown

exit 0
```