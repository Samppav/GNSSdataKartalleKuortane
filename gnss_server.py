import json
from flask import Flask, render_template, request, Response
from flask_cors import CORS, cross_origin # pip install flask-cors
from flask_socketio import SocketIO, emit
app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
socketio = SocketIO(app, cors_allowed_origins="*")

coordinates = []

@cross_origin()
@app.route('/')
def get_all_measurements_map():
    return render_template('seinajoki.html')


@cross_origin()
@app.route('/api/coordinates')
def get_all_measurements():
    return(json.dumps(coordinates))            

@cross_origin()
@app.route('/uusimittaus', methods = ['POST'])
def new_measurement():
    p = request.get_json(force=True)
    coordinates.append(p)
    x = json.dumps(p, indent=True)
    coordinatesjson = json.dumps(coordinates, indent=True)
    socketio.emit('position', {'data': x})
    return x

if __name__ == '__main__':
   socketio.run(app)