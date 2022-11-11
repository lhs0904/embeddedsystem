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

flag_exit = False
pwm1 = GPIO.PWM(led_pin1, 1000.0)
pwm1.start(0.0)
pwm2 = GPIO.PWM(led_pin2, 1000.0)
pwm2.start(0.0)
pwm_servo = GPIO.PWM(servo, 50.0)
pwm_servo.start(3.0)

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
        userInput = input("angle 60/120/60: q, angle 30/150/30: w, angle 0/180/0: e \n")
        print(userInput)

        if userInput == "q":
            pwm_servo.ChangeDutyCycle(3+10*60/180) # 60 DEG
            time.sleep(0.5)
            pwm_servo.ChangeDutyCycle(3+10*120/180)
            time.sleep(0.5)
            pwm_servo.ChangeDutyCycle(3+10*60/180)
        elif userInput == "w":
            pwm_servo.ChangeDutyCycle(3+10*30/180) # 60 DEG
            time.sleep(0.5)
            pwm_servo.ChangeDutyCycle(3+10*150/180)
            time.sleep(0.5)
            pwm_servo.ChangeDutyCycle(3+10*30/180)
        elif userInput == "e":
            pwm_servo.ChangeDutyCycle(3+10*0/180) # 60 DEG
            time.sleep(0.5)
            pwm_servo.ChangeDutyCycle(3+10*180/180)
            time.sleep(0.5)
            pwm_servo.ChangeDutyCycle(3+10*0/180)

        time.sleep(1.0)
        pwm_servo.ChangeDutyCycle(0.0)
        if flag_exit: break

t1 = threading.Thread(target=t1_sub_led)
t1.start()
t2 = threading.Thread(target=t2_sub_servo)
t2.start()

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
GPIO.cleanup()