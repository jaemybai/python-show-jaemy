from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QFont, QPen
from PyQt5.QtCore import Qt
import sys, random


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 190)
        self.setWindowTitle('Points')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self, qp):
        # 设置笔的颜色为红色，使用的是预定义好的颜色。
        pen = QPen(Qt.red, 3, Qt.SolidLine)

        qp.setPen(pen)
        qp.setFont(QFont('Decorative', 20))

        # 每次更改窗口大小，都会产生绘画事件，从size()方法里获得当前窗口的大小，然后把产生的点随机的分配到窗口的所有位置上。
        size = self.size()

        for i in range(1000):
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            # drawPoint()方法绘图。
            qp.drawPoint(x, y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())