import os
import socket
import jinja2
from datetime import datetime
# 导入sysinfo_bypsutil模块
from sysinfo_bypsutil import gather_monitor_data
''' 定义使用文件系统加载器的模板渲染函数 '''
def render(tpl_path, **kwargs):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(**kwargs)
if __name__ == '__main__':
    host_name = socket.gethostname()                              # 获取主机名
    test_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # 获取当前时间
    data = gather_monitor_data()                                   # 获取系统信息
    data.update(dict(host_name=host_name))
    data.update(dict(test_time=test_time))
    html_content = render('rpt_tmpl.html', **data)              # 渲染模板
    file_name="sysinfo-"+test_time+".html"                        # HTML文件名
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(html_content)
