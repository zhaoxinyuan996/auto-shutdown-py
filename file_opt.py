import os
import sys


call_file =  r'.\python.exe .\backend\auto_job.py'
call_func = os.popen

file = os.path.dirname(__file__ if os.path.basename(sys.executable) == 'python.exe' else sys.argv[0])

# 这里写一些初始化文件相关的，省的打包之后手动新建
path = os.path.join(file, 'config.json')
if not os.path.exists(path):
    with open(path, 'w', encoding='utf-8') as f:
        f.write('[]')

path = os.path.join(file, 'static')
if not os.path.exists(path):
    os.mkdir(path)

path = os.path.join(file, 'remind')
if not os.path.exists(path):
    os.mkdir(path)


class File:
    """统一获取路径"""
    level = {
        'conf': ('config.json', ),
        'log': ('logs.txt', ),
        'ico': ('static', 'auto-shutdown-py.ico')
    }

    def __init__(self, name, **kwargs):
        # 文件类型
        if name in self.level:
            self.real_path = self.get_file_path(name)
        # 文件夹类型
        else:
            self.real_path = name

        self.kwargs = kwargs

    def __enter__(self):
        self._f = open(self.real_path, **self.kwargs)
        return self._f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._f.close()

    def get_file_path(self, name) -> str:
        return os.path.join(file, *self.level[name])

    @staticmethod
    def get_remind(vbs):
        return os.path.join(file, 'remind', vbs)


if __name__ == '__main__':
    f = File.get_remind('vbs.vbs')
    print(f)
