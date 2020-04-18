import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

pwm = GPIO.PWM(18,1000)
dutyCycle = 50
pwm.start(dutyCycle)

while(True):
    print('dutyCycle {}'.format(dutyCycle))
    time.sleep(0.01)
    dutyCycle += 1

    if (dutyCycle) > 100:
        dutyCycle = 0
    pwm.ChangeDutyCycle(dutyCycle)