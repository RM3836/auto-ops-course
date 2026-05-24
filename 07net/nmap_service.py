import nmap
from prettytable import PrettyTable
# 定义报表用表格的PrettyTable对象并添加表头
Report_Table = PrettyTable(["Host", "Services", "State", "Version"])
# 指定扫描目标
target = '192.168.10.0/24'
nm = nmap.PortScanner()
# 通过扫描检测主机中的服务及其状态和版本
nm.scan(target, arguments='-sV')
# 遍历扫描结果中的主机列表
for host in nm.all_hosts():
    # 编辑指定主机的协议列表
    for proto in nm[host].all_protocols():
        # 初始化表示服务、状态和版本的序列
        services, states , versions = [], [], []
        # 获取指定主机指定协议的端口列表
        ports = nm[host][proto].keys()
        # 遍历端口列表并将服务、状态和版本数据添加到相应序列
        for port in ports:
            services.append(nm[host][proto][port]['name'])
            states.append(nm[host][proto][port]['state'])
            versions.append(nm[host][proto][port]['product'] + ' ' + nm[host][proto][port]['version'])
        # 将一台主机的数据添加到PrettyTable表格
        Report_Table.add_row([host, '\n'.join(services), '\n'.join(states), '\n'.join(versions)])
print(Report_Table)
