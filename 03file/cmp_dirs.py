import sys
import os
from filecmp import dircmp

# 定义全局变量便于递归处理
diff_files = []  # 名称相同但不一致的文件（目录）列表
left_only = []  # 第一个目录独有的文件（目录）列表
right_only = []  # 第二个目录独有的文件（目录）列表
# 从命令行参数中获取要比较的目录路径
try:
    dir1 = sys.argv[1]
    dir2 = sys.argv[2]
except Exception as err:
    print("错误:" + str(err))
    print("使用方法：python cmp_dirs.py 目录1 目录2")
    sys.exit()
''' 处理目录比较结果，分类添加到列表中 '''


def cmp_result(dcmp):
    for item in dcmp.diff_files:
        diff_files.append(os.path.join(dcmp.left, item))
    for item in dcmp.left_only:
        left_only.append(os.path.join(dcmp.left, item))
    for item in dcmp.right_only:
        right_only.append(os.path.join(dcmp.right, item))
    for sub_dcmp in dcmp.subdirs.values():
        cmp_result(sub_dcmp)  # 递归处理子目录


if __name__ == '__main__':
    dcmp = dircmp(dir1, dir2)       # 实例化dircmp类
    print(dcmp.subdirs.values())
    cmp_result(dcmp)
    diff_count = len(diff_files)  # 计算列表长度以获取文件（目录）数
    left_count = len(left_only)
    right_count = len(right_only)
    if (diff_count == 0 and left_count == 0 and right_count == 0):
        print("两个目录完全一致!")
    else:
        print("目录比较结果分析:")
        print(dir1 + "目录中独有" + str(left_count) + "个文件: ", left_only)
        print(dir2 + "目录中独有" + str(right_count) + "个文件: ", right_only)
        print("名称相同但不一致的有" + str(diff_count) + "个文件: ", diff_files)
