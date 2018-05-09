from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

import json
import time
import random
import threading

# Required for server-side emit() to work
import eventlet
eventlet.monkey_patch()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dreamchaser'
socketio = SocketIO(app)

@app.route("/")
def index():
    title = "Example Chart"
    return render_template("index.html", title=title)

def produce_chart_data():
    while True:
        # Sleep for random duration to prove async working
        time.sleep(0.1)

        # Get some data from source and emit to clients when recieved
        data = get_some_data()

        socketio.emit('new-chart-data', data)
        print("Emit data")

def get_some_data():
    data = {
            "series": [
                {
                    "name": 'Data 1',
                    "data": [
                            {"x": 143134652600, "y": random.random()*10+70},
                            {"x": 143234652600, "y": random.random()*10+70},
                            {"x": 143334652600, "y": random.random()*10+70},
                            {"x": 143434652600, "y": random.random()*10+70},
                            {"x": 143534652600, "y": random.random()*10+70}
                    ]
                }, {
                    "name": 'Data 2',
                    "data": [
                            {"x": 143134652600, "y": random.random()*10+40},
                            {"x": 143234652600, "y": random.random()*10+40},
                            {"x": 143334652600, "y": random.random()*10+40},
                            {"x": 143434652600, "y": random.random()*10+40},
                            {"x": 143534652600, "y": random.random()*10+40}
                    ]
                }, {
                    "name": 'Data 3',
                    "data": [
                            {"x": 143134652600, "y": random.random()*10+25},
                            {"x": 143234652600, "y": random.random()*10+25},
                            {"x": 143334652600, "y": random.random()*10+25},
                            {"x": 143434652600, "y": random.random()*10+25},
                            {"x": 143534652600, "y": random.random()*10+25}
                    ]
                }, {
                    "name": 'Data 3',
                    "data": [
                            {"x": 143134652600, "y": random.random()*10+25},
                            {"x": 143234652600, "y": random.random()*10+25},
                            {"x": 143334652600, "y": random.random()*10+25},
                            {"x": 143434652600, "y": random.random()*10+25},
                            {"x": 143534652600, "y": random.random()*10+25}
                    ]
                }
            ]}
    return data


if __name__ == '__main__':
    t = threading.Thread(target=produce_chart_data)
    t.start()

    PORT = json.load(open('config.json'))["PORT"]
    print("Running on localhost:"+str(PORT))

    socketio.run(app, host='0.0.0.0', port=PORT)
