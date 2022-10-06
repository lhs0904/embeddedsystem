import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

led_state = False
led_state_Changed = False

def buttonPressed(channel): # event callback 함수 정의
    global led_state
    global led_state_Changed
    led_state = True if not led_state else False # led_state의 상태를 반전
    led_state_Changed = True

button_pin = 18
led_pin1 = 23
led_pin2 = 24

GPIO.setup(button_pin, GPIO.IN)
GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

GPIO.add_event_detect(button_pin, GPIO.RISING)
GPIO.add_event_callback(button_pin, buttonPressed)

try:
    while True:
        if led_state_Changed == True:
            led_state_Changed = False
            GPIO.output(led_pin1, led_state)
            GPIO.output(led_pin2, led_state)
except KeyboardInterrupt:
    pass

GPIO.cleanup()