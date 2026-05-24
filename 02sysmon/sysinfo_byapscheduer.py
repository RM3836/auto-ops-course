from datetime import datetime
import os
import sys
from apscheduler.schedulers.blocking import BlockingScheduler
# 从sysinfo_bypsutil.py文件导入report()函数
from sysinfo_bypsutil import report
'''定义要执行的任务'''
def monjob():
    file = sys.stdout  # 存储控制台输出对象
    sys.stdout = open('sysinfo.txt', 'a')  # 将屏幕输出的内容写入文件
    print('监测时间: %s' % datetime.now())  # 写入文件
    print(report())  # 继续写入文件
    sys.stdout.close()  # 关闭重定向
    sys.stdout = file  # 将 print()的输出结果返回给控制台


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(monjob, 'interval', minutes=5)
    # 给出强制退出的组合键，兼顾Linux和Windows平台
    print('按 Ctrl+{0} 键退出'.format('Break' if os.name == 'nt' else 'C'))
    # 先运行一次定义的任务，再启动调度器
    monjob()
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print('已退出！')
        exit()




