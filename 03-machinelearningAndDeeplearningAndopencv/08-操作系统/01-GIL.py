import threading
import time

total=0
def add():
    global total
    for i in range(10000000):
        total+=1
        # time.sleep(0.01)
def desc():
    global total
    for i in range(10000000):
        total+=1
        # time.sleep(0.01)


if __name__=="__main__":
    thread1 = threading.Thread(target=add)
    thread2 = threading.Thread(target=desc)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print(total)