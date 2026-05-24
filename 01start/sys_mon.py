import re
import time
'''菜单函数 '''
def menu():
    print('''
    ╔———————系统监控功能菜单————————╗
    │   1  查看CPU使用率           │
    │   2  查看内存使用率           │
    │   3  查看网络接口收发数据量     │
    │   0  退出系统                │
    ╚————————————————————————————╝
    ''')
'''主函数 '''
def main():
    ctrl = True  # 标记是否退出系统
    while (ctrl):
        menu()  # 显示菜单
        option = input("请选择菜单项：")  # 选择菜单项
        option_str = re.sub("\D", "", option)  # 提取数字
        if option_str in ['0', '1', '2', '3']:
            option_int = int(option_str)
            if option_int == 0:  # 退出系统
                ctrl = False
            elif option_int == 1:  # CPU使用率
                cpu_usage = get_cpu_usage()
                print(f"CPU使用率：{cpu_usage}%")
            elif option_int == 2:  # 内存使用率
                mem_usage= get_mem_usage()
                print(f"内存使用率：{mem_usage}%")
            elif option_int == 3:  # 网络接口
                net_data = get_net_data()
                for iface in net_data.keys():
                    print(f"网络接口：{iface} 接收数据：{ net_data[iface][0]}M 发送数据：{net_data[iface][1]}M")

'''获取CPU使用率的函数'''
def get_cpu_usage():
    with open("/proc/stat", "r") as f:
        line1 = f.readline()
    cpu_time1 = line1.split()
    cpu_time1 = cpu_time1[1:8]
    # 将列表中的元素从字符串转换为整数
    cpu_time1 = [int(x) for x in cpu_time1]
    # 获取CPU空闲的时间（不包含IO等待）
    cpu_idle1 =int(cpu_time1[3])
    # 汇总CPU使用时间
    cpu_total1 = sum(cpu_time1)
    # 等5秒钟之后再测下一次CPU时间
    time.sleep(5)
    with open("/proc/stat", "r") as f:
        line1 = f.readline()
    cpu_time2 = line1.split()
    cpu_time2 = cpu_time2[1:8]
    cpu_time2 = [int(x) for x in cpu_time2]
    cpu_idle2 = cpu_time2[3]
    cpu_total2 = sum(cpu_time2)
    # 计算CPU总的空闲时间
    cpu_idle = cpu_idle2 - cpu_idle1
    # 计算CPU总的使用时间
    cpu_total = cpu_total2 - cpu_total1
    # 计算CPU利用率，结果使用round函数四舍五入并保留两位小数
    cpu_usage = round( (cpu_total - cpu_idle)/cpu_total*100,2)
    return cpu_usage
'''获取内存使用率的函数'''
def get_mem_usage():
    meminfo = {}
    with open("/proc/meminfo","r") as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    # 获取内存总量
    mem_total = int(meminfo["MemTotal"][0:-3])
    # 空闲（Free）内存的数据已失效，可以随时被程序使用
    mem_free = int(meminfo["MemFree"][0:-3])
    # Inactive内存中的数据是有效的，但是最近未被使用
    mem_inactive = int(meminfo["Inactive"][0:-3])
    # 计算已经使用的内存量
    mem_used = mem_total - mem_free - mem_inactive
    # 计算内存使用率
    mem_usage = round((mem_used / mem_total * 100),2)
    return mem_usage
'''获取网络接口收发数据量的函数'''
def get_net_data():
    net_data = {}
    ifstat = open("/proc/net/dev").readlines()
    i = 0
    for line in ifstat:
        i += 1
        # 从第3行开始处理
        if i > 2 :
            # 获取网络接口名称
            iface = line.split()[0][0:-1]
            if iface == "lo":
                continue
            # 接收数据量
            rxdata = round((int(line.split()[1])/1024/1024),2)
            # 发送数据量
            txdata = round((int(line.split()[9])/1024/1024),2)
            net_data[iface] = (rxdata,txdata)
    return net_data

if __name__ == "__main__":
    main()