import psutil
import socket
import logging




'''通用的字节转换函数'''
def bytes2human(n):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n

'''获取CPU信息'''
def get_cpu_info():
    cpu_count = psutil.cpu_count()
    cpu_percent = psutil.cpu_percent(interval=2)
    return dict(cpu_count=cpu_count, cpu_percent=cpu_percent)

'''获取内存信息'''
def get_memory_info():
    virtual_mem = psutil.virtual_memory()
    mem_total = bytes2human(virtual_mem.total)
    mem_used = bytes2human(virtual_mem.total * virtual_mem.percent)
    mem_free = bytes2human(virtual_mem.free + virtual_mem.buffers + virtual_mem.cached)
    mem_percent = virtual_mem.percent
    return dict(mem_total=mem_total, mem_used=mem_used,mem_free=mem_free,mem_percent=mem_percent)

'''获取磁盘信息'''
def get_disk_info():
    disk_usage = psutil.disk_usage('/')
    disk_total = bytes2human(disk_usage.total)
    disk_used = bytes2human(disk_usage.used)
    disk_free = bytes2human(disk_usage.free)
    disk_percent = disk_usage.percent
    disk_io = psutil.disk_io_counters()
    disk_read = bytes2human(disk_io.read_bytes)
    disk_write = bytes2human(disk_io.write_bytes)
    return dict(disk_total=disk_total,disk_used=disk_used,disk_free=disk_free, disk_percent=disk_percent,disk_read=disk_read,disk_write=disk_write)

'''获取网络信息'''
def get_net_info():
    net_io = psutil.net_io_counters()
    net_sent = bytes2human(net_io.bytes_sent)
    net_recv = bytes2human(net_io.bytes_recv)
    return dict(net_sent=net_sent,net_recv=net_recv)

'''汇集系统信息'''
def gather_monitor_data():
    data = {}
    data.update(get_cpu_info())
    data.update(get_memory_info())
    data.update(get_disk_info())
    data.update(get_net_info())
    return data

'''报告结果'''
def report():
    # 获取主机名
    hostname = socket.gethostname()
    data = gather_monitor_data()
    data.update(dict(hostname=hostname))
    # 输出系统信息
    print(f"{hostname}主机系统信息")
    print("—————————————————————————")
    print(f"CPU数量：{data['cpu_count']}")
    print(f"CPU使用率：{data['cpu_percent']}%")
    print("—————————————————————————")
    print(f"内存总量：{data['mem_total']}")
    print(f"已用内存：{data['mem_used']}")
    print(f"空闲内存：{data['mem_free']}")
    print(f"内存使用率：{data['mem_percent']}%")
    print("—————————————————————————")
    print(f"磁盘空间总量：{data['disk_total']}")
    print(f"磁盘已用空间：{data['disk_used']}")
    print(f"磁盘剩余空间：{data['disk_free']}")
    print(f"磁盘空间使用率：{data['disk_percent']}%")
    print(f"磁盘读取数据：{data['disk_read']}")
    print(f"磁盘写入数据：{data['disk_write']}")
    print("—————————————————————————")
    print(f"网卡发送数据：{data['net_sent']}")
    print(f"网卡接收数据：{data['net_recv']}")


if __name__ == '__main__':
    report()
