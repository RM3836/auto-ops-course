import yaml

with open("example1.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)  # 获取YAML文件数据
network = data['network']     # 解析字典中的network键值
network["version"] = 3         # 修改network字典中的version键值
ethernets = network["ethernets"]
# 修改嵌套的字典中的键值，下面添加两个IP地址
ethernets["enp3s0"]["addresses"].extend(("10.10.20.2/24","10.10.30.2/24"))
with open("example2.yaml", "w", encoding="utf-8") as f:
    yaml.dump(data,f)              # 写入YAML文件
with open("example2.yaml", "r", encoding="utf-8") as f:
    print(yaml.safe_load(f))     # 读取新文件验证上述修改是否正确
