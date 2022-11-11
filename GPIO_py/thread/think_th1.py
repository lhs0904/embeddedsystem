import RPi.GPIO as GPIO
import threading
import time

led_pin1 = 23
led_pin2 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

GPIO.output(led_pin1, False)
GPIO.output(led_pin2, False)

flag_exit = False
pwm1 = GPIO.PWM(led_pin1, 1000.0)
pwm1.start(0.0)
pwm2 = GPIO.PWM(led_pin2, 1000.0)
pwm2.start(0.0)

def t1_sub_led():
    while True:
        for t_high in range(0, 101):
            pwm2.ChangeDutyCycle(t_high)
            time.sleep(0.015)
        for t_high in range(100, -1, -1):
            pwm2.ChangeDutyCycle(t_high)
            time.sleep(0.015)
        if flag_exit: break

t1 = threading.Thread(target=t1_sub_led)
t1.start()

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
pwm1.stop()
pwm2.stop()
GPIO.cleanup()