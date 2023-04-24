import socket
# 基础版
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建基于tcp连接的socket对象
# client.connect(('192.168.0.103', 8089))
#
# while True:
#     cmd = input('请输入终端命令>>>').strip()
#     if not cmd:
#         continue
#     client.send(cmd.encode('utf-8'))
#     res = client.recv(1024)  # 数据量请求过大会出现粘包问题也就是串回显
#     print(res.decode('utf-8'))
# .............................................................................................................

class connect(object):

    def __init__(self, server_ip, port):
        self.server_ip = server_ip
        self.port = port

    def client(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建基于tcp连接的socket对象
        client.connect((self.server_ip, self.port))
        while True:
            cmd = input('请输入终端命令>>>').strip()
            if not cmd:
                continue
            client.send(cmd.encode('utf-8'))
            res = client.recv(1024)  # 数据量请求过大会出现粘包问题也就是串回显
            print(res.decode('utf-8'))


if __name__ == '__main__':  # 作为文件调用时会执行以下内容
    cd = connect("192.168.0.103", 8089)
    cd.client()
