import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

button_pin = 18
led_pin1 = 23
led_pin2 = 24
GPIO.setup(button_pin, GPIO.IN)
GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

buttonInputPrev = False
ledOn = False

try:
    while True:
        buttonInputPrev = GPIO.input(button_pin)
        if buttoninput and not buttonInputPrev:
            print("rising edge")
            ledOn = True if not ledOn else False
            GPIO.output(led_pin1, ledOn)
            GPIO.output(led_pin2, ledOn)

        elif not buttonInput and buttonInputPrev:
            print("falling edge")

        else: pass

        buttonInputPrev = buttonInput

except KeyboardInterrupt:
    pass

GPIO.cleanup()