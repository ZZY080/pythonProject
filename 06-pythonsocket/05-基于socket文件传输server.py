import  socket
import tqdm
import  os

# 设置服务器的IP和端口号
SERVER_HOST="192.168.0.106"
SERVER_PORT=5001

# 设置文件读写缓冲区
BUFFER_SIZE=4096
SEPARATOR="<SEPARATOR>"

# 创建的SERVER
s=socket.socket()
s.bind((SERVER_HOST,SERVER_PORT))
# 设置连接监听数
s.listen(5)
print(f"服务器端监听{SERVER_HOST}:{SERVER_PORT}")
# 接收客户端连接
client_socket,address=s.accept()
# 打印客户端的IP
print(f"客户端{address}连接")
# 接收客户端信息
received=client_socket.recv(BUFFER_SIZE).decode()
filename,file_size=received.split(SEPARATOR)
print(filename)
# 获取文件的名字
filename=os.path.basename(filename)
file_size=int(file_size)

# 文件接收处理
progress=tqdm.tqdm(range(file_size),f"接收{filename}",unit="B",unit_divisor=1024,unit_scale=True)

with open(filename,"wb") as f:
    for _ in progress:
        # 从客户端读取数据
        bytes_read=client_socket.recv(BUFFER_SIZE)
        # 如果没有数据传输内容
        if not bytes_read:
            break
        # 读取与写入
        f.write(bytes_read)
        # 更新进度条
        progress.update(len(bytes_read))
# 关闭资源
client_socket.close()
s.close()





