import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# 불필요한 warning 제거
GPIO.setwarnings(False)

button_pin = 18

GPIO.setup(button_pin, GPIO.IN)

try:
    while True:
        buttonInput = GPIO.input(button_pin)
        print(buttonInput)

except KeyboardInterrupt:
    pass

GPIO.cleanup()