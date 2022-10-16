# Created on Heesung의 iPad.

import RPi.GPIO as GPIO
import time

led_pin1 = 23
led_pin2 = 24

GPIO.setwarnings(False)
GPIO.setmode(BCM)

GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

try:
    while True:
        userInput = input("n: LED ON, m: LED OFF\n")
        print(userInput)

        if userInput == "n":
            GPIO.output(led_pin1, GPIO.HIGH)
            GPIO.output(led_pin2, GPIO.HIGH)
        elif userInput == "m":
            GPIO.output(led_pin1, GPIO.LOW)
            GPIO.output(led_pin2, GPIO.LOW)
except KeyboardInterrupt:
    pass

GPIO.cleanup()