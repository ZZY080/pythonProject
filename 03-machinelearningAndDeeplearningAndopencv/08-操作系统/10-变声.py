import pyaudio
import numpy as np
import socket

# 设置参数
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# 创建Pyaudio对象
p = pyaudio.PyAudio()

# 打开麦克风
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# 创建UDP套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # 读取音频数据
    data = stream.read(CHUNK)

    # 将音频数据转换为numpy数组
    audio = np.frombuffer(data, dtype=np.int16)

    # 对音频数据进行变声处理
    audio = np.interp(audio, [-32768, 32767], [-8192, 8191])
    audio = np.interp(audio, [-8192, 8191], [-32768, 32767])

    # 将音频数据转换为bytes类型
    data = audio.astype(np.int16).tobytes()

    # 发送音频数据到Android设备
    sock.sendto(data, ('<Android设备IP地址>', 12345))

# 关闭套接字、麦克风和Pyaudio对象
sock.close()
stream.stop_stream()
stream.close()
p.terminate()
