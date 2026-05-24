import os
from yaml import safe_load
import jinja2
''' 读取YMAL文件的数据，并转换成字典 '''
def get_data_from_yaml(filename):
    with open(filename, 'r') as f:
        content = f.read()
    data = safe_load(content)
    return data
''' 定义使用文件系统加载器的模板渲染函数 '''
def render(tpl_path, **kwargs):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(**kwargs)
if __name__ == '__main__':
    data = get_data_from_yaml('example1.yaml')                   #读取YMAL数据
    data = data['network']                                           #读取network的值
    xml_content=render('net_tmpl.xml',**data )                   # 渲染模板
    with open('net_config.xml', 'w') as f:
         f.write(xml_content)
