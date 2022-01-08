import RPi.GPIO as GPIO
import time

sw_pin = 15

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(sw_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while 1: #무한반복
    if GPIO.input(sw_pin) == HIGH:  # 스위치를 누르면
        print("The Switch is pushed!")  # 해당 문장 출력
    time.sleep(0.1)
GPIO.cleanup()