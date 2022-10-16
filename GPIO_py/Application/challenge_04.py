# Created on Heesung의 iPad.

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(BCM)

servo = 16
GPIO.setup(servo, GPIO.OUT)

pwm = GPIO.PWM(servo, 50)
pwm.start(3.0)

try:
    while True:
        userInput = input("q: 0DEG, w: 90DEG, e: 180DEG\n")
        print(userInput)

        if userInput == 'q':
            pwm.ChangeDutyCycle(3.0)
        elif userInput == 'w':
            pwm.ChangeDutyCycle(7.75)
        elif userInput == 'e':
            pwm.ChangeDutyCycle(12.5)
        
        time.sleep(1)
        pwm.ChangeDutyCycle(0.0)
except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()