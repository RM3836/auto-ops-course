import csv
file_name="sysinfo.csv"
# 以列表形式读取CSV文件
with open(file_name, encoding="utf-8-sig", mode="r") as f:
    reader = csv.reader(f)
    print("显示第一行（标题行）")
    header = next(reader)
    print(header)
    print("显示数据行")
    for row in reader:
        print(row)

# 以字典形式读取CSV文件
with open(file_name, encoding="utf-8-sig", mode="r") as f:
    # 基于打开的文件，创建csv.DictReader实例
    reader = csv.DictReader(f)
    print("以字典形式显示数据")
    for row in reader:
        print(row)
