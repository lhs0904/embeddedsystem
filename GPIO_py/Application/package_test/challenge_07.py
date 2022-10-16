import challenge_01 as c1
import challenge_02 as c2
import challenge_03 as c3
import challenge_04 as c4
import challenge_05 as c5
import RPi.GPIO as GPIO

try:
    while True:
        userinput = input("input keys : \n")
        print(userinput)

        if userinput == "1":
            c1.led1()
        elif userinput == "2":
            c2.led2()
        elif userinput == "3":
            c3.buzzer()
        elif userinput == "4":
            c4.servo()
        elif userinput == "5":
            c5.motor_control()
            
except KeyboardInterrupt:
    pass

GPIO.cleanup()