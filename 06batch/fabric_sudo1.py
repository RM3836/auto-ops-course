from invoke import Responder
from fabric import Connection

c = Connection('gly@192.168.10.60', connect_kwargs={'password': 'abc123'})
user = 'gly'
password = 'abc123'
sudopass = Responder(
    pattern=f'\[sudo\] password for {user}:',
    response=password + '\n'
)

# 注意需要设置pty=True
c.run('sudo cat /etc/shadow', pty=True, watchers=[sudopass])
c.close()
