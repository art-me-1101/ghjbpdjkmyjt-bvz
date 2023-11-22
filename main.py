import sys
import random

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        uic.loadUi('UI.ui', self)
        self.setupUi()

    def setupUi(self):
        self.pushButton.clicked.connect(self.new_round)

    def new_round(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_round(qp)
            qp.end()
        self.do_paint = False

    def draw_round(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        qp.setPen(QColor(255, 255, 0))
        for i in range(7):
            a = random.randint(1, 100)
            x = random.randint(0, self.size().width())
            y = random.randint(0, self.size().height())
            qp.drawEllipse(x, y, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
