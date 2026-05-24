from scapy.all import *
print('开始抓取数据包…')
target = '192.168.10.50'
pkts = sniff(filter='host '+ target + ' and icmp',prn=lambda x:x.summary())
# 将抓取的数据包存入PCAP文件
wrpcap('icmp_test.pcap', pkts)
