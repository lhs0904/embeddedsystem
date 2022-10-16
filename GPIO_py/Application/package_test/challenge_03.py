import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def buzzer():
    buzzer_pin = 25

    GPIO.setup(buzzer_pin, GPIO.OUT)

    pwm = GPIO.PWM(buzzer_pin, 1.0)
    pwm.start(0.0)

    melody = [262, 294, 330, 349, 392, 440, 494, 523]
    keys = ["a", "s", "d", "f", "g", "h", "j", "k"]

    userInput = input("input keys \n")
    print(userInput)
    for note in range(0, len(keys)):
        if userInput == keys[note]:
            pwm.ChangeFrequency(melody[note])
            pwm.ChangeDutyCycle(50.0)
            time.sleep(0.5)
            pwm.ChangeDutyCycle(0.0)
            break

    pwm.stop()