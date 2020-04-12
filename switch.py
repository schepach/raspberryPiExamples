import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(8,GPIO.IN) #button
GPIO.setup(4,GPIO.IN) #stop button
GPIO.setup(24,GPIO.OUT) #light
GPIO.setup(26,GPIO.OUT) #light

print('Read this manual:')
print('Press button 8 and the light will be change')
print('Press button 4 for stop program')
print('After 15 second the infinite lopp is start...')

time.sleep(15)

while (GPIO.input(4) == 1):
    button = GPIO.input(8)
    if (button == 0):
        print('light 24 ON and light 26 OFF')
        GPIO.output(24,GPIO.HIGH)
        GPIO.output(26,GPIO.LOW)
    else:
        print('light 26 ON and light 24 OFF')
        GPIO.output(26,GPIO.HIGH)
        GPIO.output(24,GPIO.LOW)

print('Stop the program and low the lights')
arrayLights = [24,26]
GPIO.output(arrayLights,GPIO.LOW)

GPIO.cleanup()