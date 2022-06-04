from functools import partial

from PyQt5.QtWidgets import QTabWidget, QWidget


def wrap(cls):
    """new方法写工厂模式挺乱的，各种继承容易出问题，这里用装饰器实现"""
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
    def add_tab(self: QWidget, p1, p2, name=''):
        setattr(self, name, p1)
        QTabWidget.addTab(self, p1, p2)
