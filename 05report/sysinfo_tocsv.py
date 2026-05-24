from datetime import datetime
import os
# 导入 csv 库
import csv
from apscheduler.schedulers.blocking import BlockingScheduler
# 从sysinfo_bypsutil.py文件导入report()函数
from sysinfo_bypsutil import gather_monitor_data
file_name="sysinfo.csv"

'''定义要执行的任务'''
def monjob():
    print('监测时间: %s' % datetime.now())
    data = gather_monitor_data()
    data['mon_time']=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # 创建标题列表
    header_list = data.keys()
    # 创建数据列表，列表的每个元素都是字典
    data_list=[]
    data_list.append(data)
    csv_lines = 0
    if os.path.exists(file_name):
        csv_lines = len(open(file_name).readlines())
    # 以追加方式打开文件。注意添加参数newline=""，否则会在两行数据之间都插入一行空白。
    with open(file_name, mode="a", encoding="utf-8-sig", newline="") as f:
        # 基于打开的文件创建csv.DictWriter对象，将标题列表作为参数传入
        writer = csv.DictWriter(f, header_list)
        if csv_lines == 0:            #如果CSV文件没有内容，则写入标题行
        # 写入标题行
            writer.writeheader()
        # 写入数据行
        writer.writerows(data_list)

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(monjob, 'interval', minutes=2)
    # 给出强制退出的组合键，兼顾Linux和Windows平台
    print('按 Ctrl+{0} 键退出'.format('Break' if os.name == 'nt' else 'C'))
    # 先运行一次定义的任务，再启动调度器
    monjob()
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print('已退出！')
        exit()
