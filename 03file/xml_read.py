from xml.dom import minidom
doc = minidom.parse("example1.xml")              # 读取XML文件获取XML文档对象
root = doc.documentElement                         # 获取DOM根节点
print("            配置清单")
print("用途:", root.getAttribute("purpose"))    # 获取根节点的属性值
type = root.getElementsByTagName("type")[0]    # 获取根节点下面第1个type节点
print("类别：", type.firstChild.data)             # 获取type节点的文本内容
ver = root.getElementsByTagName("ver")[0]
print("版本：", ver.childNodes[0].nodeValue)
mems = root.getElementsByTagName("mem")
print("内存：", mems[0].childNodes[0].data)
disks = root.getElementsByTagName("disk")      # 获取根节点disk节点集合
hds = disks[0].getElementsByTagName("hd")      # 获取disk节点下的hd子节点集合
print("硬盘数量：", len(hds))
for hd in hds:                                         # 遍历hd子节点集合
    no = hd.getAttribute("no")                       # 获取hd子节点的no属性值
    type = hd.getElementsByTagName("type")[0]     # 获取hd子节点的type节点
    cp = hd.getElementsByTagName("capacity")[0]   # 获取hd子节点的capacity节点
    print("  编号:%s, 类型:%s, 容量:%s" %
          (no, type.firstChild.data, cp.firstChild.data))
