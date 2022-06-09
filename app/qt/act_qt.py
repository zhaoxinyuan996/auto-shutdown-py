from app.qt.base_qt import BaseQt
from PyQt5.QtWidgets import QLabel, QLineEdit, QCheckBox


def ui_tab_act_5(self):
    label = BaseQt(QLabel, self, 'la1')
    label.setText('提醒语')
    label.setGeometry(50, 30, 800, 40)

    label = BaseQt(QLabel, self, 'la2')
    label.setText('无限提示')
    label.setGeometry(80, 130, 100, 40)

    line = BaseQt(QLineEdit, self, 'li1')
    line.setGeometry(50, 80, 800, 40)

    tick = BaseQt(QCheckBox, self, name='ti1')
    tick.setGeometry(50, 126, 50, 50)


def ui_tab_act_6(self):
    label = BaseQt(QLabel, self, 'la1')
    label.setText('cmd命令：')
    label.setGeometry(50, 80, 800, 40)

    line = BaseQt(QLineEdit, self, 'li1')
    line.setGeometry(50, 120, 800, 40)
