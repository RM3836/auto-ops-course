import paramiko
import sys
import socket
import select
#from paramiko.py3compat import u
# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect('192.168.10.50', port=22, username='root', password='abc123')
# 启动交互式Shell会话返回一个新的通道
channel = ssh.invoke_shell()
# 通过循环监控用户输入和服务器的回显数据
while True:
    # 通过select模块的select方法监听终端的输入输出，一旦变化，就将数据发送给服务器
    # 其中sys.stdin用于处理用户的输入，channel用于接收服务器返回的数据
    readable, writeable, error = select.select([channel, sys.stdin, ],[],[],1)
    # 如果服务器有数据返回（通常是命令执行结果），则在终端进行显示
    if channel in readable:
        try:
            #data = u(channel.recv(1024))   # 获取服务器的回显数据
            data = (channel.recv(1024))   # 获取服务器的回显数据
            data = str(data, encoding='utf-8')  
            if len(data) == 0:
                print('\r\n*** EOF\r\n')
                break
            sys.stdout.write(data)         # 写入标准输出的缓冲区
            sys.stdout.flush()              # 刷新缓冲区，将缓冲区内容显示出来
        except socket.timeout:
            pass
    # 如果用户在终端输入内容（通常是Shell命令），则将内容发送到服务器
    if sys.stdin in readable:
        input = sys.stdin.readline()
        channel.sendall(input)
# 关闭通道和连接
channel.close()
ssh.close()

