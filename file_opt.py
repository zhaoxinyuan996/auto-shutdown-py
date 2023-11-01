import os
import sys


# run.py/run.exe文件入口，调用后台py
call_file = r'python .\backend\auto_job.py'
call_func = os.popen
# run.py/run.exe文件入口，调用后台exe
# call_file = r'.\auto_job.exe'
# call_func = os.system

if os.path.basename(sys.argv[0]) != 'python.exe':
    call_file = r'.\auto_job.exe'
    call_func = os.system

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


xml_data = r'''<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <Triggers>
    <LogonTrigger>
      <Enabled>true</Enabled>
    </LogonTrigger>
  </Triggers>
  <Principals>
    <Principal id="Author">
      <UserId>S-1-5-21-421013871-1505696746-3855180446-1001</UserId>
      <LogonType>InteractiveToken</LogonType>
      <RunLevel>HighestAvailable</RunLevel>
    </Principal>
  </Principals>
  <Settings>
    <MultipleInstancesPolicy>StopExisting</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>true</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>true</StopIfGoingOnBatteries>
    <AllowHardTerminate>true</AllowHardTerminate>
    <StartWhenAvailable>false</StartWhenAvailable>
    <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
    <IdleSettings>
      <StopOnIdleEnd>true</StopOnIdleEnd>
      <RestartOnIdle>false</RestartOnIdle>
    </IdleSettings>
    <AllowStartOnDemand>true</AllowStartOnDemand>
    <Enabled>true</Enabled>
    <Hidden>false</Hidden>
    <RunOnlyIfIdle>false</RunOnlyIfIdle>
    <WakeToRun>false</WakeToRun>
    <ExecutionTimeLimit>PT72H</ExecutionTimeLimit>
    <Priority>7</Priority>
    <RestartOnFailure>
      <Interval>PT1M</Interval>
      <Count>3</Count>
    </RestartOnFailure>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>auto_job.exe</Command>
      <WorkingDirectory>%s</WorkingDirectory>
    </Exec>
  </Actions>
</Task>'''


def set_startup():
    xml_name = 'auto-job.xml'
    with open(xml_name, 'w', encoding='utf-16') as xml:
        xml.write(xml_data % os.getcwd())


if __name__ == '__main__':
    f = File.get_remind('vbs.vbs')
    print(f)
