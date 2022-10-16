import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led_pin1 = 23
led_pin2 = 24
sw = 18
servo = 16
buzzer_pin = 25

GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)
GPIO.setup(servo, GPIO.OUT)
GPIO.setup(buzzer_pin, GPIO.OUT)

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
        time.sleep(t)

    def moveB(self, x=0, t=0):
        GPIO.output(self.Inx, GPIO.HIGH)
        GPIO.output(self.Iny, GPIO.LOW)
        self.pwm.ChangeDutyCycle(x)
        time.sleep(t)

    def stop(self, t):
        self.pwm.ChangeDutyCycle(0)
        time.sleep(t)

motorA = DCmotor(26, 19, 13)
motorB = DCmotor(22, 5, 6)

melody = [262, 294, 330, 349, 392, 440, 494, 523]
keys = ["a", "s", "d", "f", "g", "h", "j", "k"]

pwm1 = GPIO.PWM(buzzer_pin, 100)
pwm1.start(0)
pwm2 = GPIO.PWM(servo, 100)
pwm2.start(2.5)

try:
    while(True):
        userInput = input("n:LED on, m:LED off, q: servo 60~120, w: servo 30~150, e: servo 0~180, t:DC moveF, b: DC moveB\n")
        print(userInput)

        for note in range(0, len(keys)):
            if userInput == keys[note]:
                pwm1.ChangeFrequency(melody[note])
                pwm1.ChangeDutyCycle(50.0)
                time.sleep(0.5)
                pwm1.ChangeDutyCycle(0.0)
                break
        if userInput == "n":
            GPIO.output(led_pin1, True)
            GPIO.output(led_pin2, True)
        elif userInput == "m":
            GPIO.output(led_pin1, False)
            GPIO.output(led_pin2, False)
        elif userInput == "q":
            while(True):
                pwm2.ChangeDutyCycle(9.6)
                time.sleep(0.5)
                pwm2.ChangeDutyCycle(16.3)
                time.sleep(0.5)
        elif userInput == "w":
            while(True):
                pwm2.ChangeDutyCycle(6.3)
                time.sleep(0.5)
                pwm2.ChangeDutyCycle(19.6)
                time.sleep(0.5)
        elif userInput == "e":
            while(True):
                pwm2.ChangeDutyCycle(3.0)
                time.sleep(0.5)
                pwm2.ChangeDutyCycle(23.0)
                time.sleep(0.5)

        elif userInput == "t":
            motorA.moveF(100, 2)
            motorB.moveF(100, 2)
            motorA.stop(1)
            motorB.stop(1)
        elif userInput == "b":
            motorA.moveB(100, 2)
            motorB.moveB(100, 2)
            motorA.stop(1)
            motorB.stop(1)

except KeyboardInterrupt:
    pass

pwm1.stop()
pwm2.stop()

GPIO.cleanup()