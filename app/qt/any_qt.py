from PyQt5.QtCore import Qt
from app.common import power_by
from PyQt5.QtWidgets import QMessageBox


def ta2_ta3_tick_click(tick_no, self):
    """复选框联动文本框，self: base.ta2.ta2"""
    label = getattr(self, f'te{tick_no}')
    flag = getattr(self, f'ti{tick_no}').checkState()
    label.setEnabled(not flag)


def show_power_by():
    QMessageBox(QMessageBox.NoIcon, '关于', power_by).exec_()
