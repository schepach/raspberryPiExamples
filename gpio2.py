import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

blue_array = [14, 12, 10, 15, 26, 18, 21, 24, 17]
yellow_array = [19, 16, 13]
txt = 'iteration #{0}'

for i in blue_array:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(i, GPIO.LOW)

for j in yellow_array:
    GPIO.setup(j, GPIO.OUT)
    GPIO.output(j, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(j, GPIO.LOW)

for x in range(3):
    GPIO.output(blue_array, GPIO.HIGH)
    GPIO.output(yellow_array, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(blue_array, GPIO.LOW)
    GPIO.output(yellow_array, GPIO.LOW)
    time.sleep(0.5)
    print(txt.format(x))

GPIO.output(blue_array, GPIO.HIGH)
GPIO.output(yellow_array, GPIO.HIGH)
print('Wait 3 seconds...')
time.sleep(3)

print('Stop check lights...')
GPIO.cleanup()

#13, 19, 16 - yellow
#14, 15, 17, 10, 24, 18, 21, 12, 26 - blue