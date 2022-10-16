#-*- coding: utf-8 -*-

#필요한 모듈을 불러 옵니다.
import RPi.GPIO as GPIO
import time

# 사용할 GPIO핀의 번호를 선정합니다.(BCM 모드)
led_pin = 4 #GPIO 4

# 불필요한 warning 제거
GPIO.setwarnings(False)

#GPIO핀의 번호 모드 설정
GPIO.setmode(GPIO.BCM)

# LED 핀의 IN/OUT 설정
GPIO.setup(led_pin, GPIO.OUT)

#10번 반복
for i in range(10):
    GPIO.output(led_pin, 1) # LED ON
    time.sleep(1) # 1초 동안 대기상태
    GPIO.output(led_pin, 0) # LED OFF
    time.sleep(1) # GPIO 설정 초기화
GPIO.cleanup()