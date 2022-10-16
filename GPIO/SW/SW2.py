import RPi.GPIo as GPIO
import time

sw_pin = 15

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sw_pin, GPIO.IN, pull_up_down=PUD_UP)

GPIO.add_event_detect(sw_pin, GPIO.FALLING, callback=sw_push, bouncetime=300)

def sw_push():
    
