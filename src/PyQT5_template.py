import sys

from PyQt5 import uic
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QComboBox, QPushButton, QShortcut,
QHBoxLayout, QVBoxLayout, QSizePolicy, QMainWindow, QAction, QLabel, QTextEdit, QLCDNumber, QCheckBox, QPlainTextEdit


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calc.ui', self)
        self.setWindowTitle('')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())