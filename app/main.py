import sys

from app.qt.act_qt import ui_tab_act_6, ui_tab_act_5
from app.qt.entry_qt import Entry
from app.qt.base_qt import BaseQt
from app.qt.fac_qt import ui_tab_fac_1, ui_tab_fac_2, ui_tab_fac_3
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QTabWidget


class AutoShutdown(QWidget):
    """这里只写大模块，细分模块在qt文件夹"""
    def __init__(self):
        # todo 禁止缩放窗口
        super().__init__()
        self.size_shadow = [1000, 800]
        self.resize(*self.size_shadow)
        self.setWindowTitle("自动关机")

        self.entry = Entry(self)
        # 初始化ui
        self.ui_tab_act()
        self.ui_tab_fac()
        self.ui_btn()
        # 从文件恢复配置
        self.entry.recovery()

    def ui_btn(self):
        """按钮相关ui"""
        btn = QPushButton(self)
        btn.setText('添加')
        btn.setGeometry(700, 760, 150, 40)
        btn.clicked.connect(self.entry.add_entry)

        btn = QPushButton(self)
        btn.setText('保存')
        btn.setGeometry(850, 760, 150, 40)
        btn.clicked.connect(self.entry.save)

    def ui_tab_act(self):
        """上面相关ui"""
        tab_act = BaseQt(QTabWidget, self, 'ta1')
        tab_act.setGeometry(0, 0, 1000, 300)

        tab_act.addTab(QWidget(), "关机", name='ta1')
        tab_act.addTab(QWidget(), "重启", name='ta2')
        tab_act.addTab(QWidget(), "睡眠", name='ta3')
        tab_act.addTab(QWidget(), "休眠", name='ta4')
        tab_act.addTab(QWidget(), "提醒", name='ta5')
        tab_act.addTab(QWidget(), "命令", name='ta6')
        tab_act.addTab(QWidget(), "自定义", name='ta7')

        ui_tab_act_5(self.ta1.ta5)
        ui_tab_act_6(self.ta1.ta6)

    def ui_tab_fac(self):
        """下面相关ui"""
        tab_fac = BaseQt(QTabWidget, self, 'ta2')
        tab_fac.setGeometry(0, 300, 1000, 460)

        tab_fac.addTab(QWidget(), "倒计时", name='ta1')
        tab_fac.addTab(QWidget(), "间隔", name='ta2')
        tab_fac.addTab(QWidget(), "定时", name='ta3')

        ui_tab_fac_1(self)
        ui_tab_fac_2(self)
        ui_tab_fac_3(self)


def main():
    _app = QApplication(sys.argv)
    _main = AutoShutdown()
    _main.show()
    sys.exit(_app.exec_())


if __name__ == "__main__":
    main()
