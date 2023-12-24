from PyQt5.QtWidgets import (QPushButton, QWidget,
                             QLineEdit, QApplication)
import sys


# 为了完成预定目标，我们要重构一些方法。首先用QPushButton上构造一个按钮实例。
class Button(QPushButton):

    def __init__(self, title, parent):
        super().__init__(title, parent)
        # 激活组件的拖拽事件
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        # 首先，我们重构了dragEnterEvent()方法。设定好接受拖拽的数据类型（plain text）
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()
            # 然后重构dropEvent()方法，更改按钮接受鼠标的释放事件的默认行为

    def dropEvent(self, e):

        self.setText(e.mimeData().text())


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # QLineEdit默认支持拖拽操作，所以我们只要调用setDragEnabled()方法使用就行了。
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button("Button", self)
        button.move(250, 65)

        self.setWindowTitle('Simple drag and drop')
        self.setGeometry(300, 300, 400, 250)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()