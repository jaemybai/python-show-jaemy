from datetime import datetime


class MemberInfo(object):
    def __init__(self):
        super().__init__()
        self.seqNo = ""
        self.memberCardNumber = ""
        self.memberNo = ""
        self.memberName = ""
        self.department = ""
        self.recordTime = ""
        self.location = ""
        self.status = ""
        self.remark = ""
        self.memberList = None
        self.isEntry = None
        self.recordTime_format = None
        self.recordTime_today = None
        self.entryTime_format = None
        self.goOutTime_format = None
        self.entry_count = 0
        self.entry_cost_times = 0
        self.total_entry_cost_time = 0
        self.illegal_entry = False
        self.illegal_go_out = False



    def init_info_by_list(self, listParam):
        self.memberList = listParam
        self.seqNo = str(listParam[0]).strip()
        self.memberCardNumber = str(listParam[1]).strip()
        self.memberNo = str(listParam[2]).strip()
        self.memberName = str(listParam[3]).strip()
        self.department = str(listParam[4]).strip()
        self.recordTime = str(listParam[5]).strip()
        self.location = str(listParam[6]).strip()
        self.status = str(listParam[7]).strip()
        self.remark = str(listParam[8]).strip()

        if self.location.endswith("出门"):
            self.isEntry = False
        elif self.location.endswith("进门"):
            self.isEntry = True
        else:
            raise ValueError('地址格式无法区分出门还是入口')

        temTimeList = self.recordTime.split("星期")
        if len(temTimeList) != 2:
            raise ValueError('时间格式不对')

        self.recordTime_format = datetime.strptime(temTimeList[0].strip(), "%Y-%m-%d %H:%M:%S")
        self.recordTime_today = self.recordTime_format.strftime("%Y-%m-%d")
        if self.isEntry:
            self.entryTime_format = self.recordTime_format
        else:
            self.goOutTime_format = self.recordTime_format
