# Created on Heesung의 iPad.
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

servo_pin = 16

GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)
pwm.start(3.0)

for t_high in range(30, 125):
    pwm.ChangeDutyCycle(t_high / 10.0)
    time.sleep(0.02)

for t_high in range(124, 29, -1):
    pwm.ChangeDutyCycle(t_high / 10.0)
    time.sleep(0.02)

pwm.ChangeDutyCycle(3.0)
time.sleep(1.0)

pwm.ChangeDutyCycle(0.0)

pwm.stop()
GPIO.cleanup()