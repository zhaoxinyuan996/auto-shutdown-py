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
    line.setGeometry(100, 80, 100, 20)
    line.setValidator(range_9999)


def ui_tab_fac_3(self):
    n = 25
    left = 100
    label = BaseQt(QLabel, self.ta2.ta3, name='la1')
    label.setText('年')
    label.setGeometry(left, 15, 80, 20)
    label = BaseQt(QLabel, self.ta2.ta3, name='la2')
    label.setText('月份')
    label.setGeometry(left, 15 + n * 1, 80, 20)
    label = BaseQt(QLabel, self.ta2.ta3, name='la3')
    label.setText('星期')
    label.setGeometry(left, 15 + n * 2, 80, 20)
    label = BaseQt(QLabel, self.ta2.ta3, name='la4')
    label.setText('日')
    label.setGeometry(left, 15 + n * 3, 80, 20)
    label = BaseQt(QLabel, self.ta2.ta3, name='la5')
    label.setText('时')
    label.setGeometry(left, 15 + n * 4, 80, 20)
    label = BaseQt(QLabel, self.ta2.ta3, name='la6')
    label.setText('分')
    label.setGeometry(left, 15 + n * 5, 80, 20)
    label = BaseQt(QLabel, self.ta2.ta3, name='la7')
    label.setText('秒')
    label.setGeometry(left, 15 + n * 6, 80, 20)
    left = 130
    tick = BaseQt(QCheckBox, self.ta2.ta3, name='ti1')
    tick.setGeometry(left, 15, 30, 20)
    tick.clicked.connect(partial(ta2_ta3_tick_click, '1', self.ta2.ta3))
    tick = BaseQt(QCheckBox, self.ta2.ta3, name='ti2')
    tick.setGeometry(left, 15 + n * 1, 30, 20)
    tick.clicked.connect(partial(ta2_ta3_tick_click, '2', self.ta2.ta3))
    tick = BaseQt(QCheckBox, self.ta2.ta3, name='ti3')
    tick.setGeometry(left, 15 + n * 2, 30, 20)
    tick.clicked.connect(partial(ta2_ta3_tick_click, '3', self.ta2.ta3))
    tick = BaseQt(QCheckBox, self.ta2.ta3, name='ti4')
    tick.setGeometry(left, 15 + n * 3, 30, 20)
    tick.clicked.connect(partial(ta2_ta3_tick_click, '4', self.ta2.ta3))
    tick = BaseQt(QCheckBox, self.ta2.ta3, name='ti5')
    tick.setGeometry(left, 15 + n * 4, 30, 20)
    tick.clicked.connect(partial(ta2_ta3_tick_click, '5', self.ta2.ta3))
    tick = BaseQt(QCheckBox, self.ta2.ta3, name='ti6')
    tick.setGeometry(left, 15 + n * 5, 30, 20)
    tick.clicked.connect(partial(ta2_ta3_tick_click, '6', self.ta2.ta3))
    tick = BaseQt(QCheckBox, self.ta2.ta3, name='ti7')
    tick.setGeometry(left, 15 + n * 6, 30, 20)
    tick.clicked.connect(partial(ta2_ta3_tick_click, '7', self.ta2.ta3))
    left = 160
    te = BaseQt(QLineEdit, self.ta2.ta3, name='te1')
    te.setGeometry(left, 15, 40, 20)

    te = BaseQt(QLineEdit, self.ta2.ta3, name='te2')
    te.setGeometry(left, 15 + n * 1, 40, 20)

    te = BaseQt(QLineEdit, self.ta2.ta3, name='te3')
    te.setGeometry(left, 15 + n * 2, 40, 20)

    te = BaseQt(QLineEdit, self.ta2.ta3, name='te4')
    te.setGeometry(left, 15 + n * 3, 40, 20)

    te = BaseQt(QLineEdit, self.ta2.ta3, name='te5')
    te.setGeometry(left, 15 + n * 4, 40, 20)

    te = BaseQt(QLineEdit, self.ta2.ta3, name='te6')
    te.setGeometry(left, 15 + n * 5, 40, 20)

    te = BaseQt(QLineEdit, self.ta2.ta3, name='te7')
    te.setGeometry(left, 15 + n * 6, 40, 20)
