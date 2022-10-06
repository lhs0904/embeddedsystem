# Created on Heesung의 iPad.

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# 불필요한 warning 제거
GPIO.setwarnings(False)

led_pin1 = 23
led_pin2 = 24

GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

try:
    while True:
        for t_high in range(0, 11):
            cnt = 0 # cnt 변수 선언 후, 0으로 초기화
            while True:
                GPIO.output(led_pin1, True)
                GPIO.output(led_pin2, True)
                time.sleep(t_high * 0.001)
                GPIO.output(led_pin1, False)
                GPIO.output(led_pin2, False)
                time.sleep((10-t_high)*0.001)

                cnt += 1
                if cnt == 10:
                    break

        for t_high in range(10, -1, -1):
            cnt = 0
            while True:
                GPIO.output(led_pin1, True)
                GPIO.output(led_pin2, True)
                time.sleep(t_high * 0.001)
                GPIO.output(led_pin1, False)
                GPIO.output(led_pin2, False)
                time.sleep((10-t_high)*0.001)

                cnt += 1
                if cnt == 10:
                    break
                    
except KeyboardInterrupt:
    pass

GPIO.cleanup()