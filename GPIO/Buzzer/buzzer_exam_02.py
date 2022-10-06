# Created on Heesung의 iPad.
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
buzzer_pin = 25

GPIO.setup(buzzer_pin, GPIO.OUT)

pwm = GPIO.PWM(buzzer_pin, 1.0)
pwm.start(50.0)

melody = [262, 294, 330, 349, 392, 440, 494, 523]

for note in range(0, 8):
    pwm.ChangeFrequency(melody[note])
    time.sleep(0.5)

pwm.ChangeDutyCycle(0.0)

pwm.stop()
GPIO.cleanup()

