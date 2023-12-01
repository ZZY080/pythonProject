from multiprocessing import Process
import time, json


def find(name):
    # 模拟网络延迟
    time.sleep(1)
    # 用于将python字符串转换为对象并且读取文件
    dic = json.load(open('ticket.txt','r'))
    print('%s 剩余票数 %s ' % (name, dic['count']))


def get(name):
    # 模拟网络延迟
    time.sleep(1)
    dic = json.load(open('ticket.txt'))
    if dic['count'] > 0:
        dic['count'] -= 1
        # 用于将python对象转换为字符串并且写入文件
        json.dump(dic, open('ticket.txt', 'w'))
        print("%s 购票成功 " % name)


def task(name):
    find(name)
    # 模拟查询票后填写买票信息
    time.sleep(1)
    get(name)


if __name__ == '__main__':
    for i in range(100):  # 模拟5个人抢票
        name = 'p%s' % i
        p = Process(target=task, args=(name,))
        p.start()
        #  而join是将整个任务改为串行。如果上面我们直接在p.start()后面p.join()。这样就只有一个人能查到票。显然与现实不符。

