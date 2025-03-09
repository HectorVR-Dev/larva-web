#!/bin/bash

LOG_FILE="python_dev.log"
PID_FILE="python_dev.pid"

if [ ! -f "$PID_FILE" ]; then
    echo "No se encontró el archivo $PID_FILE. No puedo detener el proceso."
    exit 1
fi

PYTHON_PID=$(cat "$PID_FILE")

if [ -z "$PYTHON_PID" ]; then
    echo "El archivo $PID_FILE está vacío. No hay PID para detener."
    exit 1
fi

echo "Deteniendo el proceso con PID $PYTHON_PID..."
kill "$PYTHON_PID"

# Esperar y verificar si sigue vivo
sleep 1
if ps -p "$PYTHON_PID" > /dev/null; then
    echo "El proceso no se detuvo. Forzando con kill -9..."
    kill -9 "$PYTHON_PID"
fi

# Limpiar archivos
rm "$PID_FILE"
[ -f "$LOG_FILE" ] && rm "$LOG_FILE"
echo "Proceso detenido y archivos limpiados."