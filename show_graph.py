from tkinter import *
from tkinter import font
import math
class Graph:
    def __init__(self, data_list):
        graph_window = Tk()
        Label(graph_window, text=data_list[0]["SIGUN_NM"]+" 도서관 도서 보유량").pack()
        self.width = 800
        self.height = 500
        self.frame = Frame(graph_window, width=self.width, height=self.height)
        self.frame.pack()
        self.canvas = Canvas(self.frame, width=self.width, height=self.height, bg='white',
                             scrollregion=(0,0,self.height, self.width*20))
        book_num_list = []
        name_list = []
        for data in data_list:
            book_num_list.append(eval(data["BOOK_NUM"]))
            name_list.append(data["LIBRRY_NM"])
        max_num_org = max(book_num_list)
        digits = 10**(len(str(max_num_org))-1)

        max_num = math.ceil(max_num_org / digits) * digits
        bottom_ws = 20
        left_ws = 50
        bar_max_height = 400
        bar_height_per_num = bar_max_height / max_num
        bar_width = 50
        bar_distance = 35
        y2 = self.height - bottom_ws
        self.canvas.create_line(left_ws//2+20, bottom_ws, left_ws//2+20, self.height-bottom_ws)
        legend = max_num / 4
        for i in range(5):
            line_height = self.height - (i*legend*bar_height_per_num + bottom_ws)
            self.canvas.create_line(left_ws//2+15, line_height, left_ws//2+25, line_height)
            self.canvas.create_text(left_ws//2-10, line_height, text=str(int(i*legend)))
        for i in range(len(name_list)):
            x1 = i * bar_width + i * bar_distance + left_ws
            y1 = self.height - (book_num_list[i]*bar_height_per_num+bottom_ws)
            x2 = (i+1) * bar_width + i * bar_distance + left_ws
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="pink")
            text_size = ("Arial", 45//len(name_list[i]))
            self.canvas.create_text((x1+x2)//2, y2+10, font=text_size, text=name_list[i])
            self.canvas.create_text((x1+x2)//2, y1 - 10, text=book_num_list[i])
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.scrollbar = Scrollbar(self.frame, orient=HORIZONTAL)
        self.scrollbar.pack(side=BOTTOM, fill="x")
        self.scrollbar.config(command=self.canvas.xview)
        # self.canvas.config(width=self.width, height=self.height)
        self.canvas.config(xscrollcommand=self.scrollbar.set)
        self.canvas.pack(side=LEFT, expand=True, fill=BOTH)
        graph_window.mainloop()
        pass
'''
y_stretch = 15
y_gap = 20
x_stretch = 10
x_width = 20
x_gap = 20
for x, y in enumerate(data):
    # calculate reactangle coordinates
    x0 = x * x_stretch + x * x_width + x_gap
    y0 = c_height - (y * y_stretch + y_gap)
    x1 = x * x_stretch + x * x_width + x_width + x_gap
    y1 = c_height - y_gap
    # Here we draw the bar
    c.create_rectangle(x0, y0, x1, y1, fill="red")
    c.create_text(x0+2, y0, anchor=SW, text=str(y))
root.mainloop()
'''