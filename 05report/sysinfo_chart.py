import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('sysinfo.csv')  # 读取CSV文件产生DataFrame对象
# 从DataFrame对象获取所需的序列
x1 = df['mon_time'].apply(lambda x: x.split(' ')[1])  # 使用匿名函数处理日期格式
y1 = df['cpu_percent']
y2 = df['mem_percent']
y3 = df['disk_percent']
plt.rcParams['font.family'] = ['AR PL UKai CN']  # 设置字体解决中文显示问题
plt.title('系统监控数据', fontsize='18')  # 设置图表标题内容及其字体大小
plt.plot(x1, y1, label='CPU', color='r', marker='8')  # 红色，八角形标记
plt.plot(x1, y2, label='内存', color='g', marker='o')  # 绿色，实心圆标记
plt.plot(x1, y3, label='磁盘', color='b', marker='*')  # 蓝色，星号标记
plt.grid(axis='y')  # 显示网格关闭Y轴
plt.ylabel('使用率')
plt.legend(['CPU', '内存', '磁盘'])  # 设置图例
plt.show()
