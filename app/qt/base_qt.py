import os
from file_opt import File
from hashlib import sha256
from functools import partial
from PyQt5.QtWidgets import QTabWidget, QWidget


def wrap(cls):
    """new方法做工厂模式在此场景不合适，这里用装饰器实现比较方便"""
    def f(qt, base, name=''):
        qt_obj = qt(base)
        setattr(base, name, qt_obj)

        if qt is QTabWidget:
            qt_obj.addTab = partial(cls.add_tab, qt_obj)
        return qt_obj
    return f


@wrap
class BaseQt:
    """通过.语法调用子控件，把所有控件都命名会很乱"""

    def __init__(self): ...

    def add_tab(self: QWidget, p1, p2, name=''):
        setattr(self, name, p1)
        QTabWidget.addTab(self, p1, p2)


def get_hook_class(hook_name, *args, **kwargs):
    if hook_name == 'remind':
        return RemindHook(*args, **kwargs)
    return BaseHook()


def single_obj(cls):
    def f(*args, **kwargs):
        if not hasattr(cls, 'single'):
            single = cls(*args, **kwargs)
            cls.single = single
        return cls.single
    return f


@single_obj
class BaseHook:
    """hook"""


@single_obj
class RemindHook:
    """提醒功能hook"""
    def __init__(self, *args, **kwargs):
        ...

    def delete(self):
        """删除顺便删文件"""

    def recovery(self):
        """恢复"""
