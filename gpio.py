import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

blueArray = [14, 15, 17, 10, 24, 18, 21, 12, 26]
yellowArray = [13, 19, 16]

for i in blueArray:
   GPIO.setup(i,GPIO.OUT)
   GPIO.output(i,GPIO.HIGH)
   time.sleep(0.5)
   GPIO.output(i,GPIO.LOW)

for j in yellowArray:
   GPIO.setup(j,GPIO.OUT)
   GPIO.output(j,GPIO.HIGH)
   time.sleep(0.5)
   GPIO.output(j,GPIO.LOW)
   time.sleep(0.5)
   GPIO.output(j,GPIO.HIGH)
   time.sleep(0.5)
   GPIO.output(j,GPIO.LOW)

print('Stop check lights...')

GPIO.cleanup()

#13, 19, 16 - yellow
#14, 15, 17, 10, 24, 18, 21, 12, 26 - blue