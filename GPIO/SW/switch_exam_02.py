import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# 불필요한 warning 제거
GPIO.setwarnings(False)

button_pin = 18
led_pin1 = 23
led_pin2 = 24

GPIO.setup(button_pin, GPIO.IN)
GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

try:
    while True:
        buttonInput = GPIO.input(button_pin)
        GPIO.output(led_pin1, buttonInput)
        GPIO.output(led_pin2, buttonInput)
except KeyboardInterrupt:
    pass

GPIO.cleanup()