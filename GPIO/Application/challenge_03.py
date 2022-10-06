# Created on Heesung의 iPad.

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(BCM)

buzzer_pin = 25

pwm = GPIO.PWM(buzzer_pin, 1)
pwm.start(0)

melody = [262, 294, 330, 349, 392, 440, 494, 523]
keys = ["a", "s", "d", "f", "g", "h", "j", "k"]
try:
    while True:
        userInput = input("Note(C,D,E,F,G,A,B,C) : a,s,d,f,g,h,j,k\n")
        print(userInput)

        for note in range(0, len(keys)):
            if userInput == keys[note]:
                pwm.ChangeFrequency(melody[note])
                pwm.ChangeDutyCycle(50.0)
                time.sleep(0.5)
                pwm.ChangeDutyCycle(0.0)
                break
except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()
