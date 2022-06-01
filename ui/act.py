import sys

from PyQt5.QtWidgets import QWidget, QApplication, QListWidget, QStackedWidget, QHBoxLayout, QPushButton

from ui.any_ui import err_ui


class ActTab(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 50, 10, 10)
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


        self.test = QPushButton()
        self.test.clicked.connect(err_ui.show())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = ActTab()
    main.show()
    sys.exit(app.exec_())