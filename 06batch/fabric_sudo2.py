from fabric import Config
from fabric import Connection

# 预先配置sudo密码
config = Config({
    'sudo': {
        'password': 'abc123'
    }
})
c = Connection('gly@192.168.10.60',connect_kwargs={'password': 'abc123'},config=config)
# 使用sudo方法执行命令
c.sudo('cat /etc/shadow')

c.close()
