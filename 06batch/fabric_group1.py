from fabric import SerialGroup as Group
hosts = (
  "root@192.168.10.50", "gly@192.168.10.60"
)
pool = Group(*hosts, connect_kwargs={"password": "abc123"})
pool.run("sudo ls")
pool.run('mkdir  /tmp/test')
pool.put('fabric_basic.py','/tmp/test')
pool.close()
#
# if results = pool.run('uname -s')
# for connection, result in results.items():
# 	print("{0.host}: {1.stdout}".format(connection, result))
# if pool.run('test -f /opt/mydata/myfile', warn=True).failed:
#     pool.put('myfiles.tgz', '/opt/mydata')
#     pool.run('tar -C /opt/mydata -xzvf /opt/mydata/myfiles.tgz')
