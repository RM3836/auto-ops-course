from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import subprocess
'''自定义事件处理器'''
class FSEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)
    def on_created(self, event):
        if not event.is_directory:
            bak_file(event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            bak_file(event.src_path)

'''备份文件的函数'''
def bak_file(src):
    p = subprocess.Popen("cp " + src + " /bak/", shell=True, stdout=subprocess.PIPE)
    p.communicate()
    if p.returncode==0:
        print("备份上传文件：",src)  # 返回值==0表示运行成功

if __name__ == "__main__":
    path = "/upload"
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
