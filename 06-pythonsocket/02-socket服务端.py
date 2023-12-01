import  socket
import  os

Host="192.168.0.106"
PORT=5007
# AF_INET 服务器之间网络通信 SOCK_STREAM tcp 连接
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定主机和端口号
s.bind((Host,PORT))
# 监听客户端连接
s.listen(5)

while True:
    # conn 为新的套接字用来接收和发送数据  address是连接客户端的地址
    conn, address = s.accept()
    while 1:
        # 最大接收1k
        data=conn.recv(1024)
        if not data:
            break
        print('Connected by', address,data)
        cmd_result=os.popen(data.decode()).read()
        conn.sendall(cmd_result.upper().encode())
conn.close()


