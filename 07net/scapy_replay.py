from scapy.all import *
from scapy.layers.inet import *
# 从PCAP文件中读取数据包
pkts_sniff = rdpcap('icmp_test.pcap')
pkts_replay = []
# 遍历数据包列表，并修改数据包进行第三方重放
for pkt in pkts_sniff:
    new_pkt = pkt.payload
    # 仅加入目标主机为192.168.10.50的数据包
    if new_pkt[IP].dst == '192.168.10.50':
        try:
            # 更改数据包的源地址和目标地址
            new_pkt[IP].src = '192.168.10.50'
            new_pkt[IP].dst = 'www.163.com'
            # 将IP包和ICMP的校验和恢复默认值
            del (new_pkt[IP].chksum)
            del (new_pkt[ICMP].chksum)
        except:
            pass
        # 将修改后的数据包加入重播的数据包列表
        pkts_replay.append(new_pkt)
# 重播数据包并显示返回的结果
ans, unans = sr(PacketList(pkts_replay), timeout=20)
ans.summary(lambda s, r: r.sprintf('%IP.src%  \t%IP.dst%  \t %ICMP.type% \t %ICMP.code%'))
