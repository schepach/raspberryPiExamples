import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

blueArray = [14, 15, 17, 10, 24, 18, 21, 12, 26]
yellowArray = [13, 19, 16]

GPIO.setup(blueArray,GPIO.OUT)
GPIO.output(blueArray,GPIO.HIGH)
time.sleep(3)
GPIO.output(blueArray,GPIO.LOW)

GPIO.setup(yellowArray,GPIO.OUT)
GPIO.output(yellowArray,GPIO.HIGH)
time.sleep(3)
GPIO.output(yellowArray,GPIO.LOW)

print('Cleanup is done...')

GPIO.cleanup()