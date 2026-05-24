import configparser
config = configparser.ConfigParser()  # 实例化ConfigParser类
config["Default"] = {                    # 以字典形式提供一组选项和值
    "OS": "Ubuntu",
    "purpose": "develop",
}
config["res"] = {
    "cpu": "3.2GHz",
    "mem": "16G",
    "disk": "2500G",
}
config["Net"] = {"Servername": "srv001"}  # 设置个别选项值
config["Net"]["ip"] = "192.168.10.11"
config["Net"]["firewall"] = "no"
with open("example2.ini", "w") as configfile: #将选项写入INI文件
    config.write(configfile)
with open("example2.ini", "r") as f: #读取INI验证写入操作是否正确
    print(f.read())
