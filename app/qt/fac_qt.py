from time import strftime
from functools import partial
from app.script import cd_to_sec
from app.qt.base_qt import BaseQt
from app.qt.any_qt import ta2_ta3_tick_click
from PyQt5.QtWidgets import QLabel, QLineEdit, QCheckBox
from app.common import range_99, range_24, range_60, range_9999


def ui_tab_fac_1(self):
    """倒计时ui"""
    self.ta2.ta1.shift = 0
    label = BaseQt(QLabel, self.ta2.ta1, name='la1')
    label.setText('天      时      分      秒')
    label.setGeometry(100, 50, 300, 20)

    label = BaseQt(QLabel, self.ta2.ta1, name='la2')
    label.setText('换算成秒：')
    label.setGeometry(70, 120, 100, 20)

    label = BaseQt(QLabel, self.ta2.ta1, name='la3')
    label.setText('0')
    label.setGeometry(140, 120, 200, 20)

    label = BaseQt(QLabel, self.ta2.ta1, name='la4')
    label.setText('预计时间：')
    label.setGeometry(70, 150, 100, 20)

    label = BaseQt(QLabel, self.ta2.ta1, name='la5')
    label.setText(strftime('%Y-%m-%d %H:%M:%S'))
    label.setGeometry(140, 150, 200, 20)

    te1 = BaseQt(QLineEdit, self.ta2.ta1, name='te1')
    te1.setGeometry(70, 50, 30, 20)
    te1.setValidator(range_99)

    n = 48
    te2 = BaseQt(QLineEdit, self.ta2.ta1, name='te2')
    te2.setGeometry(70 + n * 1, 50, 30, 20)
    te2.setValidator(range_24)

    te3 = BaseQt(QLineEdit, self.ta2.ta1, name='te3')
    te3.setGeometry(70 + n * 2, 50, 30, 20)
    te3.setValidator(range_60)

    te4 = BaseQt(QLineEdit, self.ta2.ta1, name='te4')
    te4.setGeometry(70 + n * 3, 50, 30, 20)
    te4.setValidator(range_60)

    # 绑定修改事件
    te1.textChanged.connect(partial(cd_to_sec, self.ta2.ta1))
    te2.textChanged.connect(partial(cd_to_sec, self.ta2.ta1))
    te3.textChanged.connect(partial(cd_to_sec, self.ta2.ta1))
    te4.textChanged.connect(partial(cd_to_sec, self.ta2.ta1))


def ui_tab_fac_2(self):
    label = BaseQt(QLabel, self.ta2.ta2, 'la1')
    label.setText('时间间隔(秒)')
    label.setGeometry(100, 50, 150, 20)

    line = BaseQt(QLineEdit, self.ta2.ta2, 'li1')
    line.setGeometry(100, 80, 70, 20)
    line.setValidator(range_9999)


def ui_tab_fac_3(self):
    n = 25
    left = 140
    tick = BaseQt(QCheckBox, self.ta2.ta3, name='ti1')
    tick.setGeometry(left, 15, 200, 20)
    tick.clicked.connect(partial(ta2_ta3_tick_click, '1', self.ta2.ta3))
    tick.setText('每年(1970-9999)')
    tick = BaseQt(QCheckBox, self.ta2.ta3, name='ti2')
    tick.setGeometry(left, 15 + n * 1, 200, 20)
    tick.clicked.connect(partial(ta2_ta3_tick_click, '2', self.ta2.ta3))
    tick.setText('每月(1-12)')
    tick = BaseQt(QCheckBox, self.ta2.ta3, name='ti3')
    tick.setGeometry(left, 15 + n * 2, 200, 20)
    tick.clicked.connect(partial(ta2_ta3_tick_click, '3', self.ta2.ta3))
    tick.setText('周几(0-6)')
    tick = BaseQt(QCheckBox, self.ta2.ta3, name='ti4')
    tick.setGeometry(left, 15 + n * 3, 200, 20)
    tick.clicked.connect(partial(ta2_ta3_tick_click, '4', self.ta2.ta3))
    tick.setText('每日(1-31)')
    tick = BaseQt(QCheckBox, self.ta2.ta3, name='ti5')
    tick.setGeometry(left, 15 + n * 4, 200, 20)
    tick.clicked.connect(partial(ta2_ta3_tick_click, '5', self.ta2.ta3))
    tick.setText('每时(0-23)')
    tick = BaseQt(QCheckBox, self.ta2.ta3, name='ti6')
    tick.setGeometry(left, 15 + n * 5, 200, 20)
    tick.clicked.connect(partial(ta2_ta3_tick_click, '6', self.ta2.ta3))
    tick.setText('每分(0-59)')
    tick = BaseQt(QCheckBox, self.ta2.ta3, name='ti7')
    tick.setGeometry(left, 15 + n * 6, 200, 20)
    tick.clicked.connect(partial(ta2_ta3_tick_click, '7', self.ta2.ta3))
    tick.setText('每秒(0-59)')
    left = 100
    te = BaseQt(QLineEdit, self.ta2.ta3, name='te1')
    te.setGeometry(left, 15, 30, 20)

    te = BaseQt(QLineEdit, self.ta2.ta3, name='te2')
    te.setGeometry(left, 15 + n * 1, 30, 20)

    te = BaseQt(QLineEdit, self.ta2.ta3, name='te3')
    te.setGeometry(left, 15 + n * 2, 30, 20)

    te = BaseQt(QLineEdit, self.ta2.ta3, name='te4')
    te.setGeometry(left, 15 + n * 3, 30, 20)

    te = BaseQt(QLineEdit, self.ta2.ta3, name='te5')
    te.setGeometry(left, 15 + n * 4, 30, 20)

    te = BaseQt(QLineEdit, self.ta2.ta3, name='te6')
    te.setGeometry(left, 15 + n * 5, 30, 20)

    te = BaseQt(QLineEdit, self.ta2.ta3, name='te7')
    te.setGeometry(left, 15 + n * 6, 30, 20)

    label = BaseQt(QLabel, self.ta2.ta3, name='la1')
    label.setGeometry(left + 180, 0, 200, 200)
    label.setText('''cron常用规则：
*或勾选\t通配符,例:秒=*即每秒触发
*/n\t每间隔n触发一次
a-b\t从a到b每个都触发
a,b\t只触发a,b
逗号等必须是英文输入法的符号
以上为常用规则
使用库APscheduler
更多花样请百度[cron规则]''')
