#!/bin/bash

LOG_FILE="python_dev.log"
PID_FILE="python_dev.pid"

# Verificar si ya hay un proceso corriendo
if [ -f "$PID_FILE" ]; then
    OLD_PID=$(cat "$PID_FILE")
    if ps -p "$OLD_PID" > /dev/null; then
        echo "Ya hay un proceso corriendo con PID $OLD_PID. Detenlo primero con './jetson/stop_python.sh'."
        exit 1
    else
        echo "Eliminando PID antiguo $OLD_PID (proceso no encontrado)."
        rm "$PID_FILE"
    fi
fi

# Activar el entorno virtual
echo "Activando entorno virtual..."
source venv/bin/activate || { echo "Error: No se pudo activar el entorno virtual"; exit 1; }

# Iniciar el script Python en segundo plano
echo "Iniciando jetson.py..."
ip=$(hostname -I | awk '{print $1}')
python3 test.py $ip
