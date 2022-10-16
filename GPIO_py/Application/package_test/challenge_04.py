import RPi.GPIO as GPIO
import time


def servo():
    servo_pin = 16
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo_pin, GPIO.OUT)

    pwm = GPIO.PWM(servo_pin, 50)
    pwm.start(2.5)
    while True:
        userInput = input("angle 0: q, angle 90: w, angle 180: e \n")
        if userInput == "q":
            pwm.ChangeDutyCycle(2.5)
        elif userInput == "w":
            pwm.ChangeDutyCycle(7.75)
        elif userInput == "e":
            pwm.ChangeDutyCycle(12.5)

    time.sleep(1.0)
    pwm.ChangeDutyCycle(0.0)

    pwm.ChangeDutyCycle(2.5)
    time.sleep(1.0)
    pwm.ChangeDutyCycle(0.0)

    pwm.stop()