import multiprocessing

# 定义一个任务函数
def task(num):
    return num * num

if __name__ == '__main__':
    # 创建一个进程池，其中包含4个进程
    pool = multiprocessing.Pool(processes=4)

    # 向进程池中提交10个任务
    results = [pool.apply_async(task, args=(i,)) for i in range(1000)]

    # 获取所有任务的结果
    output = [p.get() for p in results]

    # 输出结果
    print(output)