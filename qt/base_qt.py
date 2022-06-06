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
