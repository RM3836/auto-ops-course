import smtplib


from email.message import EmailMessage

mail_host = "smtp.163.com"    # 设置服务器
mail_user = "XXX"               # 邮箱的用户名（不是完整的邮箱地址）
mail_pass = "WWWWXXXXXXX"  # 邮箱授权密码
sender = "XXX@163.com"            # 发件人地址
receivers = ["XXX@163.com","YYY@qq.com"]  # 收件人地址列表，这里有两个地址

''' 发送文本邮件的函数  '''
def send_textmail(subject,content):
    msg = EmailMessage()
    msg["Subject"] = subject         # 邮件主题
    msg["From"] = sender              # 发件人
    msg["To"] = ",".join(receivers)  # 收件人列表
    msg.set_content(content)          # 邮件体（正文）
    s = smtplib.SMTP()                 # 创建SMTP对象
    try:
        s.connect(mail_host, 25)         # 建立SMTP连接
        s.login(mail_user, mail_pass)   # 提供登录账号和密码
        s.sendmail(sender, receivers, msg.as_string())   # 发送邮件
        print("邮件发送成功！")
    except smtplib.SMTPException as e:
        print(f"发送失败,错误原因：{e}")
    finally:
        s.quit()

