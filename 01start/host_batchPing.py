import subprocess

# 定义颜色来区分主机状态，颜色格式：\033[显示方式;前景色;背景色m
redFont = "\033[1;31m"  # 红色
greenFont = "\033[1;32m"  # 绿色
defautFont = "\033[0m"  # 结束颜色格式的输出
with open("host_list", "r") as f:
    for host in f:  # 逐行读取文本文件中的主机
        host = host.strip()  # 每行末尾有隐藏的换行符\n，使用strip()函数清除
        for i in range(3):
            result = subprocess.run(['ping', '-c1', '-W1', str(host)], stdout=subprocess.PIPE, check=False)
            if result.returncode == 0:  # 判断返回码
                print(greenFont + host + ' 主机' + defautFont + ' 正在运行')
                break
            else:
                if i == 2:  # 连续3次无法通信，则判定为停止状态
                    print(redFont + host + ' 主机' + defautFont + ' 停止运行')
