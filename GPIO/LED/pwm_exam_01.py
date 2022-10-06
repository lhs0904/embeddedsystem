import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# 불필요한 warning 제거
GPIO.setwarnings(False)

led_pin1 = 23
led_pin2 = 24

GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

pwm1 = GPIO.PWM(led_pin1, 1.0)
pwm1.start(50)
pwm2 = GPIO.PWM(led_pin2, 1.0)
pwm2.start(50)

try:
    while True:
        pass

except KeyboardInterrupt:
    pass

pwm1.stop()
pwm1.stop()

GPIO.cleanup()
