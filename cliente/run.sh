#!/bin/bash

LOG_FILE="npm_dev.log"
PID_FILE="npm_dev.pid"

# Verificar si ya hay un proceso corriendo
if [ -f "$PID_FILE" ]; then
    OLD_PID=$(cat "$PID_FILE")
    if ps -p "$OLD_PID" > /dev/null; then
        echo "Ya hay un proceso corriendo con PID $OLD_PID. Detenlo primero con './stop_dev.sh'."
        exit 1
    else
        echo "Eliminando PID antiguo $OLD_PID (proceso no encontrado)."
        rm "$PID_FILE"
    fi
fi

ip=$(hostname -I | awk '{print $1}')
echo "VITE_SYSTEM_IP=$ip" > .env

# Iniciar npm run dev en segundo plano
echo "Iniciando npm run dev..."
npm run dev > "$LOG_FILE" 2>&1 &

# Guardar el PID de npm (temporalmente)
NPM_PID=$!

# Esperar a que el servidor arranque
sleep 3

# Buscar el PID del proceso node que ejecuta vite
NODE_PID=$(ps aux | grep "[n]ode.*vite.*--host" | grep "$(pwd)" | awk '{print $2}' | head -n 1)

if [ -z "$NODE_PID" ]; then
    echo "No se pudo encontrar el PID de vite. Usando el PID de npm como fallback: $NPM_PID"
    NODE_PID=$NPM_PID
fi

# Guardar el PID en un archivo
echo "$NODE_PID" > "$PID_FILE"

# Mostrar la dirección de despliegue
echo "Dirección de despliegue:"
grep -E "Local:|Network:" "$LOG_FILE" || echo "No se encontró la dirección aún, revisa $LOG_FILE"

echo "Proceso corriendo en background con PID $NODE_PID"
echo "PID guardado en $PID_FILE"
echo "Usa './stop_dev.sh' para detenerlo."

# Desvincular el proceso de la terminal
disown "$NPM_PID"

exit 0