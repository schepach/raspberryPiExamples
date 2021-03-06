import RPi.GPIO as GPIO
import time


def is_pressed(btn, led):
    state = GPIO.input(btn)
#   print('state = {}'.format(state))
    GPIO.output(led, state)


buttons = [2, 3, 4, 8]
leds = [14, 15, 18, 24]
len_elems = len(buttons)

GPIO.setmode(GPIO.BCM)

for i in range(len_elems):
    print("Couple: button {0} and  led {1}".format(buttons[i], leds[i]))
    GPIO.setup(leds[i], GPIO.OUT)
    GPIO.setup(buttons[i], GPIO.IN)

while(True):
    if (GPIO.input(buttons[0]) == 0
        and GPIO.input(buttons[1]) == 0
        and GPIO.input(buttons[2]) == 0
            and GPIO.input(buttons[3]) == 0):
        print('Break, because all buttons was pressed')
        break

    for i in range(len_elems):
        is_pressed(buttons[i], leds[i])

print('Cleanup...')
GPIO.cleanup()
