from datetime import datetime
from datetime import date
class MyCalendar:
    def __init__(self, *args):
        self.datas = []
        self.newholiday = []

        for dt in args:
            if type(dt) is tuple:
                for d in dt:
                    if type(d) is date:
                        self.datas.append(d)
                    elif type(d) is str:
                        if len(d) == 9:
                            splited = d.split('/')
                            if int(splited[0]) > 31:
                                continue
                            if int(splited[1]) > 12:
                                continue
                            try:
                                self.datas.append(datetime.strptime(d, '%d/%m/%Y').date())
                            except:
                                pass
                        else:
                            pass
                    else:
                        pass
            else:
                if type(dt) is date:
                    self.datas.append(dt)
                elif type(dt) is str:
                    if len(dt) == 9:
                        splited = dt.split('/')
                        if int(splited[0]) > 31:
                            continue
                        if int(splited[1]) > 12:
                            continue
                        try:
                            self.datas.append(datetime.strptime(dt, '%d/%m/%Y').date())
                        except:
                            pass
                    else:
                        pass

    def add_holiday(self, *args):
        for dt in args:
            if type(dt) is date:
                self.datas.append(dt)
            elif type(dt) is str:
                if len(dt) == 9:
                    splited = dt.split('/')
                    if int(splited[0]) > 31:
                        continue
                    if int(splited[1]) > 12:
                        continue
                    try:
                        self.datas.append(datetime.strptime(dt, '%d/%m/%Y').date())
                    except:
                        pass
                else:
                    pass

# tests/test_my_holidays.py ...FFF....FFFFFFFFFF          
# tests/test_my_holidays.py ...FFF.....FFFFFFFFF          