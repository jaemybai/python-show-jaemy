from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QTableWidgetItem
from PyQt5.QtCore import Qt
import sys
import os
import pandas as pd

from forma import Ui_MainWindow

class TableWin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setAcceptDrops(True)   # 设置接受拖曳动作
        self.table_header = ''  # 存储表头
        self.file_path = ''     # 定义文件路径
        self.listener()     # 调用监听函数

    # 监听函数都写在里面
    def listener(self):
        self.choice_btn.clicked.connect(self.choice_file)
        self.open_btn.clicked.connect(self.open_file)
        self.save_btn.clicked.connect(self.save_file)

    def choice_file(self):
        now_path = os.getcwd()  # 获取当前路径
        choice_file_path = QFileDialog.getOpenFileName(self, '选择文件', now_path, 'Excel files(*.xlsx , *.xls)')

        # 如果路径存在，设置文件路径和输入框内容
        if choice_file_path[0]:
            self.file_path = choice_file_path[0]
            self.set_file_path_edt(choice_file_path[0])

    # 打开文件
    def open_file(self):
        # 判断文件路径是否有值(就是有没有选择了文件)
        if self.file_path:
            # 获取文件后缀
            file_format = self.file_path.split('.')[-1]
            # 判断文件格式是否是'xls'或者'xlsx'
            if file_format == 'xls' or file_format == 'xlsx':
                # 使用pandas提取excel数据
                excel_data = pd.read_excel(self.file_path)
                # 获取excel数据行数
                rows = excel_data.shape[0]
                # 获取excel数据列数
                columns = excel_data.shape[1]
                # print(rows, columns)

                # 设置总列数
                self.data_table.setColumnCount(columns)
                # 设置总行数
                self.data_table.setRowCount(rows)
                # 设置表头(excel_data.columns可以获取表头列表，默认第一列为表头)
                self.data_table.setHorizontalHeaderLabels(excel_data.columns)
                # 保存表头数据
                self.table_header = excel_data.columns

                '''遍历excel中的元素，添加到tableWidget里面'''
                # 设置写数据的当前索引(excel中的第二行对应tableWidget中的第一行，索引并不一样，所以要设置新索引跟踪tableWidget中的索引)
                data_table_current = 0

                # 插入值
                for i in range(0, rows):
                    for j in range(columns):
                        # 创建QTableWidgetItem对象，并设置值
                        a=excel_data.iloc[i, j]
                        aa=str(a)
                        new_item = QTableWidgetItem(aa)
                        # 设置QTableWidgetItem对象启用、可以选中和可以编辑
                        new_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable)
                        # 设置QTableWidgetItem对象里面的值水平，垂直居中
                        new_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                        # 将新建的QTableWidgetItem添加到tableWidget中，参数分别是(行索引,列索引,QTableWidgetItem对象)
                        self.data_table.setItem(data_table_current, j, new_item)
                    # 写数据的当前索引加1
                    data_table_current += 1

            else:
                QMessageBox.warning(self, '警告', '请选择xlsx或者xls文件！')
        else:
            QMessageBox.warning(self, '警告', '请选择文件！')

    # 设置输入框里面内容
    def set_file_path_edt(self, file_path):
        self.file_path_edt.setText(file_path)

    # 保存文件
    def save_file(self):
        # 判断文件路径是否有值(就是有没有选择了文件)
        if self.file_path:
            save_file_path = QFileDialog.getSaveFileName(self, '选择保存路径', '', 'xlsx(*.xlsx)')
            # 选择了路径则保存
            if save_file_path[0] == '':
                return
            else:
                try:
                    # 获取当前表的行数列数
                    columns = self.data_table.columnCount()
                    rows = self.data_table.rowCount()

                    index_data = []  # 存储行索引数据，[1, 2, 3, .....]
                    for i in range(rows):
                        index_data.append(i)

                    # 创建空的DataFrame
                    save_data = pd.DataFrame(columns=self.table_header, index=index_data)
                    # 赋值
                    for i in range(rows):
                        for j in range(columns):
                            save_data.iloc[i, j] = self.data_table.item(i, j).text()

                    # 创建excel对象
                    excel = pd.ExcelWriter(save_file_path[0])
                    # 将数据保存到excel中
                    save_data.to_excel(excel, index=None, sheet_name="数据")
                    excel.save()
                    # 提示保存成功
                    QMessageBox.information(self, "成功", "保存成功！", QMessageBox.Yes)
                except:
                    QMessageBox.critical(self, "成功", "保存成功！", QMessageBox.Yes)
        else:
            QMessageBox.warning(self, "警告", "请先打开文件！", QMessageBox.Yes)


    '''重写拖曳方法'''
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            try:
                event.setDropAction(Qt.CopyAction)
            except Exception as e:
                print(e)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.CopyAction)
            event.accept()
            links = []
            for url in event.mimeData().urls():
                links.append(str(url.toLocalFile()))
            self.file_path = links[0]   # 获取文件绝对路径
            self.set_file_path_edt(self.file_path)    # 设置文件绝对路径
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    table_win = TableWin()
    table_win.show()
    sys.exit(app.exec_())
