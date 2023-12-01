from multiprocessing import Process, Lock
import time, json


def find(name):
    # 模拟网络延迟
    time.sleep(1)
    dic = json.load(open('ticket.txt'))
    print('%s 查到剩余票数 %s ' % (name, dic['count']))


def get(name):
    # 模拟网络延迟
    time.sleep(1)
    dic = json.load(open('ticket.txt'))
    if dic['count'] > 0:
        dic['count'] -= 1
        json.dump(dic, open('ticket.txt', 'w'))
        print("%s 购票成功 " % name)


def task(name, lock):
    find(name)
    time.sleep(3)  # 模拟查询票后填写买票信息

    lock.acquire()  # 加锁  相当于进厕所后的关门操作
    get(name)
    lock.release()  # 释放锁  相当于方便完后的开门操作


# 上面加锁与释放锁的代码还可以这样，避免加锁后忘了释放
# with  lock:
#     get(name)


if __name__ == '__main__':
    lock = Lock()
    for i in range(10):  # 模拟5个人抢票
        name = 'p%s' % i
        p = Process(target=task, args=(name, lock))
        p.start()
