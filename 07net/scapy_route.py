from scapy.all import *
from scapy.layers.inet import IP,TCP
# 指定目标主机
target='163.com'
# 构造自己的数据包去跟踪1至20跳的路由
ans, unans = sr(IP(dst=target, ttl=(1,20),id=RandShort())/TCP(flags=0x2),timeout=60)
# 显示返回的路由，isinstance()函数用于判断返回包的载荷是否属于TCP类型
for snd,rcv in ans:
   print (snd.ttl, rcv.src, isinstance(rcv.payload, TCP))
