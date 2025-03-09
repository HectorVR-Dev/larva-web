# Servidor Señalización WebRTC

Este proyecto es un servidor WebRTC implementado usando Flask, Flask-SocketIO y eventlet. Permite la señalización para la comunicación en tiempo real entre clientes a través de WebRTC.

## Estructura del Proyecto

```
server/
├── .gitignore           # Archivos ignorados por Git
├── cert.pem             # Certificado SSL
├── key.pem              # Clave privada SSL
├── README.md            # Documentación
├── requirements.txt     # Dependencias de Python
├── run.sh               # Script para iniciar el servidor
├── server.py            # Aplicación principal de Flask
└── stop.sh              # Script para detener el servidor
```

## Cómo Funciona

1. **Aplicación Flask**: La aplicación Flask está definida en `server.py`. Incluye rutas para manejar la señalización WebRTC a través de WebSocket usando Flask-SocketIO.

2. **Señalización WebRTC**: El servidor actúa como intermediario para el intercambio de mensajes de señalización (ofertas, respuestas y candidatos ICE) entre los clientes.

3. **Gestión de Salas**: El servidor permite a los clientes unirse a salas específicas para establecer comunicaciones por pares.

4. **Soporte de Renegociación**: El sistema admite la renegociación de conexiones cuando nuevos clientes se conectan.

## Configuración y Uso


1. **Crear un Entorno Virtual**:
    ```sh
    python -m venv venv
    ```

2. **Activar el Entorno Virtual**:
    ```sh
    source venv/bin/activate
    ```

3. **Instalar Dependencias**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Ejecutar el Servidor**:
    ```sh
    ./run.sh
    ```

5. **Detener el Servidor**:
    ```sh
    ./stop.sh
    ```

## Notas

- El servidor se ejecuta por defecto en el puerto 5000.
- Se incluyen certificados SSL (cert.pem y key.pem) que pueden activarse modificando server.py para usar HTTPS.
- Para desarrollo, si usas un certificado autofirmado, deberás importarlo en el almacén de certificados de tu sistema o navegador.
- En producción, se recomienda utilizar un certificado firmado por una Autoridad de Certificación reconocida (ej. Let's Encrypt).
