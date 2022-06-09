# conf.json remind logs.txt
import os
import sys


file = os.path.dirname(__file__ if os.path.basename(sys.executable) == 'python.exe' else sys.argv[0])


class File:
    """统一获取路径"""
    level = {
        'conf': ('config.json', ),
        'log': ('logs.txt', )
    }

    def __init__(self, name, **kwargs):
        if name in self.level:
            self.real_path = self.get_file_path(name)
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
