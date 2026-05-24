import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 使用非root用户连接服务器
ssh.connect('192.168.10.60', port=22, username='gly', password='abc123')
# 执行sudo命令时加上-S选项
stdin, stdout, stderr = ssh.exec_command('sudo -S cat /etc/shadow')
# 通过标准输入提供用户密码，注意\n表示回车换行
stdin.write('abc123\n')
# 刷新标准输入的内部缓冲区，将其中内容立即提供给标准输入
res, err = stdout.read(), stderr.read()
result = res if res else err
print(result.decode())
# 关闭连接
ssh.close()