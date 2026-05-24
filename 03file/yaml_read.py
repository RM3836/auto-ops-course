import yaml

with open("example1.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)  # 获取YAML文件数据
network = data['network']  # 解析字典中的network键值
print("版本:", network["version"])  # 解析network键值中嵌套的字典
print("渲染:", network["renderer"])
print("以太网配置:")
ethernets = network["ethernets"]
for nic_name, nic_conf in ethernets.items():  # 遍历ethernets字典
    print("  网卡:" + nic_name)
    print("    IP地址:", ";".join(str(ip) for ip in nic_conf["addresses"])) #列表
    print("    名称服务器:")
    print("      名称搜索:", ";".join(str(s) for s in nic_conf["nameservers"]["search"]))
    print("      IP地址:", ";".join(str(a) for a in nic_conf["nameservers"]["addresses"]))
    print("    路由")
    for route in nic_conf["routes"]:             # 路由列表
        print("      目的:", route["to"])          # 嵌套字典
        print("      经由:", route["via"])

