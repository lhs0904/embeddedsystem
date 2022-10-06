# Created on Heesung의 iPad.
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(BCM)

class DCmotor():
    def __init__(self, En, Inx, Iny):
        self.En = En
        self.Inx = Inx
        self.Iny = Iny
        GPIO.setup(self.En, GPIO.OUT)
        GPIO.setup(self.Inx, GPIO.OUT)
        GPIO.setup(self.Iny, GPIO.OUT)
        self.pwm = GPIO.PWM(self.En, 100)
        self.pwm.start(0)

    def moveF(self, x=0, t=0):
        GPIO.output(self.Inx, GPIO.LOW)
        GPIO.output(self.Iny, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(x)
        sleep(t)

    def moveB(self, x=0, t=0):
        GPIO.output(self.Inx, GPIO.HIGH)
        GPIO.output(self.Iny, GPIO.LOW)
        self.pwm.ChangeDutyCycle(x)
        sleep(t)

    def stop(self, t=0):
        self.pwm.ChangeDutyCycle(0)
        sleep(t)

motorA = DCmotor(26, 19, 13)

try:
    while True:
        userInput == input("t: forward, b: reverse \n")
        print(userInput)

        if userInput == "t":
            motorA.moveF(100, 1)
            motorA.stop(1)
        elif userInput == "b":
            motorA.moveB(100, 1)
            motorA.stop(1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
