from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room  # <-- add import
from flask_cors import CORS
import eventlet
import ssl
app = Flask(__name__)

socketio = SocketIO(
    app,
    cors_allowed_origins="*",
    async_mode="eventlet"  # Cambiado a eventlet para habilitar WebSocket
    
)
CORS(app, resources={r"/*": {"origins": "*"}})

# Almacenamiento de ofertas y candidatos ICE
temp_rooms = {}

# Declarar global para identificar al cliente jetson
jets_id = None

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('offer', namespace='/')
def handle_offer(data):
    global jets_id
    room = data.get('room')
    if room not in temp_rooms:
        temp_rooms[room] = {}
    temp_rooms[room]['offer'] = data['offer']
    # Si la oferta viene de jetson, guardamos su SID
    if data.get("jetson"):
        jets_id = request.sid
    print(f"📩 Oferta recibida (SDP snippet): {data['offer']['sdp'][:100]}...")
    emit('offer', data['offer'], room=data['room'], namespace='/')

@socketio.on('answer', namespace='/')
def handle_answer(data):
    room = data.get('room')
    if room not in temp_rooms:
        temp_rooms[room] = {}
    temp_rooms[room]['answer'] = data['answer']
    print(f"✅ Respuesta recibida en {room}")
    emit('answer', data['answer'], room=room, namespace='/') 

@socketio.on('candidate', namespace='/')
def handle_candidate(data):
    room = data.get('room')
    if room not in temp_rooms:
        temp_rooms[room] = {}
    if 'candidates' not in temp_rooms[room]:
        temp_rooms[room]['candidates'] = []
    temp_rooms[room]['candidates'].append(data['candidate'])
    print(f"📡 Candidato ICE recibido en {room}")
    emit('candidate', data['candidate'], room=room, namespace='/') 
    
@socketio.on('join',  namespace='/')
def handle_join(data):
    room = data.get('room')
    join_room(room)
    print(f"👤 Cliente unido a {room}")
    if room in temp_rooms:
        if 'offer' in temp_rooms[room]:
            emit('offer', temp_rooms[room]['offer'], room=request.sid, namespace='/')
        if 'candidates' in temp_rooms[room]:
            for candidate in temp_rooms[room]['candidates']:
                emit('candidate', candidate, room=request.sid, namespace='/')
    # Si el cliente que se conecta no es el jetson, solicitar renegociación al jetson
    if jets_id and request.sid != jets_id:
        emit('renegotiate', {}, room=jets_id, namespace='/')

@socketio.on('leave', namespace='/')
def handle_leave(data):
    room = data.get('room')
    leave_room(room)
    if room in temp_rooms:
        temp_rooms[room]['candidates'] = []  
    print(f"👤 Cliente salió de {room}, limpiando candidatos.")

if __name__ == '__main__':
    # For development without SSL, use plain HTTP:
    listener = eventlet.listen(('0.0.0.0', 5000))
    eventlet.wsgi.server(listener, app)

   
    # context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    # context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')
    # listener = eventlet.listen(('0.0.0.0', 5000))
    # ssl_listener = eventlet.wrap_ssl(listener, certfile='cert.pem', keyfile='key.pem', server_side=True)
    # eventlet.wsgi.server(ssl_listener, app)