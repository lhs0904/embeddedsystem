import threading # thread를 사용하기 위한 threading 모듈(변수, 함수, 클라스(메소드)) 임포트
import time

def sub_thread01():
    while True:
        print("\t sub_thread_01 is operating!")
        time.sleep(0.5)

thread01 = threading.Thread(target = sub_thread01) #thread01 객체 생성(Thread 클라스)
thread01.start() #sub_thread01 실행 시작(start() 메소드)

try:
    while True:
        print("main thread is operating!")
        time.sleep(2.0)
except KeyboardInterrupt:
    pass

print("main and sub thread have benn finished!")