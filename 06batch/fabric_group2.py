from fabric import SerialGroup as Group

hosts = (
    "root@192.168.10.50", "gly@192.168.10.60"
)
pool = Group(*hosts, connect_kwargs={"password": "abc123"})


def upload(c):
    if not c.run('test -e /tmp/test', warn=True):
        print("dd")
        c.run('mkdir -p /tmp/test')
    c.put('fabric_basic.py', '/tmp/test')


for conn in pool:
    upload(conn)
