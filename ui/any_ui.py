from PyQt5.QtWidgets import QMessageBox


def err_ui(self, title: str, msg: str):
    QMessageBox.critical(self, title, msg)
