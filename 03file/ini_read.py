import configparser
config = configparser.ConfigParser()  # 实例化ConfigParser类
config.read("example1.ini")  # 读取配置文件
print("读取所有选项值：")          # 遍历整个字典
for section in config.sections():  # 首先读取节
    print(f"节：[{section}]")
    for key in config[section]:  # 读取每个节的选项和值
        print(f"选项：{key}, 值：{config[section][key]}")  # 输出选项和值
print("读取个别选项值：")          # 从字典中读取指定元素
print(f"版本：{config['Global']['version']}")
print(f"发行商：{config['Preferences']['app.distributor']}")
