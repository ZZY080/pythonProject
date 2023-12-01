import numpy as np
import scipy.stats as stats
import simpy

# 设置模拟参数
num_packets = 1000
packet_length_bits = 1000
transmission_rate = 1000  # 每秒1000位
channel_ber = 0.01  # 信道误码率

# 创建模拟环境
env = simpy.Environment()

# 创建一个模拟的无线信道
def wireless_channel(env, packet_length_bits, transmission_rate, ber):
    while True:
        yield env.timeout(packet_length_bits / transmission_rate)
        if np.random.rand() < ber:
            print("Packet with bit errors received")
        else:
            print("Packet successfully received")

# 生成随机数据包
def generate_packets(env, num_packets):
    for _ in range(num_packets):
        yield env.timeout(np.random.exponential(1.0 / 100))  # 每100个包发送一个
        env.process(wireless_channel(env, packet_length_bits, transmission_rate, channel_ber))

# 启动模拟
env.process(generate_packets(env, num_packets))
env.run()
