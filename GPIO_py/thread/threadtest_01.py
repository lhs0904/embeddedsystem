import threading
import time

sub_thread_exit = False

def sub_thread01():
    while True:
        print("\t sub_thread_01 is operating!")
        time.sleep(0.5)
        if sub_thread_exit: break

thread01 = threading.Thread(target = sub_thread01)
thread01.start()

try:
    while True:
        print("main thread is operating!")
        time.sleep(2.0)
except KeyboardInterrupt:
    pass

sub_thread_exit = True
print("main and sub thread have benn finished!")