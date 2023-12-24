import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        # 创建了两个按钮
        okButton = QPushButton("Top1")
        cancelButton = QPushButton("Top2")
        Top3Button = QPushButton("Top3")

        middleLeft1Button = QPushButton("middleLeft1Button")
        middleLeft2Button = QPushButton("middleLeft2Button")
        middleLeft3Button = QPushButton("middleLeft3Button")
        middleLeft4Button = QPushButton("middleLeft4Button")

        middleRight1Button = QPushButton("middleRight1Button")



        # 创建一个水平布局，并增加弹性空间和两个按钮。stretch函数在两个按钮前面增加了一块弹性空间，它会将按钮挤到窗口的右边
        topHHox = QHBoxLayout()

        topHHox.addWidget(okButton)
        topHHox.addWidget(cancelButton)
        topHHox.addWidget(Top3Button)

        middleHox = QHBoxLayout()
        middleLeftHox = QVBoxLayout()
        middleLeftHox.addWidget(middleLeft1Button)
        middleLeftHox.addWidget(middleLeft2Button)
        middleLeftHox.addWidget(middleLeft3Button)
        middleLeftHox.addWidget(middleLeft4Button)

        middleHox.addLayout(middleLeftHox)
        middleHox.addWidget(middleRight1Button)

        allVBox = QVBoxLayout()
        allVBox.addLayout(topHHox)
        allVBox.addLayout(middleHox)

        self.setLayout(allVBox)


        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


    def initUI2(self):
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


        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())