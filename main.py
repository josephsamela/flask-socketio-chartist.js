from flask import Flask, render_template
from flask_socketio import SocketIO, send
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dreamchaser'
socketio = SocketIO(app)

@app.route("/")
def index():
    messages = ["message1", "message2", "message3", "message4", "message5", "message6", "message7", "message8", "message9", "message10"]
    return render_template("index.html", messages=messages)

@socketio.on('message')
def handle_message(message):
    print(message)
    send(message, broadcast=True)

if __name__ == '__main__':
    PORT = json.load(open('config.json'))["PORT"]
    socketio.run(app, host='0.0.0.0', port=PORT)
