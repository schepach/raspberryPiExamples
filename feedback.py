import time
import RPi.GPIO as GPIO
from flask import Flask, send_file
from flask_socketio import SocketIO, send, emit

#configure led
GPIO.setmode(GPIO.BCM)
buttons = [2, 3, 4, 8]
leds = [14, 15, 17, 10, 24, 18, 21, 12, 26, 13, 19, 16]

for btn in buttons:
    GPIO.setup(btn, GPIO.IN)

for led in leds:
    GPIO.setup(led,GPIO.OUT)

app = Flask('feedback')
socketio = SocketIO(app)

GPIO.output(leds[1],GPIO.HIGH)

@app.route('/')
def index():
    return send_file('feedback.html')

@app.route('/images/<filename>')
def get_image(filename):
    return send_file('images/' + filename)

#buttons event
@socketio.on('isPressed')
def checkButton(receiveData):
    data = {btn : GPIO.input(btn) for btn in buttons}
    socketio.emit('button', data)

#leds event
@socketio.on('toggle')
def checkLight(toggleData):
    print('toggleData json: {0}'.format(toggleData))
    GPIO.output(toggleData['id'], toggleData['state'])

socketio.run(app, port=3000, host='0.0.0.0')