from openpyxl import Workbook
wb = Workbook(write_only=True)    # 实例化Workbook类生成工作簿对象
ws = wb.create_sheet()              # 创建一个工作表
ws.append(['部门', '服务器', '得分'])   # 添加而第一行数据
rows = [                                   # 定义一个包含元组的列表（提供二维表数据）
    ('信息部', 'A01', 95),
    ('信息部', 'A02', 78),
    ('信息部', 'A03', 92),
    ('业务部', 'B01', 82),
    ('业务部', 'B02', 66),
    ('业务部', 'B03', 88)
]
for row in rows:                         # 将上述二维表数据逐行添加到工作表
    ws.append(row)
wb.save("servertest.xlsx")                 
