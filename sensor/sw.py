import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED = 14
SW = 2

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
	while True:
		sw_input = GPIO.input(SW)
		print(sw_input)
		GPIO.output(LED, not sw_input)
	
except KeyboardInterrupt:
	pass
	
GPIO.cleanup()
