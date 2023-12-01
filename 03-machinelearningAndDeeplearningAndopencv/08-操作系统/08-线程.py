from threading import Thread
from time import sleep


def func1(name):
    print(f"线程{name},start")  # format
    for i in range(3):
        print(f"线程{name},{i}")
        sleep(3)
    print(f"线程{name},end")


if __name__ == '__main__':  # 当前程序运行时，生成一个进程
    print("主线程，start")  # 程序运行时，生成一个进程，并主动生成一个主线程
    # 创建线程
    t1 = Thread(target=func1, args=("t1",))  # 使用threading模块中的Thread类创建两个线程对象，target参数是要绑定的函数或者方法
    # 绑定函数或者方法的参数，需要把这些参数放进一个元组args里
    t2 = Thread(target=func1, args=("t2",))
    # 启动线程
    t1.start()
    t2.start()
    print("主线程,end")
# 主线程，start
# 线程t1,start
# 线程t1,0
# 线程t2,start
# 线程t2,0
# 主线程,end
# 线程t1,1
# 线程t2,1
# 线程t1,2
# 线程t2,2
# 线程t1,end
# 线程t2,end
# 主线程在子线程之前就结束了