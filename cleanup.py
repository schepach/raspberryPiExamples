import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

blue_array = [14, 15, 17, 10, 24, 18, 21, 12, 26]
yellow_array = [13, 19, 16]

GPIO.setup(blue_array, GPIO.OUT)
GPIO.output(blue_array, GPIO.HIGH)
time.sleep(3)
GPIO.output(blue_array, GPIO.LOW)

GPIO.setup(yellow_array, GPIO.OUT)
GPIO.output(yellow_array, GPIO.HIGH)
time.sleep(3)
GPIO.output(yellow_array, GPIO.LOW)

print('Cleanup is done...')

GPIO.cleanup()