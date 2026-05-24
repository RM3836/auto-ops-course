# 通过脚本参数提供要查看文件，可一次性查看多个文件
import sys
import os
import re
# 编译正则表达式生成一个正则表达式对象，其模式为匹配以“#”或“;”开头的注释，或者空行
re_obj = re.compile('^#|^;|^$')
arg = sys.argv                # 获取Python脚本参数
if len(arg) > 1:
    del(arg[0])                # 删除第一个参数,即脚本文件本身
else:
    print("请通过参数提供文件！")
    exit()
for file_path in arg:
    if os.path.isfile(file_path):               # 判断由参数提供的文件是否存在
        with open(file_path, mode="r") as f:   # 打开配置文件
            print(file_path,"文件内容：")
            print("-" * 60)
            for line in f.readlines():
                if len(re.findall(re_obj, line))>0: # 匹配的注释行或空行不显示
                    continue
                else:
                    print(line.strip())
            print("-"*60)
    else:
        print(file_path, "文件不存在！")
