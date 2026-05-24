from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sys
import time
'''自定义事件处理器'''
class FSEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)
    def on_moved(self, event):
        if event.is_directory:
            print("目录{0}移动到{1}".format(event.src_path, event.dest_path))
        else:
            print("文件{0}移动到{1}".format(event.src_path, event.dest_path))
    def on_created(self, event):
        if event.is_directory:
            print("创建目录：{0}".format(event.src_path))
        else:
            print("创建文件：{0}".format(event.src_path))
    def on_deleted(self, event):
        if event.is_directory:
            print("删除目录：{0}".format(event.src_path))
        else:
            print("删除文件：{0}".format(event.src_path))
    def on_modified(self, event):
        if event.is_directory:
            print("修改目录：{0}".format(event.src_path))
        else:
            print("修改文件：{0}".format(event.src_path))

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    observer = Observer()
    event_handler = FSEventHandler()
    observer.schedule(event_handler, path, True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
