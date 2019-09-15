from flask import Flask, request, Response, render_template, session
from flask_socketio import SocketIO, emit, join_room, disconnect
from threading import Thread, Timer
# import api.cameraCV
from socket import *


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
thread = None


@app.route('/')
def index():
    # global thread
    # if thread is None:
    #     thread = Thread(target=background_stuff)
    #     thread.start()
    return render_template('index.html')


@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected', 'count': 0})


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


@socketio.on('message')
def handle_message(message):
    print(message)
    emit('message', { 'content': 'You are connected!', 'importance': '1' })

@socketio.on('json')
def handle_json(json):
    print(json)
    emit('message', { 'content': 'You are connected!', 'importance': '1' })

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))

def sendEmotion(emotion):
    socketio.emit('emotion', {'data': emotion}, namespace='/test')

    # print(socketio.emit('emotion', { 'emotion': emotion }))

def sendName(name):
    socketio.emit('name', { 'name': name }, namespace='/test')

def sendSong(songId):
    socketio.emit('song', { 'song': songId })
#
def startCamera():
    api.cameraCV.runCV(sendEmotion)

def startServer():
    socketio.run(app)

def startServer(flag):
    pass
    # print("-- Starting Server Receive --")
    # while True:
    #     message, clientAddress = ringoSocket.recvfrom(max_buffer_size)
    #     handleReceive(message, clientAddress)

def startRingoServer():
    ringoSocket = socket(AF_INET, SOCK_DGRAM)
    ringoSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    pocRingo = ("127.0.0.1", 3000)
    ringoSocket.bind(pocRingo)
    while True:
        print("h")
        message, clientAddress = ringoSocket.recvfrom(2048)
        sendEmotion(message)
        print(message)

if __name__ == '__main__':
    # socketio.run(app)
    Thread(target=startRingoServer).start()
    socketio.run(app)

    # startCamera()
    # startRingoServer()
