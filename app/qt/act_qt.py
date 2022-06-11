from app.qt.base_qt import BaseQt
from PyQt5.QtWidgets import QLabel, QLineEdit, QCheckBox


def ui_tab_act_3(self):
    label = BaseQt(QLabel, self, 'la1')
    label.setText('提醒语')
    label.setGeometry(50, 20, 300, 20)

    line = BaseQt(QLineEdit, self, 'li1')
    line.setGeometry(50, 40, 300, 20)

    tick = BaseQt(QCheckBox, self, name='ti1')
    tick.setGeometry(50, 80, 100, 20)
    tick.setText('无限提示')


def ui_tab_act_4(self):
    label = BaseQt(QLabel, self, 'la1')
    label.setText('cmd命令：')
    label.setGeometry(50, 30, 100, 20)

    line = BaseQt(QLineEdit, self, 'li1')
    line.setGeometry(50, 60, 300, 20)
