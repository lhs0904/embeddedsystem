import RPi.GPIO as GPIO
import threading
import time

led_pin1 = 23
led_pin2 = 24
servo = 16

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)
GPIO.setup(servo, GPIO.OUT)

GPIO.output(led_pin1, False)
GPIO.output(led_pin2, False)

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
        GPIO.output(self.Inx, GPIO.HIGH)
        GPIO.output(self.Iny, GPIO.LOW) #direction setup forward
        self.pwm.ChangeDutyCycle(x) #speed control
        time.sleep(t)
        
    def moveB(self, x=0, t=0):
        GPIO.output(self.Inx, GPIO.LOW)
        GPIO.output(self.Iny, GPIO.HIGH) #direction setup reverse
        self.pwm.ChangeDutyCycle(x) #speed control
        time.sleep(t)
        
    def stop(self, t=0):
        self.pwm.ChangeDutyCycle(0)
        time.sleep(t)

flag_exit = False
userInput = False
pwm1 = GPIO.PWM(led_pin1, 1000.0)
pwm1.start(0.0)
pwm2 = GPIO.PWM(led_pin2, 1000.0)
pwm2.start(0.0)
pwm_servo = GPIO.PWM(servo, 50.0)
pwm_servo.start(3.0)
motorA = DCmotor(26, 19, 13)

def t1_sub_led():
    while True:
        for t_high in range(0, 101):
            pwm2.ChangeDutyCycle(t_high)
            time.sleep(0.015)
        for t_high in range(100, -1, -1):
            pwm2.ChangeDutyCycle(t_high)
            time.sleep(0.015)
        if flag_exit: break

def t2_sub_servo():
    while True:
        global userInput
        if userInput == "q":
            for angle in range(60, 121):
                pwm_servo.ChangeDutyCycle(3+10*angle/180)
                time.sleep(0.01)
            for angle in range(120, 60, -1):
                pwm_servo.ChangeDutyCycle(3+10*angle/180)
                time.sleep(0.01)
        elif userInput == "w":
            for angle in range(30, 151):
                pwm_servo.ChangeDutyCycle(3+10*angle/180)
                time.sleep(0.01)
            for angle in range(150, 29, -1):
                pwm_servo.ChangeDutyCycle(3+10*angle/180)
                time.sleep(0.01)
        elif userInput == "e":
            for angle in range(0, 181):
                pwm_servo.ChangeDutyCycle(3+10*angle/180)
                time.sleep(0.01)
            for angle in range(180, -1, -1):
                pwm_servo.ChangeDutyCycle(3+10*angle/180)
                time.sleep(0.01)
        time.sleep(1.0)
        pwm_servo.ChangeDutyCycle(0.0)
        if flag_exit: break

def t3_userInput():
    while True:
        global userInput
        userInput = input("q:60 -> 120, w: 30 -> 150, e: 0 ->180, t: forward, b: reverse\n")
        print(userInput)
        time.sleep(0.1)

def t4_sub_dcmotor():
    while True:
        if userInput == "t":
            motorA.moveF(100, 1)
            motorA.stop(1)
        elif userInput == "b":
            motorA.moveB(100, 1)
            motorA.stop(1)

t1 = threading.Thread(target=t1_sub_led)
t1.start()
t2 = threading.Thread(target=t2_sub_servo)
t2.start()
t3 = threading.Thread(target=t3_userInput)
t3.start()
t4 = threading.Thread(target=t4_sub_dcmotor)
t4.start()

try:
    while True:
        for t_high in range(0, 101):
            pwm1.ChangeDutyCycle(t_high)
            time.sleep(0.005)
        for t_high in range(100, -1, -1):
            pwm1.ChangeDutyCycle(t_high)
            time.sleep(0.005)
        if flag_exit: break
except KeyboardInterrupt:
    pass

flag_exit = True
t1.join()
t2.join()
pwm1.stop()
pwm2.stop()
pwm_servo.stop()
motorA.pwm.stop()
GPIO.cleanup()