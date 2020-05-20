import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)

i = 0
while (i < 5):
    i += 1
    time.sleep(0.5)
    GPIO.output(19, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(19, GPIO.LOW)

GPIO.cleanup()
