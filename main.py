import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from functools import partial
from ui.any_ui import err_ui


class StackedExample(QWidget):
    def __init__(self):

        super().__init__()
        self.setGeometry(300, 500, 10, 10)
        self.setWindowTitle("自动关机")

        self.list = QListWidget()
        self.list.insertItem(0, "关机")
        self.list.insertItem(1, "重启")
        self.list.insertItem(2, "休眠")

        self.stack1 = QWidget()
        self.stack = QStackedWidget()
        # 将界面添加到窗口上
        self.stack.addWidget(self.stack1)

        hbox = QHBoxLayout()
        hbox.addWidget(self.list)
        hbox.addWidget(self.stack)
        self.setLayout(hbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = StackedExample()
    main.show()
    sys.exit(app.exec_())
