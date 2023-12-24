import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QPushButton
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # QAction是菜单栏、工具栏或者快捷键的动作的组合。
        # 上面三行中，前两行创建了一个图标、一个exit的标签和一个快捷键组合，都执行了一个动作；
        # 第三行，创建了一个状态栏，当鼠标悬停在菜单栏的时候，能显示当前状态。
        exitAct = QAction(QIcon('Ex2.2.jpg'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        # 当执行这个指定的动作时，就触发了一个事件。这个事件跟QApplication的quit()行为相关联，所以这个动作就能终止这个应用。
        exitAct.triggered.connect(qApp.quit)
        # 创建状态栏
        self.statusBar()
        # 创建菜单栏
        # menuBar()创建菜单栏。这里创建了一个菜单栏，并用addMenu()在上面添加了一个File菜单，用addAction()关联了点击退出应用的事件。
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File1')
        fileMenu.addAction(exitAct)
        fileMenu2 = menubar.addMenu('&File2')
        fileMenu2.addAction(exitAct)


        # 创建了两个按钮
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
        # 创建一个水平布局，并增加弹性空间和两个按钮。stretch函数在两个按钮前面增加了一块弹性空间，它会将按钮挤到窗口的右边
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addStretch(1)

        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)

        # 为了布局需要，我们把这个水平布局放到了一个垂直布局盒里面。弹性元素会把水平布局挤到窗口的下边。
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)


        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())