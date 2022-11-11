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
userInput = 0
shared_number = 0
pwm_servo = GPIO.PWM(servo, 50.0)
pwm_servo.start(2.5)
motorA = DCmotor(26, 19, 13)
lock_1 = threading.Lock()

def t1_sub_led():
    while True:
        global shared_number
        global userInput
        if userInput == "l":
            for i in range(3):
                GPIO.output(led_pin1, GPIO.HIGH)
                time.sleep(1)
                lock_1.acquire()
                shared_number+=1
                lock_1.release()
                print(f"HW action count : {shared_number}")
                GPIO.output(led_pin1, GPIO.LOW)
                time.sleep(1)
                lock_1.acquire()
                shared_number+=1
                lock_1.release()
                print(f"HW action count : {shared_number}")
        elif flag_exit: break
               
def t2_sub_servo():
    while True:
        global shared_number
        global userInput
        if userInput == "s":
            for angle in range(0, 181):
                pwm_servo.ChangeDutyCycle((2.5)+(10.5)*angle/180)
                time.sleep(0.01)
            lock_1.acquire()
            shared_number+=1
            lock_1.release()
            print(f"HW action count : {shared_number}")
            for angle in range(180, -1, -1):
                pwm_servo.ChangeDutyCycle((2.5)+(10.5)*angle/180)
                time.sleep(0.01)
            lock_1.acquire()
            shared_number+=1
            lock_1.release()
            print(f"HW action count : {shared_number}")
        elif flag_exit: break
    
def t3_sub_dcmotor():
    while True:
        global shared_number
        global userInput
        if userInput == "d":
            for j in range(3):
                motorA.moveF(100, 1)
                lock_1.acquire()
                shared_number+=1
                lock_1.release()
                print(f"HW action count : {shared_number}")
                motorA.stop(1)
                lock_1.acquire()
                shared_number+=1
                lock_1.release()
                print(f"HW action count : {shared_number}")
        elif flag_exit: break

t1 = threading.Thread(target=t1_sub_led)
t1.start()
t2 = threading.Thread(target=t2_sub_servo)
t2.start()
t3 = threading.Thread(target=t3_sub_dcmotor)
t3.start()

try:
    while True:
        userInput = input("l: led, s:servo, d:dcmotor\n")
        print(userInput)
        time.sleep(0.1)
except KeyboardInterrupt:
    pass

flag_exit = True
pwm_servo.stop()
GPIO.cleanup()