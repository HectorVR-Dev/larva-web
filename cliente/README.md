# Cliente WebRTC

Este proyecto es una aplicación cliente WebRTC construida con Vite y React. Permite la comunicación en tiempo real entre pares utilizando la tecnología WebRTC.

## Estructura del Proyecto

```
client/
├── node_modules/        # Módulos de Node.js
├── public/              # Activos públicos
├── src/                 # Código fuente
│   ├── components/      # Componentes de React
│   ├── styles/          # Estilos CSS
│   ├── App.jsx          # Componente principal App
│   ├── main.jsx         # Punto de entrada
│   └── ...              # Otros archivos fuente
├── .gitignore           # Archivo Git ignore
├── eslint.config.js     # Configuración de ESLint
├── index.html           # Plantilla HTML
├── package.json         # Configuración de paquete NPM
├── README.md            # Documentación del proyecto
└── vite.config.js       # Configuración de Vite
```

## Cómo Funciona

La aplicación cliente WebRTC establece una conexión peer-to-peer utilizando las APIs de WebRTC. Permite a los usuarios comunicarse en tiempo real a través de streams de video y audio.

### Características Principales

- Video en tiempo real
- Conexión peer-to-peer usando WebRTC
- Interfaz de usuario basada en React

## Primeros Pasos

### Requisitos Previos

- Node.js (versión 14 o superior)
- NPM (versión 6 o superior)

### Instalación

1. Instalar dependencias:

   ```bash
   npm install
   ```

2. iniciar el servidor de desarrollo, ejecuta:

   ```bash
   npm run dev
   ```

3. Puedes acceder a la aplicación desde la direccion indicada en la consola.

### Despliegue
Para la ejecucion del cliente con los demas servicios necesarios se crearon unos scripts .sh que se encargan de ejecutar los servicios necesarios para la comunicacion entre pares. Para ejecutar el cliente con los servicios necesarios se debe ejecutar el siguiente comando:

```bash
./run.sh
```
tambien se puede detener con el siguiente comando:

```bash 
./stop.sh
```