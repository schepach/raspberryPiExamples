import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

blueArray = [14, 12, 10, 15, 26, 18, 21, 24, 17]
yellowArray = [19, 16, 13]
txt = 'iteration #{0}'

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

for x in range(3):
   GPIO.output(blueArray,GPIO.HIGH)
   GPIO.output(yellowArray,GPIO.HIGH)
   time.sleep(0.5)
   GPIO.output(blueArray,GPIO.LOW)
   GPIO.output(yellowArray,GPIO.LOW)
   time.sleep(0.5)
   print(txt.format(x))

GPIO.output(blueArray,GPIO.HIGH)
GPIO.output(yellowArray,GPIO.HIGH)
print('Wait 3 seconds...')
time.sleep(3)

print('Stop check lights...')
GPIO.cleanup()

#13, 19, 16 - yellow
#14, 15, 17, 10, 24, 18, 21, 12, 26 - blue