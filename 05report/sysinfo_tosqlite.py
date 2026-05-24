from datetime import datetime
import os
# 导入sqlite3 模块
import sqlite3
from apscheduler.schedulers.blocking import BlockingScheduler
# 从sysinfo_bypsutil.py文件导入report()函数
from sysinfo_bypsutil import gather_monitor_data

db_file = "sysinfo.db3"
'''定义数据库表'''
def db_define():
    # 连接数据库
    con = sqlite3.connect(db_file, timeout=10, check_same_thread=False)
    # 创建游标对象
    cur = con.cursor()
    # 创建表（如果存在该表就不创建）
    cur.execute('CREATE TABLE IF NOT EXISTS  sysinfo (id INTEGER PRIMARY KEY, cpu_count INT, cpu_percent REAL, mem_total TEXT, mem_used TEXT, mem_free TEXT, mem_percent REAL, disk_total TEXT,disk_used TEXT,disk_free TEXT,disk_percent REAL,disk_read TEXT,disk_write TEXT,net_sent TEXT,net_recv TEXT,mon_time TEXT)')
    con.commit()
    cur.close()
    con.close()

'''定义要执行的任务'''
def monjob():
    print('监测时间: %s' % datetime.now())
    data = gather_monitor_data()
    data['mon_time']=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    field_names = ','.join(data.keys())           # 从字典数据中获取字段名并转换为字符串
    field_values = ''                                # 定义字段值变量
    # 从字典数据中获取字段值并连接成字符串
    for index, item in enumerate(data.values()):
        if isinstance(item, str):
            item = '\'' + item + '\''
        else:
            item = str(item)
        if index>0:
            field_values = field_values + "," + item
        else:
            field_values = field_values + item
    # 插入记录语句
    statement = "INSERT INTO sysinfo (" + field_names + ") VALUES("  + field_values +")"
    con = sqlite3.connect(db_file, timeout=10, check_same_thread=False)
    cur = con.cursor()
    cur.execute(statement)             # 执行插入操作
    con.commit()
    cur.close()
    con.close()

if __name__ == '__main__':
    db_define()                       # 创建数据库和表
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
