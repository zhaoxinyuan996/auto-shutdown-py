from PyInstaller.utils.hooks import copy_metadata


# 这些包需要手动添加
datas = copy_metadata('apscheduler') + copy_metadata('six') + copy_metadata('tzlocal') + copy_metadata('pytz')

"""
脚本文件不需要性能，无需过度编译，用虚拟环境打包体积比较小
QT文件需要性能，优先照顾性能，无视文件体积
auto_job采用pyinstaller打包，run采用nuitka打包
"""
#   pyinstaller
# --additional-hooks-dir=.
# -F 单文件，-w 不生成控制台
# pyinstaller -Fw --additional-hooks-dir . auto_job.py

#   nuitka
"""
nuitka --standalone --mingw64 --nofollow-imports --plugin-enable=upx --windows-disable-console --plugin-enable=pyqt5 --include-qt-plugins=sensible,styles --follow-import-to=app --output-dir=. run.py
"""

# 这里会维护一份job和ui必须要的打包的包
#   job
# pydantic
# apscheduler 
#   ui
# pydantic
# pyqt5
