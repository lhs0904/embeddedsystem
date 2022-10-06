# Created on Heesung의 iPad.

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(BCM)

led_pin1 = 23
led_pin2 = 24

GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

pwm1 = GPIO.PWM(led_pin1, 50)
pwm1.start(0)
pwm2 = GPIO.PWM(led_pin2, 50)
pwm2.start(0)

try:
    while True:
        userInput = input("0: 0%, 5: 50%, f: 100%\n")
        print(userInput)

        if userInput == "0":
            pwm1.ChangeDutyCycle(0)
            pwm2.ChangeDutyCycle(0)
        elif userInput == "5":
            pwm1.ChangeDutyCycle(50)
            pwm2.ChangeDutyCycle(50)
        elif userInput == "f":
            pwm1.ChangeDutyCycle(100)
            pwm2.ChangeDutyCycle(100)
except KeyboardInterrupt:
    pass

pwm1.stop()
pwm2.stop()
GPIO.cleanup()
