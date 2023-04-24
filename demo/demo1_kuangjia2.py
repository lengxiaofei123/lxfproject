import socket
import subprocess

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('192.168.0.103', 8089))
server.listen(5)

while True:
    conn, addr = server.accept()
    while True:
        try:
            cmd = conn.recv(1024)
        except:
            break
        if not cmd:
            break
        obj = subprocess.Popen(cmd.decode('utf-8'),
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE
                               )
        out_res = obj.stdout.read()
        err_res = obj.stderr.read()

        conn.send(out_res + err_res)
    conn.close()
#  服务端脚本的需要传到服务端运行，chmod u+x xxx.py,python2 xxx.py
