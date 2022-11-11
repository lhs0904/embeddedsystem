import threading
import time

shared_number = 0
lock_1 = threading.Lock() #lock_1 객체 생성(threading 모듈 하위 Lock 클래스를 활용)

def thread01():
    global shared_number
    lock_1.acquire() # 자물쇠 잠금
    for i in range(3):
        print(f" thread_01 count: {i}, shared number : {shared_number}")
        time.sleep(1)
        shared_number += 1
    lock_1.release() # 자물쇠 해제

def thread02():
    global shared_number
    lock_1.acquire() # 자물쇠 잠금
    for j in range(3):
        print(f"\t thread_02 count: {j}, shared number: {shared_number}")
        time.sleep(1)
        shared_number += 1
    lock_1.release() # 자물쇠 해제

thread01 = threading.Thread(target = thread01)
thread01.start()
thread02 = threading.Thread(target = thread02)
thread02.start()