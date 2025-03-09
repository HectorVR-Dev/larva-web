import asyncio
import cv2
import socketio
from aiortc import RTCPeerConnection, VideoStreamTrack, RTCSessionDescription, RTCIceCandidate, MediaStreamTrack, RTCConfiguration, RTCIceServer
from av import VideoFrame
import time
from fractions import Fraction
import urllib3
from aiortc.sdp import candidate_from_sdp
import sys
#import control as ctrl # Importar modulo de control

ip = sys.argv[1]

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Se ajustan los parámetros de reconexión para acelerar la reconexión
sio = socketio.AsyncClient(
    reconnection_attempts=5,
    reconnection_delay=0.1,        
    reconnection_delay_max=1.0,     
    randomization_factor=0.5
)
ROOM_ID = "jetson-room"
pc = None 
control_channel = None
# Nuevo: Lista para almacenar mensajes recibidos por el canal de datos
received_messages = []

class SignalingNamespace(socketio.AsyncClientNamespace):
    def on_connect(self):
        print("✅ Conectado al servidor de señalización (namespace /)")
        
    def on_disconnect(self):
        
        print("ℹ️ Desconexión transitoria (polling) del servidor")

# Registra el namespace y conecta
sio.register_namespace(SignalingNamespace('/'))

class VideoTrack(MediaStreamTrack):
    kind = "video"
    
    def __init__(self):
        super().__init__()
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set (cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
        if not self.cap.isOpened():
            raise RuntimeError("Error al abrir la cámara")
        self._start = time.time()  
        print("🔥 Cámara inicializada correctamente")
    
    async def recv(self):
        loop = asyncio.get_running_loop()  # optimización: uso de get_running_loop()
        ret, frame = await loop.run_in_executor(None, self.cap.read)
        
        if not ret:
            print("🚨 Error capturando frame")
            return None
        
        #print("📸 Frame capturado correctamente")
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV_I420)
        video_frame = VideoFrame.from_ndarray(frame, format="yuv420p")
        now = time.time()
        video_frame.pts = int((now - self._start) * 90000)
        video_frame.time_base = Fraction(1, 90000)
        return video_frame
    
    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()
            print("📷 Cámara liberada en destructor.")
        cv2.destroyAllWindows()


@sio.on("answer", namespace='/')
async def on_answer(data):
    print("📥 Respuesta recibida")
    
    if not data.get("sdp") or "m=" not in data["sdp"]:
        print("❗ Respuesta SDP inválida, se ignora.")
        return
    if pc and pc.signalingState == "have-local-offer":
        answer = RTCSessionDescription(
            sdp=data["sdp"],
            type=data["type"]
        )
        try:
            await pc.setRemoteDescription(answer)
        except AttributeError as err:
            if "'NoneType' object has no attribute 'media'" in str(err):
                print("❗ SDP answer inválida, se ignora.")
            else:
                raise
    else:
        print("❗ Estado de señalización no permite establecer respuesta.")

@sio.on("candidate", namespace='/')
async def on_candidate(data):
    print("📡 Candidato recibido:", data)
    candidate = candidate_from_sdp(data["candidate"])
    candidate.sdpMid = data["sdpMid"]
    candidate.sdpMLineIndex = data["sdpMLineIndex"]
    await pc.addIceCandidate(candidate)
    

@sio.on("renegotiate", namespace='/')
async def on_renegotiate(data):
    global pc
    print("Renegociación solicitada por nuevo cliente.")
    if pc is None or pc.signalingState == "closed":
        print("RTCPeerConnection está cerrado, reinicializando...")
        pc = createPeerConnection()
    else:
        print("Renegociación: reiniciando ICE en conexión existente")
        await pc.restartIce()
    offer = await pc.createOffer()
    await pc.setLocalDescription(offer)
    await sio.emit("offer", {
         "offer": {
           "sdp": pc.localDescription.sdp,
           "type": pc.localDescription.type
         },
         "room": ROOM_ID,
         "jetson": True
    }, namespace='/')

def procesar_mensaje(mensaje):
    match mensaje:
        case "x_R":
            print("Moviendo cámara a la derecha")
        case "x_L":
            print("Moviendo cámara a la izquierda")
        case "y_R":
            print("Moviendo cámara hacia arriba")
        case "y_L":
            print("Moviendo cámara hacia abajo")
        case "z_R":
            print("Haciendo zoom in")
        case "z_L":
            print("Haciendo zoom out")
        case "turn on":
            print("Encendiendo la cámara")
        case "1":
            print("Modo 1 activado")
        case "2":
            print("Modo 2 activado")
        case "3":
            print("Modo 3 activado")
        case _:
            print(f"Mensaje no reconocido: {mensaje}")

def on_control_message(msg):
#Captura de mensajes en el canal de datos
    received_messages.append(msg)
    # Imprimir mensaje capturado, funcion por el momento 
    print("Mensaje capturado:", msg)
    procesar_mensaje(msg)

def createPeerConnection():
    global control_channel
    config = RTCConfiguration(iceServers=[RTCIceServer(urls="stun:stun.l.google.com:19302")])
    pc_new = RTCPeerConnection(configuration=config)
    
    pc_new.oniceconnectionstatechange = lambda: print(f"ICE state (jetson): {pc_new.iceConnectionState}")
    pc_new.addTrack(VideoTrack())
    # Crear canal de datos "control"
    control_channel = pc_new.createDataChannel("control")
    control_channel.on("open", lambda: print("Canal de datos 'control' abierto"))
    # Asignar handler para capturar mensajes en la lista
    control_channel.on("message", on_control_message)
    
    return pc_new

async def main():
    global pc
    try:
        await sio.connect(f"http://{ip}:5000", transports=["websocket"], namespaces=['/'], wait_timeout=3)
        await sio.emit("join", {"room": ROOM_ID}, namespace='/')
        
        pc = createPeerConnection()
        # Crear oferta inicial
        offer = await pc.createOffer()
        await pc.setLocalDescription(offer)
        await sio.emit("offer", {
            "offer": {
                "sdp": pc.localDescription.sdp,
                "type": pc.localDescription.type
            },
            "room": ROOM_ID,
            "jetson": True
        }, namespace='/')
        
        while True:
            await asyncio.sleep(1)
    finally:
        await sio.disconnect()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🔌 Conexión cerrada")
        sio.disconnect()