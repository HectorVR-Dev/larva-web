# Proyecto Larva Web

## Descripción
Sistema de comunicación y procesamiento distribuido que integra aplicaciones cliente, señalización de red y procesamiento con hardware Jetson.

## Arquitectura

El proyecto consiste en tres componentes principales:

### 1. Cliente (Frontend)
Interfaz de usuario web que permite:
- Conexión al servidor de señalización
- Visualización de streams de video
- Control de los procesos en Jetson
- Interacción con los resultados procesados

### 2. Servidor de Señalización
Gestiona la comunicación entre clientes y dispositivos Jetson:
- Establece conexiones WebRTC
- Maneja autenticación de usuarios
- Distribuye mensajes entre componentes
- Orquesta los flujos de datos

### 3. Jetson (Procesamiento)
Unidad de procesamiento basada en NVIDIA Jetson que:
- Ejecuta algoritmos de visión por computador
- Procesa datos en tiempo real
- Transmite resultados al cliente
- Gestiona recursos de hardware especializado

## Scripts de Control

### run.sh
Script de inicialización que:
```bash
# Inicia todos los servicios del proyecto en el orden correcto
```

Este script realiza las siguientes acciones:
- Verifica dependencias necesarias
- Inicia el servidor de señalización
- Configura variables de entorno
- Establece conexiones con dispositivos Jetson
- Registra el inicio en logs

### stop.sh
Script para detener la ejecución del sistema:
```bash
# Detiene todos los servicios de manera ordenada
```

Este script realiza:
- Detención segura de los servicios
- Cierre de conexiones activas
- Limpieza de archivos temporales
- Liberación de puertos y recursos

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/usuario/larva_web.git
cd larva_web

# Instalar dependencias
./install.sh
```

## Uso Básico

1. Iniciar el sistema:
```bash
./run.sh
```

2. Acceder al cliente web en la direccion indicada en consola.

3. Detener el sistema:
```bash
./stop.sh
```