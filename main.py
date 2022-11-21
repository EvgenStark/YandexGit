from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
import sys
import random


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('UI.ui', self)
        self.flag = False
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.size = random.randint(10, 100)
        self.color = (255, 255, 0)
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(*self.color))
            qp.setBrush(QColor(*self.color))
            self.x, self.y = random.randint(100, 800 - 100), random.randint(100, 600 - 100)
            qp.drawEllipse(self.x, self.y, self.size, self.size)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec_())
