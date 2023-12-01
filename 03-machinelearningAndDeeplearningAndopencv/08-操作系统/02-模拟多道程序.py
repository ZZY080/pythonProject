import multiprocessing
import time


def worker1():
    """子进程执行的函数"""
    print('子进程1开始执行')
    time.sleep(2)
    # 子进程执行的代码
    print('子进程1结束执行')

def worker2():
    """子进程执行的函数"""
    print('子进程2开始执行')
    time.sleep(1)
    # 子进程执行的代码
    print('子进程2结束执行')

if __name__ == '__main__':
    # 创建子进程
    p = multiprocessing.Process(target=worker1)
    r = multiprocessing.Process(target=worker2)

    p.start()
    # 等待子进程结束
    # p.join()

    r.start()
    # 等待子进程结束
    # r.join()