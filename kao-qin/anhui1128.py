# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anhui1128.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(951, 699)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.topWidget = QtWidgets.QWidget(self.centralwidget)
        self.topWidget.setStyleSheet("")
        self.topWidget.setObjectName("topWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.topWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.topFirstLabel = QtWidgets.QLabel(self.topWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.topFirstLabel.setFont(font)
        self.topFirstLabel.setAutoFillBackground(False)
        self.topFirstLabel.setStyleSheet("")
        self.topFirstLabel.setObjectName("topFirstLabel")
        self.horizontalLayout_2.addWidget(self.topFirstLabel)
        self.topSecondLabel = QtWidgets.QLineEdit(self.topWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.topSecondLabel.setFont(font)
        self.topSecondLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.topSecondLabel.setReadOnly(True)
        self.topSecondLabel.setObjectName("topSecondLabel")
        self.horizontalLayout_2.addWidget(self.topSecondLabel)
        self.topThirdLabel = QtWidgets.QLabel(self.topWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.topThirdLabel.setFont(font)
        self.topThirdLabel.setObjectName("topThirdLabel")
        self.horizontalLayout_2.addWidget(self.topThirdLabel)
        self.gridLayout.addWidget(self.topWidget, 0, 0, 1, 1)
        self.middleWidget = QtWidgets.QWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setKerning(False)
        self.middleWidget.setFont(font)
        self.middleWidget.setStyleSheet("")
        self.middleWidget.setObjectName("middleWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.middleWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.middleLefetWidget = QtWidgets.QWidget(self.middleWidget)
        self.middleLefetWidget.setMinimumSize(QtCore.QSize(400, 0))
        self.middleLefetWidget.setObjectName("middleLefetWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.middleLefetWidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.departMembertatWidget = QtWidgets.QWidget(self.middleLefetWidget)
        self.departMembertatWidget.setObjectName("departMembertatWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.departMembertatWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.departMembertatLabel = QtWidgets.QLabel(self.departMembertatWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.departMembertatLabel.setFont(font)
        self.departMembertatLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.departMembertatLabel.setAutoFillBackground(False)
        self.departMembertatLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.departMembertatLabel.setObjectName("departMembertatLabel")
        self.verticalLayout.addWidget(self.departMembertatLabel, 0, QtCore.Qt.AlignHCenter)
        self.departMembertatLine = QtWidgets.QFrame(self.departMembertatWidget)
        self.departMembertatLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.departMembertatLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.departMembertatLine.setObjectName("departMembertatLine")
        self.verticalLayout.addWidget(self.departMembertatLine)
        self.verticalLayout_4.addWidget(self.departMembertatWidget)
        self.memberStatWidget = QtWidgets.QWidget(self.middleLefetWidget)
        self.memberStatWidget.setObjectName("memberStatWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.memberStatWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.memberStatWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.memberStatCountLable = QtWidgets.QLabel(self.memberStatWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.memberStatCountLable.setFont(font)
        self.memberStatCountLable.setObjectName("memberStatCountLable")
        self.horizontalLayout.addWidget(self.memberStatCountLable)
        self.verticalLayout_4.addWidget(self.memberStatWidget)
        self.enterCountStatWidWget = QtWidgets.QWidget(self.middleLefetWidget)
        self.enterCountStatWidWget.setObjectName("enterCountStatWidWget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.enterCountStatWidWget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.enterCountStatLaBel = QtWidgets.QLabel(self.enterCountStatWidWget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.enterCountStatLaBel.setFont(font)
        self.enterCountStatLaBel.setObjectName("enterCountStatLaBel")
        self.verticalLayout_2.addWidget(self.enterCountStatLaBel)
        self.enterCountStatLine = QtWidgets.QFrame(self.enterCountStatWidWget)
        self.enterCountStatLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.enterCountStatLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.enterCountStatLine.setObjectName("enterCountStatLine")
        self.verticalLayout_2.addWidget(self.enterCountStatLine)
        self.enterCountStatTableWidget = QtWidgets.QTableWidget(self.enterCountStatWidWget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.enterCountStatTableWidget.setFont(font)
        self.enterCountStatTableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.enterCountStatTableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.enterCountStatTableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.enterCountStatTableWidget.setAutoScroll(True)
        self.enterCountStatTableWidget.setShowGrid(False)
        self.enterCountStatTableWidget.setObjectName("enterCountStatTableWidget")
        self.enterCountStatTableWidget.setColumnCount(3)
        self.enterCountStatTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.enterCountStatTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.enterCountStatTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.enterCountStatTableWidget.setHorizontalHeaderItem(2, item)
        self.enterCountStatTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.enterCountStatTableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.enterCountStatTableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.enterCountStatTableWidget.horizontalHeader().setStretchLastSection(True)
        self.enterCountStatTableWidget.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.enterCountStatTableWidget)
        self.verticalLayout_4.addWidget(self.enterCountStatWidWget)
        self.enterCostTimesStatWidwget = QtWidgets.QWidget(self.middleLefetWidget)
        self.enterCostTimesStatWidwget.setObjectName("enterCostTimesStatWidwget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.enterCostTimesStatWidwget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.enterCostTimesStatLabel = QtWidgets.QLabel(self.enterCostTimesStatWidwget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.enterCostTimesStatLabel.setFont(font)
        self.enterCostTimesStatLabel.setObjectName("enterCostTimesStatLabel")
        self.verticalLayout_3.addWidget(self.enterCostTimesStatLabel)
        self.enterCostTimesStatLine = QtWidgets.QFrame(self.enterCostTimesStatWidwget)
        self.enterCostTimesStatLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.enterCostTimesStatLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.enterCostTimesStatLine.setObjectName("enterCostTimesStatLine")
        self.verticalLayout_3.addWidget(self.enterCostTimesStatLine)
        self.enterCostTimesStatTableWidwget = QtWidgets.QTableWidget(self.enterCostTimesStatWidwget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.enterCostTimesStatTableWidwget.setFont(font)
        self.enterCostTimesStatTableWidwget.setAutoFillBackground(True)
        self.enterCostTimesStatTableWidwget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.enterCostTimesStatTableWidwget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.enterCostTimesStatTableWidwget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.enterCostTimesStatTableWidwget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.enterCostTimesStatTableWidwget.setShowGrid(False)
        self.enterCostTimesStatTableWidwget.setGridStyle(QtCore.Qt.NoPen)
        self.enterCostTimesStatTableWidwget.setRowCount(0)
        self.enterCostTimesStatTableWidwget.setObjectName("enterCostTimesStatTableWidwget")
        self.enterCostTimesStatTableWidwget.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.enterCostTimesStatTableWidwget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.enterCostTimesStatTableWidwget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.enterCostTimesStatTableWidwget.setHorizontalHeaderItem(2, item)
        self.enterCostTimesStatTableWidwget.horizontalHeader().setCascadingSectionResizes(True)
        self.enterCostTimesStatTableWidwget.horizontalHeader().setDefaultSectionSize(100)
        self.enterCostTimesStatTableWidwget.horizontalHeader().setSortIndicatorShown(True)
        self.enterCostTimesStatTableWidwget.horizontalHeader().setStretchLastSection(True)
        self.enterCostTimesStatTableWidwget.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.enterCostTimesStatTableWidwget)
        self.verticalLayout_4.addWidget(self.enterCostTimesStatWidwget)
        self.horizontalLayout_3.addWidget(self.middleLefetWidget)
        self.middleRightWidget = QtWidgets.QWidget(self.middleWidget)
        self.middleRightWidget.setMinimumSize(QtCore.QSize(500, 0))
        self.middleRightWidget.setObjectName("middleRightWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.middleRightWidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.middleRightFirstLabel = QtWidgets.QLabel(self.middleRightWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.middleRightFirstLabel.setFont(font)
        self.middleRightFirstLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.middleRightFirstLabel.setObjectName("middleRightFirstLabel")
        self.verticalLayout_6.addWidget(self.middleRightFirstLabel)
        self.middleRightSecondLine = QtWidgets.QFrame(self.middleRightWidget)
        self.middleRightSecondLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.middleRightSecondLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.middleRightSecondLine.setObjectName("middleRightSecondLine")
        self.verticalLayout_6.addWidget(self.middleRightSecondLine)
        self.search_frame = QtWidgets.QFrame(self.middleRightWidget)
        self.search_frame.setMaximumSize(QtCore.QSize(500, 16777215))
        self.search_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.search_frame.setObjectName("search_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.search_frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.search_name_label = QtWidgets.QLabel(self.search_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.search_name_label.setFont(font)
        self.search_name_label.setObjectName("search_name_label")
        self.gridLayout_2.addWidget(self.search_name_label, 0, 0, 1, 1)
        self.search_name_input = QtWidgets.QLineEdit(self.search_frame)
        self.search_name_input.setMaximumSize(QtCore.QSize(100, 16777215))
        self.search_name_input.setObjectName("search_name_input")
        self.gridLayout_2.addWidget(self.search_name_input, 0, 1, 1, 1)
        self.search_depart_label = QtWidgets.QLabel(self.search_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.search_depart_label.setFont(font)
        self.search_depart_label.setObjectName("search_depart_label")
        self.gridLayout_2.addWidget(self.search_depart_label, 0, 2, 1, 1)
        self.search_depart_input = QtWidgets.QLineEdit(self.search_frame)
        self.search_depart_input.setMaximumSize(QtCore.QSize(100, 16777215))
        self.search_depart_input.setObjectName("search_depart_input")
        self.gridLayout_2.addWidget(self.search_depart_input, 0, 3, 1, 1)
        self.search_button = QtWidgets.QPushButton(self.search_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.search_button.setFont(font)
        self.search_button.setObjectName("search_button")
        self.gridLayout_2.addWidget(self.search_button, 0, 4, 1, 1)
        self.verticalLayout_6.addWidget(self.search_frame)
        self.middleRightThirdTable = QtWidgets.QTableWidget(self.middleRightWidget)
        font = QtGui.QFont()
        font.setKerning(True)
        self.middleRightThirdTable.setFont(font)
        self.middleRightThirdTable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.middleRightThirdTable.setAutoFillBackground(True)
        self.middleRightThirdTable.setStyleSheet("")
        self.middleRightThirdTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.middleRightThirdTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.middleRightThirdTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.middleRightThirdTable.setAutoScrollMargin(5)
        self.middleRightThirdTable.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.middleRightThirdTable.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.middleRightThirdTable.setShowGrid(True)
        self.middleRightThirdTable.setObjectName("middleRightThirdTable")
        self.middleRightThirdTable.setColumnCount(9)
        self.middleRightThirdTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.middleRightThirdTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.middleRightThirdTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.middleRightThirdTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.middleRightThirdTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.middleRightThirdTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.middleRightThirdTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.middleRightThirdTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.middleRightThirdTable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.middleRightThirdTable.setHorizontalHeaderItem(8, item)
        self.middleRightThirdTable.horizontalHeader().setCascadingSectionResizes(False)
        self.middleRightThirdTable.horizontalHeader().setDefaultSectionSize(100)
        self.middleRightThirdTable.horizontalHeader().setHighlightSections(True)
        self.middleRightThirdTable.horizontalHeader().setMinimumSectionSize(50)
        self.middleRightThirdTable.horizontalHeader().setSortIndicatorShown(True)
        self.middleRightThirdTable.horizontalHeader().setStretchLastSection(True)
        self.middleRightThirdTable.verticalHeader().setVisible(False)
        self.middleRightThirdTable.verticalHeader().setSortIndicatorShown(True)
        self.verticalLayout_6.addWidget(self.middleRightThirdTable)
        self.horizontalLayout_3.addWidget(self.middleRightWidget)
        self.gridLayout.addWidget(self.middleWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 951, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.menuLoadExcelAction = QtWidgets.QAction(MainWindow)
        self.menuLoadExcelAction.setObjectName("menuLoadExcelAction")
        self.menuQuitAction = QtWidgets.QAction(MainWindow)
        self.menuQuitAction.setObjectName("menuQuitAction")
        self.menu.addAction(self.menuLoadExcelAction)
        self.menu.addSeparator()
        self.menu.addAction(self.menuQuitAction)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.topFirstLabel.setText(_translate("MainWindow", "安集微电子科技（上海）股份有限公司"))
        self.topSecondLabel.setText(_translate("MainWindow", "安集微电子车间人员监控看板"))
        self.topThirdLabel.setText(_translate("MainWindow", "2023年11月27日星期一 18:00:00"))
        self.departMembertatLabel.setText(_translate("MainWindow", "车间人员情况"))
        self.label.setText(_translate("MainWindow", "本周总人数"))
        self.memberStatCountLable.setText(_translate("MainWindow", "0人"))
        self.enterCountStatLaBel.setText(_translate("MainWindow", "进出频繁TOP3"))
        self.enterCountStatTableWidget.setSortingEnabled(True)
        item = self.enterCountStatTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "排名"))
        item = self.enterCountStatTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.enterCountStatTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "次数"))
        self.enterCostTimesStatLabel.setText(_translate("MainWindow", "进出进出TOP3"))
        self.enterCostTimesStatTableWidwget.setSortingEnabled(True)
        item = self.enterCostTimesStatTableWidwget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "排名"))
        item = self.enterCostTimesStatTableWidwget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.enterCostTimesStatTableWidwget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "时间"))
        self.middleRightFirstLabel.setText(_translate("MainWindow", "人员进出详细记录"))
        self.search_name_label.setText(_translate("MainWindow", "姓名："))
        self.search_depart_label.setText(_translate("MainWindow", "部门："))
        self.search_button.setText(_translate("MainWindow", "搜索"))
        self.middleRightThirdTable.setSortingEnabled(True)
        item = self.middleRightThirdTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "工号"))
        item = self.middleRightThirdTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.middleRightThirdTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "部门"))
        item = self.middleRightThirdTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "状态"))
        item = self.middleRightThirdTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "入门状态"))
        item = self.middleRightThirdTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "出门时间"))
        item = self.middleRightThirdTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "进出次数"))
        item = self.middleRightThirdTable.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "累计进出时间"))
        item = self.middleRightThirdTable.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "累计进出时间"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.menuLoadExcelAction.setText(_translate("MainWindow", "载入&Excel"))
        self.menuQuitAction.setText(_translate("MainWindow", "退出"))
