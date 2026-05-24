# 从scapy.all导入所有函数
from scapy.all import *
# 从scapy.layers.inet导入IP等类
from scapy.layers.inet import IP, TCP
#  定义要扫描的目标主机和端口
target = ['192.168.10.50', 'www.163.com']
port = [22, 53, 80, 443]
# 构建SYN数据包并发送到目标主机和端口，由一个元组获取返回的数据包
ans, unans = sr(IP(dst=target) / TCP(dport=port, flags='S'), timeout=30)
# 将获取的应答包使用make_table()函数输出报表
ans.make_table(
    lambda s, r: (s.dst, s.dport, r.sprintf('打开')) if r.sprintf('%TCP.flags%') == 'SA' else (s.dst, s.dport, r.sprintf('关闭')))
