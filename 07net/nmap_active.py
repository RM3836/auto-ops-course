import nmap
# 指定扫描目标
target = '192.168.10.10/24'
nm = nmap.PortScanner()
# 通过扫描检测子网中的主机状态
nm.scan(hosts=target, arguments='-n -sn -PE -PA21,23,80,3389')
# 定义输出格式
fm = "{:25}\t{:10}"
print( '--------------主机状态----------------')
print(fm.format(' 主机','状态'))
hosts = nm.all_hosts()   # 从扫描结果中获取主机列表
for host in hosts:
    state = nm[host].state()   # 获取指定主机的状态
    if state == 'up':
        print('\033[1;32m',fm.format(host,'正在运行'))  # 以绿色字体显示活动状态的主机
    else:
        print('\033[1;31m',fm.format(host,'已经停机'))  # 以红色字体显示停机状态的主机

