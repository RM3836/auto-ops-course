import dns.resolver
while True:
    domain = input('请输入要解析的域名（输入"q"退出）：')
    if domain == 'q':
        break
    print('*******主机记录解析*********')
    try:
       A = dns.resolver.resolve(domain, 'A')  # 解析类型为A记录
       for m in A.response.answer:
           for n in m.items:
                # 通过判断排除没有IP地址的CNAME对象
                if n.rdtype == 1:
                   print('IP地址：',n.address)
    except Exception as e:
       print(e)
    print('*******别名记录解析*********')
    try:
      CNAME = dns.resolver.resolve(domain,'CNAME')    # 解析类型为CNAME记录
      for m in CNAME.response.answer:
          for n in m.items:
            print('别名：',n.to_text())
    except Exception as e:
       print(e)
    print('*******邮件服务器记录解析*********')
    try:
       MX = dns.resolver.resolve(domain, 'MX')  # 解析类型为MX记录
       for m in MX:
         print('邮件服务器：', m.exchange, '优先级：', m.preference)
    except Exception as e:
        print(e)
    print('*******名称服务器记录解析*********')
    try:
        NS = dns.resolver.resolve(domain, 'NS')  # 解析类型为NS记录
        for m in NS.response.answer:
            for n in m.items:
                print('名称服务器：',m.to_text())
    except Exception as e:
       print(e)
