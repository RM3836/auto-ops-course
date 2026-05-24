import paramiko
# 创建Transport对象
transport = paramiko.Transport(('192.168.10.60', 22))
# 建立SSH连接
transport.connect(username='gly', password='abc123')
# 创建SSHClient对象并将其transport变量指定为上述Transport对象
ssh = paramiko.SSHClient()
ssh._transport = transport
# 使用SSHClient对象的方法进行远程操作
# stdin, stdout, stderr = ssh.exec_command('ls -ltr /etc')
# print (stdout.read().decode())
# 可以创建SFTPClient对象，继续利用Transport对象及其连接执行文件传输操作
# 关闭Transport对象及其连接

stdin, stdout, stderr = ssh.exec_command('sudo -S df')
stdin.write('abc123\n')
stdin.flush()
print (stdout.read().decode())

transport.close()



# ssh = paramiko.SSHClient()
# ssh._transport = transport
# # 执行命令，和传统方法一样
# stdin, stdout, stderr = ssh.exec_command('echo `date` && df -hl')
# print(stdout.read().decode('utf-8'))
#
# # 实例化一个 sftp对象,指定连接的通道
# sftp = paramiko.SFTPClient.from_transport(transport)
# # 发送文件
# sftp.put(localpath='./paramiko_pwd.py',
#         remotepath='/tmp/paramiko_pwd.py')
# # 下载文件
# # sftp.get(localpath='./transport_upload_download.py',
# #        remotepath='/tmp/transport_upload_download_tmp.py')
# stdin, stdout, stderr = ssh.exec_command('ls -l /tmp')
# # print(stdout.read().decode('utf-8'))
# # 获取命令结果
# res, err = stdout.read(), stderr.read()
# result = res if res else err
#
# print(result.decode())
# 关闭连接
transport.close()
