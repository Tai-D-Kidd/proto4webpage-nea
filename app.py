from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import eventlet
#serving a webpage that uses websockets connecions and sneds badk rt responses 'emit()' 



#making flask app
app = Flask(__name__)

#secret key for session management
app.config['SECRET_KEY'] = 'dot.dot.dot.'

#to use websockest for real time changes
socketio= SocketIO(app)

#basic route for homepage
@app.route('/')
def index():
    return render_template('index.html')

#when a user connects
@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('joining', {'message': 'A user has joined'})

#when user sends data
socketio.on('user_event')
def handle_user_event(data):
    print('Received data from user: ',data)
    emit('server_response', {'message': 'Data received'}, broadcast=True)

#running the app
if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0',port=5000)