from fabric import SerialGroup as Group
from fabric import Config
import invoke
# 定义目标服务器集合
hosts = (
    "root@192.168.10.50", "gly@192.168.10.60"
)
# 配置sudo密码
config = Config(overrides={
    'sudo': {
        'password': 'abc123'
    }
})
# 创建SerialGroupd对象统一建立组成员服务器的SSH连接
group = Group(*hosts, connect_kwargs={"password": "abc123"}, config=config)
# 本地文件打包
invoke.run("tar -czf source_test.tar.gz *.py")
# 计算本地压缩包文件的MD5值
local_md5 = invoke.run("md5sum source_test.tar.gz").stdout.split(' ')[0]
# 定义上传校验函数
def upload_check(c):
    c.sudo("mkdir -p /source_test")
    # 修改目标目录权限
    c.sudo("chmod 777 /source_test")
    # 上传压缩包文件
    c.put("source_test.tar.gz", "/source_test/")
    # 计算已上传的压缩包文件的MD5值
    remote_md5 = c.run("md5sum /source_test/source_test.tar.gz").stdout.split(' ')[0]
    # 比较本地与远程压缩包文件的MD5值进行校验
    if remote_md5 == local_md5:
        print(c.host + "服务器上已完成上传")
        c.run("tar -zxvf /source_test/source_test.tar.gz -C /source_test")
    else:
        print(c.host + "服务器上上传失败")
    # 还原目标目录权限
    c.sudo("chmod 754 /source_test")
# 遍历组成员执行上传校验函数
for conn in group:
    upload_check(conn)
group.close()
