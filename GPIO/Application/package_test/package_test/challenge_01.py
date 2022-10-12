import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def led1():
    led_pin1 = 23
    led_pin2 = 24

    GPIO.setup(led_pin1, GPIO.OUT)
    GPIO.setup(led_pin2, GPIO.OUT)

    GPIO.output(led_pin1, False)
    GPIO.output(led_pin2, False)

    while True:
        userInput = input("LED ON: n, LED OFF: m \n")
        print(userInput)
        if userInput == "n":
            GPIO.output(led_pin1, True)
            GPIO.output(led_pin2, True)
        elif userInput == "m":
            GPIO.output(led_pin1, False)
            GPIO.output(led_pin2, False)