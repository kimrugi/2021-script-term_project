
from tkinter import *

WIDTH = 500
HEIGHT = 800
BUTTON_SIZE = 90

class MainGUI:
    def search(self, event=0):
        pass

    def mail(self):
        pass
    def graph(self):
        pass
    def telegram(self):
        pass

    def __init__(self):
        window = Tk()
        window.geometry(str(WIDTH)+"x"+str(HEIGHT))
        window.resizable(width=False, height=False)
        # 상단 검색 프레임
        self.search_frame = window
        self.to_search = Entry(self.search_frame)
        self.to_search.bind('<Return>', self.search)
        self.to_search.place(x=5, y=5, width=390, height=45)

        self.search_button = Button(self.search_frame, text="검색", command=self.search)
        self.search_button.place(x=405, y=5, width=90, height=45)

        # 중단 결과 캠버스
        canvas_width = WIDTH-10
        canvas_height = HEIGHT - 150
        self.result_canvas = Canvas(window, bg='white', width=canvas_width, height=canvas_height)
        self.result_canvas.place(x=5, y=55, width=canvas_width, height=canvas_height)

        # 하단 버튼 프레임 gmail 그래프 chatbot
        self.button_frame = Frame(window)
        self.button_frame.pack()
        self.mail_button = Button(self.button_frame, text="Gmail", command=self.mail)
        self.mail_button.pack(side=LEFT)
        self.graph_button = Button(self.button_frame, text="그래프", command=self.graph)
        self.graph_button.pack(side=LEFT)
        self.telegram_button = Button(self.button_frame, text="전송", command=self.telegram)
        self.telegram_button.pack(side=LEFT)


        window.mainloop()





