import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

def led2():
    led_pin1 = 23
    led_pin2 = 24


    GPIO.setup(led_pin1, GPIO.OUT)
    GPIO.setup(led_pin2, GPIO.OUT)

    pwm1 = GPIO.PWM(led_pin1, 1000)
    pwm1.start(0)
    pwm2 = GPIO.PWM(led_pin2, 1000)
    pwm2.start(0)

    while True:
        userInput = input("Brightness 0%: 0, 50%: 5, 100%: f \n")
        print(userInput)
        if userInput == "0":
            pwm1.ChangeDutyCycle(0)
            pwm2.ChangeDutyCycle(0)
        elif userInput == "5":
            pwm1.ChangeDutyCycle(50)
            pwm2.ChangeDutyCycle(50)
        elif userInput == "t":
            pwm1.ChangeDutyCycle(100)
            pwm2.ChangeDutyCycle(100)
