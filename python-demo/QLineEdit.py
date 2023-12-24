import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
                             QLineEdit, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        # 创建一个QLineEdit对象。
        qle = QLineEdit(self)

        qle.move(60, 100)
        self.lbl.move(60, 40)
        ##如果输入框的值有变化，就调用onChanged()方法
        qle.textChanged[str].connect(self.onChanged)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit')
        self.show()

    # 在onChanged()方法内部，我们把文本框里的值赋值给了标签组件，然后调用adjustSize()方法让标签自适应文本内容。
    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())