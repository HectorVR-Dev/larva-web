#!/bin/bash

cd ./client || { echo "Error: No se pudo cambiar al directorio"; exit 1; }
./run.sh

cd ../server || { echo "Error: No se pudo cambiar al directorio"; exit 1; }
./run.sh

sleep 2

cd ../jetson || { echo "Error: No se pudo cambiar al directorio"; exit 1; }
./run.sh

exit 0
```
