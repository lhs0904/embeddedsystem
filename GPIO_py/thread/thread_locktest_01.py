import threading
import time

shared_number = 0

def thread01():
    global shared_number
    for i in range(0,3):
        print(f" thread_01 count: {i}, shared number : {shared_number}")
        time.sleep(1)
        shared_number += 1

def thread02():
    global shared_number
    for j in range(3):
        print(f"\t thread_02 count: {j}, shared number: {shared_number}")
        time.sleep(1)
        shared_number += 1

thread01 = threading.Thread(target = thread01)
thread01.start()
thread02 = threading.Thread(target = thread02)
thread02.start()