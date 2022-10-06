# Created on Heesung의 iPad.

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
buzzer_pin = 25

GPIO.setup(buzzer_pin, GPIO.OUT)

pwm = GPIO.PWM(buzzer_pin, 262)
pwm.start(50.0)

time.sleep(2.0)
pwm.ChangeDutyCycle(0.0)

pwm.stop()
GPIO.cleanup()
print ('Program end')
