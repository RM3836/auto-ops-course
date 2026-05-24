import sys
import pyinotify
'''定制事件处理类'''
class EventHandler(pyinotify.ProcessEvent):
    # 定制所需的事件处理函数
    def process_IN_CREATE(self, event):
        #event.pathname表示触发事件的文件路径
        if event.dir:
            print("创建目录：",format(event.pathname))
        else:
            print("创建文件：",format(event.pathname))
    def process_IN_DELETE(self, event):
        if event.dir:
            print("删除目录：",format(event.pathname))
        else:
            print("删除文件：",format(event.pathname))
    def process_IN_MODIFY(self, event):
        if event.dir:
            print("修改目录：", format(event.pathname))
        else:
            print("修改文件：",format(event.pathname))
'''文件系统变化监控函数，参数path为要监控的文件或目录路径'''
def fs_monitor(path):
    wm = pyinotify.WatchManager()
    # 指定要监控的事件
    mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE | pyinotify.IN_MODIFY
    wm.add_watch(path, mask, rec=True)
    print('开始监控%s...' % path)
    # 创建事件处理器（event handler）
    handler = EventHandler()
    # 创建Notifier对象时传入该事件处理器
    notifier = pyinotify.Notifier(wm, handler)
    notifier.loop()
if __name__ == '__main__':
    # 监控目录可以由命令行参数提供，如果不提供则监控当前目录
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    fs_monitor(path)

