from datetime import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler

# 从sysinfo_bypsutil.py文件导入report()函数
from sysinfo_bypsutil import report
from sysinfo_bypsutil import gather_monitor_data
import logging
# 日志文件基本设置
logging.basicConfig(format='%(asctime)s  %(message)s',  level=logging.WARNING, filename='sys_overload.log')
'''定义要执行的任务'''
def monjob():
    print('监测时间: %s' % datetime.now())
    report()
    logging.warning('执行一次监测! ')
    data = gather_monitor_data()
    threshold = 2  # 过载阈值（百分比）
    if data['cpu_percent'] > threshold:
        logging.warning(f"CPU过载！使用率达 {data['cpu_percent']}%")
    if data['mem_percent'] > threshold:
        logging.warning(f"内存过载！使用率达 {data['mem_percent']}%")
    if data['disk_percent'] > threshold:
        logging.warning(f"磁盘空间紧张！使用率达 {data['disk_percent']}%")

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(monjob, 'interval', minutes=5)
    # 给出强制退出的组合键，兼顾Linux和Windows平台
    print('按 Ctrl+{0} 键退出'.format('Break' if os.name == 'nt' else 'C    '))
    # 先运行一次定义的任务，再启动调度器
    monjob()
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print('已退出！')
        exit()




