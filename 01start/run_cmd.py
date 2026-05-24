import subprocess

'''定义执行外部命令的函数'''


def run_cmd(cmd):
    p = subprocess.Popen(cmd,
                         shell=True,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if p.returncode != 0:  # 执行失败，以元组形式返回返回码和错误信息
        return p.returncode, stderr
    return p.returncode, stdout  # 执行成功，以元组形式返回返回码和输出结果

if __name__ == "__main__":
    # 测试上述函数
    res = run_cmd(['pip list'])
    # 获取的信息需要解码
    if res[0] != 0:
        print('未成功执行！')
        print(res[1].decode())
    else:
        print('执行结果：')
        print(res[1].decode())
