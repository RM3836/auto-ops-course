import paramiko
# 创建Transport对象
transport = paramiko.Transport(('192.168.10.50', 22))
# 建立SSH连接
transport.connect(username='root', password='abc123')
# 创建SSHClient对象并将其transport变量指定为上述Transport对象
ssh = paramiko.SSHClient()
sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put('./paramiko_pwd.py', '/tmp/paramiko_pwd.py')
dir = sftp.listdir(path='/tmp')
print(dir)
# 将remove_path 下载到本地 local_path
sftp.get('/etc/hosts', 'centos_host1')

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
