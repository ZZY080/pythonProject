import  socket
import  time

HOST='192.168.0.106'
PORT=5007
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
while True:
    content = input('请输入内容:').strip().encode()
    s.sendall(content)
    data = s.recv(1024)
    print('Received', repr(data))
s.close()

