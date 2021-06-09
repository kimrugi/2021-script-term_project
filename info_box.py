from tkinter import *
import datetime

mid_night0 = datetime.datetime.strptime("00:00", "%H:%M")
mid_night24 = datetime.datetime.strptime("23:59", "%H:%M")

class InfoBox:
    def __init__(self, frame, data, size, command):
        self.height = size
        self.body_canvas = Canvas(frame, width=490, height=self.height)
        self.body_canvas.pack()
        self.body = Frame(self.body_canvas, relief="solid", bd=2)

        Label(self.body, text=data["LIBRRY_NM"]).pack()
        Label(self.body, text=data["ROAD_ADDRESS"]).pack()
        self.time_check(data)
        time_text = "평일 운영시간: "+data["BEGIN_TM"] + "~" + data["END_TM"] +\
                    "\n토요일 운영시간: " + data["SAT_BEGIN_TM"] + "~" + data["SAT_END_TM"]
        Label(self.body, text=time_text).pack()

        if self.time_check(data):
            Label(self.body, text="개관").pack()
        else:
            Label(self.body, text="휴관").pack()

        self.button = Button(self.body, text="선택", command=command, width=5, height=5)
        self.button.place(x=390, y=3)
        self.body_canvas.create_window((0, 0), window=self.body, anchor="nw", height=self.height, width=450)

    def button_selected(self):
        self.button.configure(bg="red")

    def button_unselected(self):
        self.button.configure(bg='SystemButtonFace')

    def time_check(self, data):
        now = datetime.datetime.today()
        if now.weekday() == 6:
            return False

        current_time = datetime.datetime(1900,1,1, now.hour, now.minute)
        if now.weekday() == 5:
            begin_time = datetime.datetime.strptime(data["SAT_BEGIN_TM"], "%H:%M")
            end_time = datetime.datetime.strptime(data["SAT_END_TM"], "%H:%M")
            if begin_time == mid_night0:
                begin_time = mid_night24
            if end_time == mid_night0:
                end_time = mid_night24
            if begin_time < current_time < end_time:
                return True
            return False

        begin_time = datetime.datetime.strptime(data["BEGIN_TM"], "%H:%M")
        end_time = datetime.datetime.strptime(data["END_TM"], "%H:%M")
        if begin_time == mid_night0:
            begin_time = mid_night24
        if end_time == mid_night0:
            end_time = mid_night24
        if begin_time < current_time < end_time:
            return True
        return False



