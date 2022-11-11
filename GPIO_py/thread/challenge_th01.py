import RPi.GPIO as GPIO
import threading
import time

led_pin1 = 23
led_pin2 = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

GPIO.output(led_pin1, False)
GPIO.output(led_pin2, False)

flag_exit = False

def t1_sub_led():
    while True:
        GPIO.output(led_pin2, True)
        time.sleep(1.7)
        GPIO.output(led_pin2, False)
        time.sleep(1.7)
        if flag_exit: break

t1 = threading.Thread(target=t1_sub_led)
t1.start()

try:
    while True:
        GPIO.output(led_pin1, True)
        time.sleep(0.7)
        GPIO.output(led_pin1, False)
        time.sleep(0.7)
except KeyboardInterrupt:
    pass

flag_exit = True
t1.join()
GPIO.cleanup()