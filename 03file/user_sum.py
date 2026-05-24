with open("/etc/passwd", mode="r") as f:   # 打开/etc/passwd文件
    counts = {"system":0,"regular":0}        # 计数用字典
    regulars = []                                # 普通用户列表
    for item in f:
        li = item.strip().split(":")         # 读取的每行数据去除换行符再分割为列表
        user = dict(                            # 使用字典保存用户账户的主要信息
            name = li[0],
            uid = li[2],
            gid = li[3],
            home = li[5],
            shell = li[6]
        )
        uid = int(user["uid"])
        # 通过UID判断系统用户和普通用户
        if uid in range(1000) or uid == 65534:
            counts["system"] += 1
        elif uid >= 1000:
            counts["regular"] += 1
            regulars.append(user)
print("系统用户数：",counts["system"])
print("普通用户数：",counts["regular"])
print("普通用户列表")
print("-"*80)
# 格式化输出用户列表
print(format("用户名", "<20"), format("UID", "^6"), format("GID", "^6"),
      format("主目录", "<20"), format("Shell", "<30"))
for user in regulars:
    print(format(user["name"], "<20"), format(user["uid"], ">6"),
          format(user["gid"], ">6"),format(user["home"], "<20"),
          format(user["shell"], "<30"))
