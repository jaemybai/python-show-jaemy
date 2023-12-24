from MemberInfo import MemberInfo
import pandas
import LogUtil


class MemberStats(object):
    def __init__(self):
        super().__init__()
        self.rows = 0
        self.columns = 0
        self.column_list = []
        self.member_info_list = []
        self.member_info_list_by_sort = []
        self.enter_cost_times_stat_series = None
        self.enter_count_stat_series = None
        self.member_stat_by_department_series = None
        self.name_by_department_stat_series = None
        self.total_members = None
        self.enter_detail_stat_frame = None

    def init_info(self, rows, columns, column_list, member_info_list):
        self.rows = rows
        self.columns = columns
        self.column_list = column_list
        self.member_info_list = member_info_list
        # 按照刷卡时间排序
        self.member_info_list_by_sort = sorted(self.member_info_list, key=lambda m: m.recordTime_format, reverse=False)
        self.stat_member_info()

        data_list = []
        temColumns = ["工号", "姓名", "部门", "状态", "入门时间", "出门时间", "进出次数", "本次进出时间",
                      "累计进出时间", "是否是进门"]
        for index_member in self.member_info_list_by_sort:
            temMember = index_member
            oneRow = [temMember.memberNo, temMember.memberName, temMember.department,
                      temMember.entry_cost_times > 0,
                      temMember.entryTime_format, temMember.goOutTime_format, temMember.entry_count,
                      temMember.entry_cost_times, temMember.total_entry_cost_time, temMember.isEntry]
            data_list.append(oneRow)
        data_frame = pandas.DataFrame(data_list, columns=temColumns)
        # 统计总人数
        self.total_members = data_frame["姓名"].nunique()
        # 按照部门分组并根据姓名列去重统计人数
        self.member_stat_by_department_series = data_frame.groupby("部门")["姓名"].nunique()
        # filter_df = df[df["班级"] == "一班"]

        enter_data_frame = data_frame[data_frame["是否是进门"]]
        self.enter_count_stat_series = enter_data_frame[enter_data_frame["进出次数"] > 0].groupby("姓名").max("进出次数").sort_values("进出次数").tail(3)[
            "进出次数"]
        self.enter_cost_times_stat_series =enter_data_frame[enter_data_frame["累计进出时间"] > 0].groupby("姓名").max("累计进出时间").sort_values("累计进出时间").tail(3)["累计进出时间"]
        self.enter_detail_stat_frame = enter_data_frame[
            ["工号", "姓名", "部门", "状态", "入门时间", "出门时间", "进出次数", "本次进出时间", "累计进出时间"]]

    def stat_member_info(self):
        tem_member_map = {}
        for index_member_info in self.member_info_list_by_sort:
            member_info = index_member_info
            member_stat_key = member_info.memberNo + ":" + member_info.recordTime_today
            # member_stat_key = member_info.memberNo

            if member_stat_key in tem_member_map:
                tem_member_enter_go_out_map = tem_member_map[member_stat_key]
            else:
                tem_member_enter_go_out_map = None

            if tem_member_enter_go_out_map is None or len(tem_member_enter_go_out_map) == 0:
                # 首次初始化
                if member_info.isEntry:
                    # 第一次打卡进门
                    tem_member_enter_go_out_map = {}
                    tem_member_enter_go_out_map["current_count"] = 1
                    tem_member_enter_go_out_map["total_entry_cost_time"] = 0
                    tem_member_enter_go_out_map["enter_member"] = member_info
                    tem_member_map[member_stat_key] = tem_member_enter_go_out_map
                else:
                    # 还没有打卡进来，出现打卡出去记录（异常）
                    member_info.illegal_go_out = True
                    LogUtil.printLog("还没有打卡进来，出现打卡出去记录（异常）", member_info.memberNo, ":",
                                     member_info.seqNo)
            elif "go_out_member" not in tem_member_enter_go_out_map:
                if member_info.isEntry:
                    # 重复打卡进来，以第一次打卡时间为准
                    member_info.illegal_entry = True
                    LogUtil.printLog("重复打卡进门本次忽略跳过", member_info.memberNo, ":", member_info.seqNo)
                else:
                    tem_member_enter_go_out_map["go_out_member"] = member_info

                    # 打卡进来，出来后再次打卡进来，进行统计
                    current_count = tem_member_enter_go_out_map["current_count"]
                    total_entry_cost_time = tem_member_enter_go_out_map["total_entry_cost_time"]
                    enter_member = tem_member_enter_go_out_map["enter_member"]
                    go_out_member = tem_member_enter_go_out_map["go_out_member"]

                    # 存在进入出去打开记录，在进入记录上处理逻辑
                    enter_member.goOutTime_format = go_out_member.goOutTime_format
                    enter_member.entry_count = current_count
                    time_diff = enter_member.goOutTime_format - enter_member.entryTime_format
                    enter_member.entry_cost_times = time_diff.total_seconds()
                    enter_member.total_entry_cost_time = enter_member.entry_cost_times + total_entry_cost_time
            else:
                if member_info.isEntry:
                    # 再次打卡进来，之前记录清理掉
                    current_count = tem_member_enter_go_out_map["current_count"]
                    enter_member = tem_member_enter_go_out_map["enter_member"]

                    tem_member_enter_go_out_map.clear()
                    current_count = current_count + 1
                    tem_member_enter_go_out_map = {}
                    tem_member_enter_go_out_map["current_count"] = current_count
                    tem_member_enter_go_out_map["total_entry_cost_time"] = enter_member.total_entry_cost_time
                    tem_member_enter_go_out_map["enter_member"] = member_info
                    tem_member_map[member_stat_key] = tem_member_enter_go_out_map
                else:
                    # 连续打卡出去，重新计算进出时间耗时
                    tem_member_enter_go_out_map["go_out_member"] = member_info

                    total_entry_cost_time = tem_member_enter_go_out_map["total_entry_cost_time"]
                    enter_member = tem_member_enter_go_out_map["enter_member"]
                    go_out_member = tem_member_enter_go_out_map["go_out_member"]

                    enter_member.goOutTime_format = go_out_member.goOutTime_format
                    time_diff = enter_member.goOutTime_format - enter_member.entryTime_format
                    enter_member.entry_cost_times = time_diff.total_seconds()
                    enter_member.total_entry_cost_time = enter_member.entry_cost_times + total_entry_cost_time
