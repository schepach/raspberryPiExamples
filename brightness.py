import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

pwm = GPIO.PWM(18, 1000)
duty_cycle = 50
pwm.start(duty_cycle)

while(True):
    print('duty_cycle {}'.format(duty_cycle))
    time.sleep(0.01)
    duty_cycle += 1

    if (duty_cycle) > 100:
        duty_cycle = 0
    pwm.ChangeDutyCycle(duty_cycle)