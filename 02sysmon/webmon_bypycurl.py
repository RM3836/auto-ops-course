# -*- coding: utf-8 -*-
import os
import sys
import pycurl

Web_URL = "https://www.baidu.com"
c = pycurl.Curl()
c.setopt(pycurl.URL, Web_URL)    # 设置要连接的URL
c.setopt(pycurl.CONNECTTIMEOUT, 5)  # 连接前等待时间
c.setopt(pycurl.TIMEOUT, 5)  # 连接超时时间
c.setopt(pycurl.FORBID_REUSE, 1)  # 禁止重用
c.setopt(pycurl.MAXREDIRS, 5)  # 允许5级重定向
c.setopt(pycurl.NOPROGRESS, 1)  # 禁止下载进度条
c.setopt(pycurl.DNS_CACHE_TIMEOUT, 30)  # DNS缓存过期事件
# 打开一个文件记录返回的网页头部
head_file = open(os.path.dirname(os.path.realpath(__file__)) + "/head.txt", "wb")
c.setopt(pycurl.WRITEHEADER, head_file)
# 将返回的网页内容输出到空设备文件,以免其输出到控制台
fnull = open('/dev/null', 'wb')
c.setopt(pycurl.WRITEDATA, fnull)
# 发起会话执行传输任务
try:
    c.perform()
except Exception as e:
    print("链接错误connecion error:" + str(e))
    head_file.close()
    fnull.close()
    c.close()
    sys.exit()

'''汇集返回的信息'''
def gather_data():
    effective_url = c.getinfo(pycurl.EFFECTIVE_URL)
    http_code = c.getinfo(c.HTTP_CODE)
    content_type = c.getinfo(c.CONTENT_TYPE)
    namelookup_time = c.getinfo(c.NAMELOOKUP_TIME)
    connect_time = c.getinfo(c.CONNECT_TIME)
    pretransfer_time = c.getinfo(c.PRETRANSFER_TIME)
    starttransfer_time = c.getinfo(c.STARTTRANSFER_TIME)
    total_time = c.getinfo(c.TOTAL_TIME)
    size_download = c.getinfo(c.SIZE_DOWNLOAD)
    header_size = c.getinfo(c.HEADER_SIZE)
    content_length_download = c.getinfo(c.CONTENT_LENGTH_DOWNLOAD)
    speed_download = c.getinfo(c.SPEED_DOWNLOAD)
    c.close()
    head_file.close()
    return dict(effective_url=effective_url, http_code=http_code, content_type=content_type,
                namelookup_time=namelookup_time,
                connect_time=connect_time, pretransfer_time=pretransfer_time, starttransfer_time=starttransfer_time,
                total_time=total_time, size_download=size_download, header_size=header_size,
                content_length_download=content_length_download,
                speed_download=speed_download)
'''输出报告'''
def report():
    data = gather_data()
    print("网页地址：%s" % (data["effective_url"]))
    print("HTTP状态码：%s" % (data["http_code"]))
    print("请求内容类型：%s" % (data["content_type"]))
    print("域名解析时间：%.2f ms" % (data["namelookup_time"] * 1000))
    print("连接建立时间：%.2f ms" % (data["connect_time"] * 1000))
    print("准备传输时间：%.2f ms" % (data["pretransfer_time"] * 1000))
    print("传输开始时间：%.2f ms" % (data["starttransfer_time"] * 1000))
    print("请求总时间：%.2f ms" % (data["total_time"] * 1000))
    print("下载数据包大小：%.2f MB" % (data["size_download"] / 1024))
    print("HTTP头部大小：%.2f MB" % (data["header_size"] / 1204))
    print("下载内容长度：%.2f MB" % (data["content_length_download"] / 1204))
    print("平均下载速度：%.2f MB/s" % (data["speed_download"] / 1024))

if __name__ == '__main__':
    report()
