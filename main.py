import sys
from time import strftime
from PyQt5.QtWidgets import *
from functools import partial
from ui.any_qt import Entry, ta2_ta2_tick_click
from ui.base_qt import BaseQt
from common import range_99, range_24, range_60, range_9999
from script import cd_to_sec


class StackedExample(QWidget):
    def __init__(self):
        super().__init__()
        self.size_shadow = [1000, 800]
        self.resize(*self.size_shadow)
        self.setWindowTitle("自动关机")

        self.entry = Entry(self)

        self.ui_tab_act()
        self.ui_tab_fac()
        self.ui_btn()

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
        tab_act.addTab(QWidget(), "局域网", name='ta5')
        tab_act.addTab(QWidget(), "自定义", name='ta6')
        print(tab_act.tabText(tab_act.currentIndex()))

    def ui_tab_fac(self):
        """下面相关ui"""
        tab_fac = BaseQt(QTabWidget, self, 'ta2')
        tab_fac.setGeometry(0, 300, 1000, 460)

        tab_fac.addTab(QWidget(), "倒计时", name='ta1')
        tab_fac.addTab(QWidget(), "定时", name='ta2')
        tab_fac.addTab(QWidget(), "自定义", name='ta3')
        self.ta2.ta1.time = 0
        self.ui_tab_fac_1()
        self.ui_tab_fac_2()

    def ui_tab_fac_1(self):
        """倒计时ui"""
        label = BaseQt(QLabel, self.ta2.ta1, name='la1')
        label.setText('天      时      分      秒')
        label.setGeometry(200, 100, 800, 40)

        label = BaseQt(QLabel, self.ta2.ta1, name='la2')
        label.setText('换算成秒：')
        label.setGeometry(200, 300, 150, 40)

        label = BaseQt(QLabel, self.ta2.ta1, name='la3')
        label.setText('0')
        label.setGeometry(320, 300, 800, 40)

        label = BaseQt(QLabel, self.ta2.ta1, name='la4')
        label.setText('预计时间：')
        label.setGeometry(200, 350, 150, 40)

        label = BaseQt(QLabel, self.ta2.ta1, name='la5')
        label.setText(strftime('%Y-%m-%d %H:%M:%S'))
        label.setGeometry(320, 350, 800, 40)

        te1 = BaseQt(QLineEdit, self.ta2.ta1, name='te1')
        te1.setGeometry(150, 100, 50, 40)
        te1.setValidator(range_99)

        te2 = BaseQt(QLineEdit, self.ta2.ta1, name='te2')
        te2.setGeometry(150 + 95 * 1, 100, 50, 40)
        te2.setValidator(range_24)

        te3 = BaseQt(QLineEdit, self.ta2.ta1, name='te3')
        te3.setGeometry(150 + 95 * 2, 100, 50, 40)
        te3.setValidator(range_60)

        te4 = BaseQt(QLineEdit, self.ta2.ta1, name='te4')
        te4.setGeometry(150 + 95 * 3, 100, 50, 40)
        te4.setValidator(range_60)

        # 绑定修改事件
        te1.textChanged.connect(partial(cd_to_sec, self.ta2.ta1))
        te2.textChanged.connect(partial(cd_to_sec, self.ta2.ta1))
        te3.textChanged.connect(partial(cd_to_sec, self.ta2.ta1))
        te4.textChanged.connect(partial(cd_to_sec, self.ta2.ta1))

    def ui_tab_fac_2(self):
        label = BaseQt(QLabel, self.ta2.ta2, name='l1')
        label.setText('年\n\n月份\n\n星期\n\n日\n\n时\n\n分\n\n秒')
        label.setGeometry(200, 20, 80, 400)

        n = 54
        tick = BaseQt(QCheckBox, self.ta2.ta2, name='ti1')
        tick.setGeometry(150, 32, 50, 50)
        tick.clicked.connect(partial(ta2_ta2_tick_click, '1', self.ta2.ta2))
        tick = BaseQt(QCheckBox, self.ta2.ta2, name='ti2')
        tick.setGeometry(150, 32 + n * 1, 50, 50)
        tick.clicked.connect(partial(ta2_ta2_tick_click, '2', self.ta2.ta2))
        tick = BaseQt(QCheckBox, self.ta2.ta2, name='ti3')
        tick.setGeometry(150, 32 + n * 2, 50, 50)
        tick.clicked.connect(partial(ta2_ta2_tick_click, '3', self.ta2.ta2))
        tick = BaseQt(QCheckBox, self.ta2.ta2, name='ti4')
        tick.setGeometry(150, 32 + n * 3, 50, 50)
        tick.clicked.connect(partial(ta2_ta2_tick_click, '4', self.ta2.ta2))
        tick = BaseQt(QCheckBox, self.ta2.ta2, name='ti5')
        tick.setGeometry(150, 32 + n * 4, 50, 50)
        tick.clicked.connect(partial(ta2_ta2_tick_click, '5', self.ta2.ta2))
        tick = BaseQt(QCheckBox, self.ta2.ta2, name='ti6')
        tick.setGeometry(150, 32 + n * 5, 50, 50)
        tick.clicked.connect(partial(ta2_ta2_tick_click, '6', self.ta2.ta2))
        tick = BaseQt(QCheckBox, self.ta2.ta2, name='ti7')
        tick.setGeometry(150, 32 + n * 6, 50, 50)
        tick.clicked.connect(partial(ta2_ta2_tick_click, '7', self.ta2.ta2))

        te = BaseQt(QLineEdit, self.ta2.ta2, name='te1')
        te.setGeometry(270, 38, 100, 40)
        te.setValidator(range_9999)

        te = BaseQt(QLineEdit, self.ta2.ta2, name='te2')
        te.setGeometry(270, 38 + n * 1, 50, 40)
        te.setValidator(range_99)

        te = BaseQt(QLineEdit, self.ta2.ta2, name='te3')
        te.setGeometry(270, 38 + n * 2, 50, 40)
        te.setValidator(range_99)

        te = BaseQt(QLineEdit, self.ta2.ta2, name='te4')
        te.setGeometry(270, 38 + n * 3, 50, 40)
        te.setValidator(range_99)

        te = BaseQt(QLineEdit, self.ta2.ta2, name='te5')
        te.setGeometry(270, 38 + n * 4, 50, 40)
        te.setValidator(range_99)

        te = BaseQt(QLineEdit, self.ta2.ta2, name='te6')
        te.setGeometry(270, 38 + n * 5, 50, 40)
        te.setValidator(range_99)

        te = BaseQt(QLineEdit, self.ta2.ta2, name='te7')
        te.setGeometry(270, 38 + n * 6, 50, 40)
        te.setValidator(range_99)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = StackedExample()
    main.show()
    sys.exit(app.exec_())
