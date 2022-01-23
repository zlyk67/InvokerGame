import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('LogIn.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec_())

