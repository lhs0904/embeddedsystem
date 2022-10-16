# Created on Heesung의 iPad.

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

Ena = 26
In1, In2 = 19, 13

GPIO.setup(Ena, GPIO.OUT)
GPIO.setup(In1, GPIO.OUT)
GPIO.setup(In2, GPIO.OUT)

pwma = GPIO.PWM(Ena, 100)
pwma.start(0)

try:
    while True:
        GPIO.output(In1, GPIO.LOW)
        GPIO.output(In2, GPIO.HIGH)
        pwma.ChangeDutyCycle(50)
        sleep(2)
        GPIO.output(In1, GPIO.HIGH)
        GPIO.output(In2, GPIO.LOW)
        pwma.ChangeDutyCycle(30)
        sleep(2)
except KeyboardInterrupt:
    pass

pwma.stop()
GPIO.cleanup()