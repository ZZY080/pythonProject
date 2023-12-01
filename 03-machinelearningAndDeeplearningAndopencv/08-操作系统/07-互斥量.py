from multiprocessing import Process,Semaphore
import time,random

def wc(sem,name):
    sem.acquire()
    print("%s is wcing" % name)
    time.sleep(random.randint(2,9))
    print("%s is done" % name)
    sem.release()


if __name__ == '__main__':
    # 将信号量设置为3，就是最多之能同时运行3个进程，这个数字可以自己根据情况设置
    sem = Semaphore(3)
    for i in range(10):
        p = Process(target=wc,args=(sem,"p"+str(i)))
        p.start()
