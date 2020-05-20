import time
import RPi.GPIO as GPIO
from flask import Flask, send_file

# configure led
GPIO.setmode(GPIO.BCM)
led = 18
GPIO.setup(18, GPIO.OUT)

app = Flask('lightControl')


@app.route('/')
def index():
    return send_file('light.html')


@app.route('/images/<filename>')
def get_image(file_name):
    return send_file('images/' + file_name)


@app.route('/turn<state>')
def turn(state):
    print("State is {0}".format(state))
    if (state == 'On'):
        GPIO.output(led, GPIO.HIGH)
    elif (state == 'Off'):
        GPIO.output(led, GPIO.LOW)
    return 'OK'


app.run(debug=True, port=3000, host='0.0.0.0')