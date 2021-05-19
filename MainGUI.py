
from tkinter import *
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
        # 상단 검색 프레임
        self.search_frame = Frame(window)
        self.search_frame.pack()
        self.to_search = Entry(self.search_frame)
        self.to_search.bind('<Return>', self.search)
        self.to_search.pack(side=LEFT)
        self.search_button = Button(self.search_frame, text="검색", command=self.search)
        self.search_button.pack(side=LEFT)

        # 중단 결과 프레임
        self.result_frame = Frame(window)
        self.result_frame.pack()

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





