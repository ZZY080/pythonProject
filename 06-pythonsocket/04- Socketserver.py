import  socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handler(self):
        self.data=self.request.recv(1024).strip()
        self.request.sendall(self.data.upper())


if __name__=='__main__':
    HOST,PORT='192.168.0.106',5007
    server=socketserver.ThreadingTCPServer((HOST,PORT),MyTCPHandler)
    server.serve_forever()