import sys
import difflib
# 从命令行参数中获取要比较的文件路径
try:
    file1 = sys.argv[1]
    file2 = sys.argv[2]
except Exception as  err:
    print("错误:" + str(err))
    print("使用方法：python diff_files.py  文件1 文件2")
    sys.exit()
''' 读取整个文件，自动生成逐行分隔的字符串列表 '''
def readfile(filename):
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except IOError as err:
        print('读取文件错误:' + str(err))
        sys.exit()
''' 比较两个文件，生成HTML格式的文档 '''
def compare_file(file1, file2):
    file1_content= readfile(file1)
    file2_content = readfile(file2)
    # 实例化HtmlDiff()类以生成HtmlDiff对象
    d = difflib.HtmlDiff()
    # 通过make file()方法生成HTML格式的比较结果
    result = d.make_file(file1_content, file2_content)
    return result
if __name__ == '__main__':
    result = compare_file(file1,file2)
    # 将比较结果写入到结果文件中
    with open("diff_result.html", 'w') as f:
        f.writelines(result)
