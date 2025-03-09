# Servidor WebRTC para Jetson

Este proyecto implementa un cliente WebRTC para la transmisión de video desde una Jetson (Nano/Orin Nano) a un navegador web. Permite la comunicación bidireccional en tiempo real para transmisión de video y control remoto del sistema óptico.

## Estructura del Proyecto

```
jetson/
├── .gitignore           # Archivos ignorados por Git
├── control.py           # Módulo para control de motores 
├── main.py              # Aplicación principal WebRTC
├── README.md            # Este archivo de documentación
├── requirements.txt     # Dependencias de Python
├── run.sh               # Script para iniciar el servicio
├── stop.sh              # Script para detener el servicio
└── test.py              # Versión de prueba del script principal
```

## Funcionalidades

- **Transmisión de Video en Tiempo Real**: Captura video desde la cámara conectada y lo transmite mediante WebRTC.
- **Control Bidireccional**: Recibe comandos para controlar:
    - Posición del microscopio (motores X, Y)
    - Enfoque (motor Z)
    - Intensidad de iluminación (3 niveles)
    - Encendido/apagado del sistema
- **Conexión Automática**: Se conecta automáticamente al servidor de señalización para establecer la comunicación WebRTC.

## Requisitos

- Python 3.7+
- Jetson Nano/Xavier con JetPack instalado
- Cámara USB o módulo de cámara compatible
- Conexión a la misma red que el servidor de señalización

## Dependencias

Las principales dependencias se encuentran en `requirements.txt`:
- asyncio
- opencv-python
- python-socketio[asyncio]
- aiohttp
- aiortc
- av
- urllib3
- Jetson.GPIO (para control de hardware)
- RPi.GPIO (para simulación de hardware)

## Instalación

1. Crear y activar un entorno virtual:
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```
    **Nota:** Si el entorno virtual no riene acceso a lo pines fisicos se debe instalar en un entorno global.

3. Instalar dependencias:
     ```
     pip install -r requirements.txt
     ```

## Configuración

El sistema utiliza GPIO para controlar motores paso a paso y relés para la iluminación. La configuración de los pines se encuentra en `control.py`. Ajusta estos valores según tu configuración de hardware específica.

## Uso

### Iniciar el servicio

```bash
./run.sh
```

El script detectará automáticamente la dirección IP del sistema y establecerá la conexión WebRTC con el servidor de señalización.

### Detener el servicio

```bash
./stop.sh
```

## Funcionamiento

1. El script `main.py` inicia una conexión con el servidor de señalización WebRTC.
2. Establece un canal de datos para recibir comandos de control.
3. Transmite el video de la cámara conectada como un flujo WebRTC.
4. Procesa los mensajes recibidos y controla los motores/iluminación según corresponda.

## Comandos de control

- **Movimiento X/Y**: "x_R", "x_L", "y_R", "y_L"
- **Enfoque (Z)**: "z_R", "z_L"
- **Control de iluminación**: "1", "2", "3" (niveles de intensidad)
- **Encendido/Apagado**: "turn on", "turn off"

## Desarrollo

Para probar nuevas funcionalidades sin afectar el hardware, use `test.py` que simula las respuestas de hardware.