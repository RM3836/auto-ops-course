from fabric import SerialGroup as Group

hosts = (
    "root@192.168.10.50", "gly@192.168.10.60"
)
# 创建SerialGroupd对象统一建立组成员服务器的SSH连接
group = Group(*hosts, connect_kwargs={"password": "abc123"})
# 定义汇总服务器系统信息的数组
data_total = []


# 定义执行Shell命令采集系统信息的函数
def get_sysinfo(c):
    # 定义采集服务器系统信息的命令字典
    sys_commands = {
        "hostname": "hostname",
        "kernel": "uname -r",
        "architecture": "uname -m",
        "ipadd": "hostname -I",
        "cpu_idle": "top -n 1 -b | sed -n '3p' | awk '{print $8}'",
        "memory_used": "free -m | sed -n '2p' | awk '{print $3}'",
        "memory_total": "free -m | sed -n '2p' | awk '{print $2}'",
        "process_number": "ps -A --no-headers | wc -l",
        "disk_usage": "df / | sed -n '2p' | awk '{print $5}'"
    }
    data_sys = {}  # 定义汇集单台服务器系统信息结果的字典
    # 遍历字典执行Shell命令采集多种系统信息（其中CPU和内存使用率需单独计算）
    for item, command in sys_commands.items():
        if item == "cpu_idle":
            cpu_idle = c.run(command).stdout.rstrip('\n')
            if cpu_idle == "id,":
                cpu_idle = 100
            cpu_usage = str(round(100 - float(cpu_idle), 2)) + "%"
            data_sys['cpu_usage'] = cpu_usage
        elif item == "memory_used":
            memory_used = c.run(command).stdout.rstrip('\n')
        elif item == "memory_total":
            memory_total = c.run(command).stdout.rstrip('\n')
            memory_usage = str(round(int(memory_used) / int(memory_total), 2)) + "%"
            data_sys['memory_usage'] = memory_usage
        else:
            data_sys[item] = c.run(command).stdout.rstrip('\n')
    data_total.append(data_sys)


# 定义输出系统信息报告的函数（这里输出到控制台）
def report(label, item):
    print(f"\n{label:15}", end=" ")
    for data_sys in data_total:
        print(f"{data_sys[item]:40}", end=" ")


# 遍历组成员采集各服务器系统信息
for conn in group:
    get_sysinfo(conn)
group.close()
# 定义报告用的系统信息项目字典
item_names = {'hostname': '服务器', 'kernel': 'Linux内核', 'architecture': '体系结构', 'ipadd': 'IP地址', 'cpu_usage': 'CPU使用率',
              'memory_usage': '内存使用率', 'process_number': '当前进程数', 'disk_usage': '磁盘使用率'}
# 输出系统信息报告
print("===============================服务器系统信息============================")
for item, label in item_names.items():
    report(label, item)
