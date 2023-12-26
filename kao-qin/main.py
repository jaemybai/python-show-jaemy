import sys
import threading
import time
import traceback
from datetime import datetime

import numpy
import pandas
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import QBarSeries, QBarSet, QChart, QChartView, QValueAxis, QBarCategoryAxis, QPieSlice
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QEasingCurve

from anhui1128 import Ui_MainWindow
from MemberInfo import MemberInfo
from MemberStats import MemberStats


def format_time(time):
    if time >= 10:
        return str(time)
    elif time > 0:
        return "0" + str(time)
    else:
        return "00"


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("考勤V1.0")
        self.start_time_for_thread()
        screen_size = QDesktopWidget().screenGeometry()
        width = screen_size.width()
        height = screen_size.height()
        self.middleRightWidget.setMinimumWidth(int(width * 0.5))
        self.middleLefetWidget.setMaximumWidth(int(width / 3))

        self.int_chart_view()
        self.connectSlots()
        self.table_header = ''  # 存储表头
        self.file_path = ''  # 定义文件路径
        self.memberStats = MemberStats()
        self.current_member_info = MemberInfo()

    def start_time_for_thread(self):
        thread = threading.Thread(target=self.run_update_time_for_thread)
        thread.start()

    def run_update_time_for_thread(self):
        while True:
            self.update_time()
            time.sleep(0.5)

    def update_time(self):
        weekday_map = ["一", "二", "三", "四", "五", "六", "日"]
        current_time = datetime.now()

        time_day = str(current_time.year) + "年" + str(current_time.month) + "月" + str(current_time.day) + "日"
        week_day = current_time.weekday()
        time_second = current_time.strftime("%H:%M:%S")
        time_format = time_day + " 星期" + weekday_map[week_day] + " " + time_second
        self.topThirdLabel.setText(time_format)

    def search_table(self):
        if self.memberStats is None or self.memberStats.enter_detail_stat_frame is None:
            return
        enter_detail_stat_frame = self.memberStats.enter_detail_stat_frame

        search_name_input_format = None
        search_depart_input_format = None
        search_name_input = self.search_name_input.text()
        search_depart_input = self.search_depart_input.text()

        if search_name_input is not None and len(search_name_input) > 0:
            search_name_input_format = str(search_name_input).strip()
        if search_depart_input is not None and len(search_depart_input) > 0:
            search_depart_input_format = str(search_depart_input).strip()

        if search_name_input_format is None and search_depart_input_format is None:
            self.load_table_from_data_frame(self.memberStats.enter_detail_stat_frame, self.middleRightThirdTable)
        elif search_name_input_format is not None and search_depart_input_format is not None:
            self.load_table_from_data_frame(
                enter_detail_stat_frame[(enter_detail_stat_frame["姓名"] == search_name_input_format)
                                        & (enter_detail_stat_frame["部门"] == search_depart_input_format)],
                self.middleRightThirdTable)
        elif search_name_input_format is not None:
            self.load_table_from_data_frame(
                enter_detail_stat_frame[enter_detail_stat_frame["姓名"] == search_name_input_format],
                self.middleRightThirdTable)
        else:
            self.load_table_from_data_frame(
                enter_detail_stat_frame[enter_detail_stat_frame["部门"] == search_depart_input_format],
                self.middleRightThirdTable)

    def int_chart_view(self):
        self.chart = QChart()
        self.chart.setBackgroundBrush(QColor(85, 170, 127))
        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.verticalLayout.addWidget(self.chart_view)

    def connectSlots(self):
        """connect slots with buttons/
        """
        self.menuLoadExcelAction.triggered.connect(self.loanExcelData_catch)
        self.menuQuitAction.triggered.connect(self.close)
        self.search_button.clicked.connect(self.search_table)
    def loanExcelData_catch(self):
        try:
            start_date = datetime.strptime("2023-12-27 00:00:00".strip(), "%Y-%m-%d %H:%M:%S")
            current_time = datetime.now()
            time_diff = current_time - start_date
            day = int(time_diff.total_seconds() / 3600 / 24)
            if day >= 8:
                QMessageBox.about(self, '温馨提示', '试用已到期，请联系后台管理员激活！')
                return

            self.loanExcelData()
        except Exception as e:
            traceback.print_exc()
            QMessageBox.about(self, '温馨提示', '文件解析异常！')
            return


    def loanExcelData(self):
        path, _ = QFileDialog.getOpenFileName(
            self, '请选择文件', '', 'excel(*.xlsx *.xls)')
        if not path:
            QMessageBox.about(self, '温馨提示', '请选择xlsx或者xls文件！')
            return
        if _.find('*.xlsx'):
            return self.parseExcel(path)
        if _.find('*.xls'):
            return self.parseExcel(path)

    def parseExcel(self, path):
        if path:
            self.file_path = path
        else:
            QMessageBox.about(self, '温馨提示', '请选择文件！')

        excel_data = pandas.read_excel(self.file_path)
        # 获取excel数据行数
        rows = excel_data.shape[0]
        # 获取excel数据列数
        columns = excel_data.shape[1]
        # 保存表头数据
        member_list = []
        # 插入值
        for i in range(0, rows):
            one_row = []
            for j in range(columns):
                # 创建QTableWidgetItem对象，并设置值
                columnValue = excel_data.iloc[i, j]
                one_row.append(columnValue)

            member_info = MemberInfo()
            member_info.init_info_by_list(one_row)
            member_list.append(member_info)

        try:
            self.memberStats.init_info(rows, columns, excel_data.columns, member_list)
            self.memberStatCountLable.setText(str(self.memberStats.total_members) + "人")
            self.load_table_from_data_frame(self.memberStats.enter_detail_stat_frame, self.middleRightThirdTable)
            self.load_table_from_series(["排名", "姓名", "次数"], self.memberStats.enter_count_stat_series,
                                        self.enterCountStatTableWidget)
            self.load_table_from_series(["排名", "姓名", "时长"], self.memberStats.enter_cost_times_stat_series,
                                        self.enterCostTimesStatTableWidwget)
            self.add_depayment_member_chart(self.memberStats.member_stat_by_department_series)
        except Exception as e:
            traceback.print_exc()
            QMessageBox.about(self, '温馨提示', '文件解析异常！')
            return

    def load_table_from_data_frame(self, data_frame, q_table_widget):
        q_table_widget.clear()
        self.set_table_style(q_table_widget)

        rows_count = data_frame.shape[0]
        column_count = data_frame.shape[1]
        columns = data_frame.columns
        q_table_widget.setColumnCount(column_count)
        # 设置总行数
        q_table_widget.setRowCount(rows_count)
        # 设置表头(excel_data.columns可以获取表头列表，默认第一列为表头)
        # q_table_widget.setHorizontalHeaderLabels(columns)
        self.set_horizontal_header_labels(columns, q_table_widget)

        for row_index in range(0, rows_count):
            for column_index in range(column_count):
                # 创建QTableWidgetItem对象，并设置值
                column_value = data_frame.iloc[row_index, column_index]
                if isinstance(column_value, (numpy.int64, numpy.int32, numpy.float32, numpy.float64)):
                    column_value = int(column_value)
                    column_value = column_value if column_value > 0 else None

                if column_value is None or type(column_value) == type(pandas.NaT):
                    column_value = ""
                elif columns[column_index] == '状态':
                    column_value = "↑" if column_value else "○"
                elif columns[column_index] == '本次进出时间' or columns[column_index] == '累计进出时间':
                    column_value = int(column_value)
                    column_value = self.combine_hour_minute_second(column_value)

                column_value_item = QTableWidgetItem(str(column_value))
                column_value_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                # # 设置QTableWidgetItem对象里面的值水平，垂直居中
                column_value_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                q_table_widget.setItem(row_index, column_index, column_value_item)
                q_table_widget.resizeColumnToContents(column_index)
                q_table_widget.resizeRowToContents(row_index)

    def combine_hour_minute_second(self, second):
        hour = second // 3600
        rest_second = second - hour * 3600
        minute = rest_second // 60
        second = rest_second - minute * 60
        hour_str = format_time(hour)
        minute_str = format_time(minute)
        second_str = format_time(second)
        if hour_str != "00":
            return hour_str + ":" + minute_str + ":" + second_str
        elif minute_str != "00":
            return "00:" + minute_str + ":" + second_str
        else:
            return "00:00:" + second_str

    def load_table_from_series(self, header_labels, data_series, q_table_widget):
        q_table_widget.clear()
        self.set_table_style(q_table_widget)

        q_table_widget.setColumnCount(3)
        # 设置总行数
        q_table_widget.setRowCount(len(data_series.keys()))
        # 设置表头(excel_data.columns可以获取表头列表，默认第一列为表头)
        # q_table_widget.setHorizontalHeaderLabels(header_labels)
        self.set_horizontal_header_labels(header_labels, q_table_widget)
        series_dict = dict(data_series)
        sort_series_dict = dict(sorted(series_dict.items(), key=lambda item: item[1], reverse=True))
        index = 0
        for key, value in sort_series_dict.items():
            self.add_table_item(index, 0, index + 1, q_table_widget)
            self.add_table_item(index, 1, key, q_table_widget)
            column_value = value
            if header_labels[2] == "时长":
                column_value = int(column_value)
                column_value = self.combine_hour_minute_second(column_value)
            self.add_table_item(index, 2, column_value, q_table_widget)
            index = index + 1

    def set_horizontal_header_labels(self, header_labels, q_table_widget):
        for index in range(len(header_labels)):
            item = QtWidgets.QTableWidgetItem()
            item.setText(header_labels[index])
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            q_table_widget.setHorizontalHeaderItem(index, item)

    def add_table_item(self, row_index, column_index, value, q_table_widget):
        column_value_item = QTableWidgetItem(str(value))
        column_value_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        # # 设置QTableWidgetItem对象里面的值水平，垂直居中
        column_value_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        q_table_widget.setItem(row_index, column_index, column_value_item)
        q_table_widget.resizeColumnToContents(column_index)
        q_table_widget.resizeRowToContents(row_index)

    def set_table_style(self, q_table_widget):
        q_table_widget.setStyleSheet("QTableWidget::item{padding-left:5px;padding-right:10px;}")

    def create_bar_set(self, name, value_list):
        set = QBarSet(name)
        # set.setBrush(QtGui.QColor(166, 174, 166))  # 设置颜色为绿色
        set.setBrush(QtGui.QColor(30, 195, 30))  # 设置颜色为绿色
        set.append(value_list)
        return set

    def load_chart_view(self, x_value_list, y_value_list):
        self.chart.removeAllSeries()

        series = QBarSeries()
        series.append(self.create_bar_set("Bar1", y_value_list))
        series.setLabelsVisible(True)
        # series.setLabelsAngle(75.0)
        # 展示数值精度
        series.setLabelsPrecision(3)
        series.setLabelsPosition(QBarSeries.LabelsOutsideEnd)
        # series.append(create_bar_set("Bar2"))
        # Create barset and append series to it
        valueAxisY = QValueAxis()
        valueAxisY.setRange(0, 40)
        valueAxisY.setVisible(False)
        barCategoryAxis = QBarCategoryAxis()
        # barCategoryAxis.append(["一季度", "二季度", "三季度"])
        barCategoryAxis.append(x_value_list)

        self.chart.addSeries(series)
        self.chart.setAxisY(valueAxisY)
        self.chart.setAxisX(barCategoryAxis)
        # chart.setTitle("PyQt Bar Chart")
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.setAnimationEasingCurve(QEasingCurve.InQuint)
        # Add barsets to the chart
        # chart.createDefaultAxes()
        self.chart.legend().setVisible(False)
        self.chart.legend().setAlignment(Qt.AlignBottom)

    def add_depayment_member_chart(self, series):
        x_value_list = []
        y_value_list = []

        series_dict = dict(series)
        sort_series_dict = dict(sorted(series_dict.items(), key=lambda item: item[1], reverse=True))
        for key, value in sort_series_dict.items():
            x_value_list.append(key)
            y_value_list.append(value)
        self.load_chart_view(x_value_list, y_value_list)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    w.setFocus()
    sys.exit(app.exec_())
