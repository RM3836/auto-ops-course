from IPy import IP

while True:
    ip_inp = input('请输入IP地址或网络地址（输入"q"退出）：')
    if ip_inp == 'q':
        break                   # 退出
    try:
        ips = IP(ip_inp)
    except Exception as e:
        print(e)
        continue
    if len(ips) > 1:               # IP地址个数大于1
        print('网络地址： %s' % ips.net())
        print('网络掩码： %s' % ips.netmask())
        print('网络前缀长度： %s' % ips.prefixlen())
        print('广播地址： %s' % ips.broadcast())
        print('反向解析地址： %s' % ips.reverseNames()[0])
        print('子网IP地址数：%s' % len(ips))
    else:                            # 单个IP地址的情形
        print('反向解析地址： %s' % ips.reverseName())
    print('整数形式： %s' % ips.int())
    print('十六进制形式： %s' % ips.strHex())
    print('二进制形式： %s' % ips.strBin())
    print('IP地址类型： %s' % ips.iptype())


