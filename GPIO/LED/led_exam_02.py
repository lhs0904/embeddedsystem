# Created on Heesung의 iPad.

# 필요한 모듈을 import
import RPi.GPIO as GPIO
import time

# BCM 모드로 셋업
GPIO.setmode(GPIO.BCM)

# 불필요한 warning 제거
GPIO.setwarnings(False)

#LED 핀 번호 설정
led_pin1 = 23
led_pin2 = 24

#LED 핀 출력 포트 설정
GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

# try ~ except 구문 실행 
try:
    while True:
        GPIO.output(led_pin1, True)
        GPIO.output(led_pin2, True)
        time.sleep(0.5)
        GPIO.output(led_pin1, False)
        GPIO.output(led_pin2, False)
        time.sleep(0.5)
except KeyboardInterrupt:
    pass

GPIO.cleanup()