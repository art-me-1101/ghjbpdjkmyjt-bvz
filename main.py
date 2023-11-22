import sys
import random

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from UI import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        self.setupUi(self)
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
        for i in range(7):
            c = (random.randint(1, 255) for _ in range(3))
            qp.setBrush(QColor(*c))
            qp.setPen(QColor(*c))
            a = random.randint(30, 300)
            x = random.randint(0, self.size().width() - a)
            y = random.randint(0, self.size().height() - a)
            qp.drawEllipse(x, y, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
