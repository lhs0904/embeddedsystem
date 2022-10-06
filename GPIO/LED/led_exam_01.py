# Created on Heesung의 iPad.

#필요한 모듈을 불러 옵니다.
import RPi.GPIO as GPIO
import time

# 사용할 GPIO핀의 번호를 선정합니다.(BCM 모드)
led_pin1 = 23 #GPIO23
led_pin2 = 24 #GPIO24

# 불필요한 warning 제거
GPIO.setwarnings(False)

#GPIO핀의 번호 모드 설정
GPIO.setmode(GPIO.BCM)

# LED 핀의 IN/OUT 설정
GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

# LED1, LED2 ON
GPIO.output(led_pin1, True)
GPIO.output(led_pin2, True)

time.sleep(2.0) # 2.0초 대기

# LED1, LED2 OFF
GPIO.output(led_pin1, False)
GPIO.output(led_pin2, False)

# GPIO 핀 상태 초기화
GPIO.cleanup()