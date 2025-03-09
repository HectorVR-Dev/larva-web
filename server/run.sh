#!/bin/bash

LOG_FILE="python_dev.log"
PID_FILE="python_dev.pid"

# Verificar si ya hay un proceso corriendo
if [ -f "$PID_FILE" ]; then
    OLD_PID=$(cat "$PID_FILE")
    if ps -p "$OLD_PID" > /dev/null; then
        echo "Ya hay un proceso corriendo con PID $OLD_PID. Detenlo primero con './server/stop.sh'."
        exit 1
    else
        echo "Eliminando PID antiguo $OLD_PID (proceso no encontrado)."
        rm "$PID_FILE"
    fi
fi

# Activar el entorno virtual
echo "Activando entorno virtual..."
source ./venv/bin/activate || { echo "Error: No se pudo activar el entorno virtual"; exit 1; }

# Iniciar el script Python en segundo plano
echo "Iniciando server.py..."
python3 server.py > "$LOG_FILE" 2>&1 &

# Guardar el PID del proceso Python
PYTHON_PID=$!

# Esperar un momento para que el script inicie
sleep 1

# Verificar que el PID corresponde a python3 ejecutando jetson.py
ACTUAL_PID=$(ps aux | grep "[p]ython3.*server.py" | awk '{print $2}' | head -n 1)

if [ -z "$ACTUAL_PID" ]; then
    echo "No se pudo encontrar el PID de server.py. Usando el PID capturado como fallback: $PYTHON_PID"
    ACTUAL_PID=$PYTHON_PID
fi

# Guardar el PID en un archivo
echo "$ACTUAL_PID" > "$PID_FILE"

echo "Proceso corriendo en background con PID $ACTUAL_PID"
echo "PID guardado en $PID_FILE"
echo "Usa './server/stop.sh' para detenerlo."
echo "Logs disponibles en $LOG_FILE"
deactivate

# Desvincular el proceso de la terminal
disown "$PYTHON_PID"

exit 0