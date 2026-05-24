import sqlite3
db_file="sysinfo.db3"

con = sqlite3.connect(db_file, timeout=10, check_same_thread=False)
cur = con.cursor()
# 执行查询语句
cur.execute('SELECT * FROM sysinfo')
values = cur.fetchall()
cur.close()
con.close()
# 显示所有记录
for rec in values:
   print(rec)

