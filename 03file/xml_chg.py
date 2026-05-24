from xml.dom import minidom
doc = minidom.parse("example1.xml")  # 读取XML文件生成DOM树
root = doc.documentElement  # 获取根节点
ver = root.getElementsByTagName("ver")[0]  # 获取第1个ver节点对象
ver.childNodes[0].nodeValue = 2.0  # 获取第1个ver节点的内容
cd = doc.createElement("cd")  # 创建名称为cd的普通节点
cd.appendChild(doc.createTextNode("dvd"))  # 给cd节点添加内容
mem = root.getElementsByTagName("mem")[0]
root.insertBefore(cd, mem)  # 将新增的cd节点插入mem节点之前
# 在disk节点下添加一个hd子节点
disk = root.getElementsByTagName("disk")[0]
hd = doc.createElement("hd")
hd.setAttribute("no", "004")
type = doc.createElement("type")
type.appendChild(doc.createTextNode("ssd"))
cp = doc.createElement('capacity')
cp.appendChild(doc.createTextNode("500M"))
hd.appendChild(type)
hd.appendChild(cp)
disk.appendChild(hd)
# 使用writexml()方法将修改后的DOM树写入文件
with open('example2.xml', 'w', encoding='utf-8') as f:
    doc.writexml(f, addindent='', encoding='utf-8')
