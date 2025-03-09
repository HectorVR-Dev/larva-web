#!/bin/bash

LOG_FILE="npm_dev.log"
PID_FILE="npm_dev.pid"

if [ ! -f "$PID_FILE" ]; then
    echo "No se encontró el archivo $PID_FILE. No puedo detener el proceso."
    exit 1
fi

NODE_PID=$(cat "$PID_FILE")

if [ -z "$NODE_PID" ]; then
    echo "El archivo $PID_FILE está vacío. No hay PID para detener."
    exit 1
fi

echo "Deteniendo el proceso con PID $NODE_PID..."
kill "$NODE_PID"

# Esperar y verificar si sigue vivo
sleep 1
if ps -p "$NODE_PID" > /dev/null; then
    echo "El proceso no se detuvo. Forzando con kill -9..."
    kill -9 "$NODE_PID"
fi

# Limpiar archivos
rm "$PID_FILE"
[ -f "$LOG_FILE" ] && rm "$LOG_FILE"
echo "Proceso detenido y archivos limpiados."