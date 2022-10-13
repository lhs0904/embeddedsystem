import RPi.GPIO as GPIO
import time

# 코드 실행시 불필요한 warning 제거
GPIO.setwarnings(False)

# BCM번호 기준으로 라즈베리파이 핀 제어
GPIO.setmode(GPIO.BCM)

# GPIO14에 LED 연결
LED = 14

# LED를 연결한 14번 핀을 OUT모드로 사용하도록 설정
GPIO.setup(LED, GPIO.OUT)

pwm = GPIO.PWM(LED, 50)
pwm.start(0)

try:
	while 1:
		for i in range(0, 101):
			pwm.ChangeDutyCycle(i)
			time.sleep(0.1)
			pwm.ChangeDutyCycle(0)
			
		for j in range(100, -1, -1):
			pwm.ChangeDutyCycle(j)
			time.sleep(0.1)
			
except KeyboardInterrupt:
	pass

#pwm stop
pwm.stop()	
#GPIO 초기화
GPIO.cleanup()
