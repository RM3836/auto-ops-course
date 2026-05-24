import json
with open("example1.json", 'r', encoding='utf-8') as f:
    dic = json.load(f)                       # 从JSON文件中读取的数据传给字典变量
mirror = dic['registry-mirrors']          # 从字典中解析数据
print("镜像加速地址:", ";".join(str(i) for i in mirror))  # 解析JSON数组
print("私有注册中心的地址:", ";".join(str(i) for i in dic['insecure-registries']))
print("下载最大并发数:", dic['max-concurrent-downloads'])
subdic = dic['log-opts']                    # 使用字典嵌套解析JSON对象嵌套
print("日志选项:")
print("    禁用缓存:", "是" if subdic['cache-disabled']  else "否")
print("    压缩缓存:", "是" if subdic['cache-compress']  else "否")
print("    文件最大数:", subdic['max-file'])
print("    文件最大容量:", subdic['max-size'])
