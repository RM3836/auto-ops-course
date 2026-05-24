import json
with  open("example1.json", 'r', encoding='utf-8') as f:
    dic = json.load(f)                 # 从JSON文件中读取的数据传给字典变量
reg = dic['insecure-registries']    # 解析insecure-registries的值得到一个列表
reg.append("192.168.10.12:5000")    # 向该列表中添加数据
dic['insecure-registries'] = reg    # 修改insecure-registries的值
dic['max-concurrent-downloads'] = 15  # 键值为数值可直接修改
log_subdic = dic['log-opts']           # 使用字典嵌套解析JSON对象嵌套
log_subdic["cache-max-file"] = 5
log_subdic["cache-max-size"] = "20m"
dic['log-opts'] = log_subdic
with open("example2.json", 'w', encoding='utf-8') as f:
    json.dump(dic, f, indent=4, ensure_ascii=False)   # 写入JSON文件
with open("example2.json", "r") as f:        # 读取新文件验证上述修改是否正确
    print(f.read())

