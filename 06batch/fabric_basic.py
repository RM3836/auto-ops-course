from fabric import Connection
host = '192.168.10.50'
user = 'root'
password = 'abc123'
# 实例化Connection类以建立SSH连接
c = Connection(host=host, user=user, connect_kwargs={ 'password': 'abc123'} )
print(c.config)

# 在远程系统上运行命令(用run方法),并获得返回结果
result = c.run('uname -r')
# 显示执行命令返回的结果
print(result.stdout.strip())
# 继续执行命令
c.run('df')
# 切换当前目录连续执行多条命令
with c.cd('/home'):
    c.run("mkdir -p testdir")
    c.run("touch testfile")
    c.run("ls -l")
# 自动切换回之前的当前目录
c.run("pwd")
c.close()



