# 根据进程名称杀死进程，可一次性杀死多个进程，进程名称由命令行参数提供
import psutil
import sys
'''定义按进程名杀死进程的函数'''
def kill_proc_byname(proc_names):
    proc_list = psutil.pids()
    try:
        for pid in proc_list:
             # 循环读取进程名，符合条件即杀死相应的进程
            for proc_name in proc_names:
                # 基于PID创建进程对象
                p = psutil.Process(pid)
                # 判断该进程对象的进程名是否等于要杀死的进程名
                if p.name() == proc_name:
                    p.kill()
                    print(f"已杀死名称为{proc_name}，PID为{pid}的进程!")
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    # 从命令行参数列表中读取进程名
    kill_proc_byname(sys.argv[1:])


