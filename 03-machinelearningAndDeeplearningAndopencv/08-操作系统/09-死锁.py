import threading

class Resource:
    def __init__(self, num):
        self.num_available = num
        self.lock = threading.Lock()

    def acquire(self):
        self.lock.acquire()
        if self.num_available <= 0:
            self.lock.release()
            return False
        self.num_available -= 1
        self.lock.release()
        return True

    def release(self):
        self.lock.acquire()
        self.num_available += 1
        self.lock.release()


class Process(threading.Thread):
    def __init__(self, name, resource):
        threading.Thread.__init__(self)
        self.name = name
        self.resource = resource

    def run(self):
        print(f"{self.name} is requesting the resource.")
        acquired = self.resource.acquire()
        if acquired:
            print(f"{self.name} has acquired the resource and is executing.")
            # 在这里执行进程的工作
            print(f"{self.name} has finished executing and is releasing the resource.")
            self.resource.release()
        else:
            print(f"{self.name} couldn't acquire the resource and is waiting.")


def main():
    num_resources = 3  # 资源的数目
    max_demand = 1  # 每个进程的最大需求
    num_processes = 3  # 进程的数目

    resource = Resource(num_resources)

    # 创建并启动进程
    processes = []
    for i in range(num_processes):
        process = Process(f"Process-{i+1}", resource)
        processes.append(process)
        process.start()

    # 等待所有进程执行完毕
    for process in processes:
        process.join()

    print("All processes have finished.")

if __name__ == "__main__":
    main()
