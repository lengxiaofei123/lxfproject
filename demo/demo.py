import paramiko

ssh_connect = paramiko.SSHClient()
def ssh_connects(hostname,username,password,port,cmds):
    know_host = paramiko.AutoAddPolicy()
    ssh_connect.set_missing_host_key_policy(know_host)
    ssh_connect.connect(username = username,hostname=hostname,password=password,port = port)
    stdin, stdout, stderr = ssh_connect.exec_command(cmds)
    print(stdout.read().decode())
    ssh_connect.close()

ssh_connects("192.168.0.103","root","huawei@123","22","ls")