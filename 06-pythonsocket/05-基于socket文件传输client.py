import  socket
import tqdm
import os

# 传输数据分割符
SEPARATOR="<SEPARATOR>"

# 服务器信息
host="192.168.0.106"
port=5001

# 文件传输的缓冲区
BUFFER_SIZE=4096

# 传输文件名
filename=r"E:\backend\DjangoStudy\djangodemo1\static\videos\1.mp4"

# 文件大小
file_size=os.path.getsize(filename)

# 创建socket连接
s=socket.socket()

# 连接服务器
print(f"服务器连接中{host}:{port}")
s.connect((host,port))
print("与服务器连接成功")
# 发送文件名字和文件大小，必须进行编码处理encode()
s.send(f"{filename}{SEPARATOR}{file_size}".encode())
# 文件传输
progress=tqdm.tqdm(range(file_size),f"发送{filename}",unit="B",unit_divisor=1024)
with open(filename,"rb") as f:
    for _ in progress:
        # 读取文件
        bytes_read=f.read(BUFFER_SIZE)
        if not bytes_read:
            break
        # sendall 确保及时网络忙碌的时候，数据任然可以传输
        s.sendall(bytes_read)
        progress.update(len(bytes_read))
# 关闭资源
s.close()


