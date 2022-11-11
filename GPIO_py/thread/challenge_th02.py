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
pwm_servo.start(2.5)

def t1_sub_led():
    while True:
        for t_high in range(0, 101):
            pwm2.ChangeDutyCycle(t_high)
            time.sleep(0.01)
        for t_high in range(100, -1, -1):
            pwm2.ChangeDutyCycle(t_high)
            time.sleep(0.01)
        if flag_exit: break

def t2_sub_servo():
    while True:
        for angle in range(0, 181):
            pwm_servo.ChangeDutyCycle(2.5+10.5*angle/180)
            time.sleep(0.01)
        for angle in range(180, -1, -1):
            pwm_servo.ChangeDutyCycle(2.5+10.5*angle/180)
            time.sleep(0.01)
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
pwm1.stop()
pwm2.stop()
pwm_servo.stop()
GPIO.cleanup()