from PyInstaller.utils.hooks import copy_metadata


# 这些包需要手动添加
datas = copy_metadata('apscheduler') + copy_metadata('six') + copy_metadata('tzlocal') + copy_metadata('pytz')

# mark
# --additional-hooks-dir=.
#  -F 单文件，-w 不生成控制台


# 这里会维护一份job和ui必须要的打包的包，全打包体积太大吃不消
#   job

#   ui
