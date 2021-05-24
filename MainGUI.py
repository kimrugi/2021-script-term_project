
from tkinter import *
from tkinter import font
import load_xml

WIDTH = 500
HEIGHT = 800
BUTTON_SIZE = 90

class MainGUI:
    def search(self, event=0):
        load_xml.search(Entry.get(self.to_search))

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
        s_font = font.Font(window, size=17, weight='bold', family='consolas')

        self.to_search = Entry(self.search_frame, font=s_font)
        self.to_search.bind('<Return>', self.search)
        self.to_search.pack()
        self.to_search.place(x=5, y=5, width=390, height=45)

        self.search_button = Button(self.search_frame, text="검색", command=self.search)
        self.search_button.pack()
        self.search_button.place(x=405, y=5, width=90, height=45)

        # 중단 결과 캠버스
        canvas_width = WIDTH-10
        canvas_height = HEIGHT - 145
        self.result_canvas = Canvas(window, bg='white', width=canvas_width, height=canvas_height)
        self.result_canvas.place(x=5, y=55, width=canvas_width, height=canvas_height)

        # 하단 버튼 프레임 gmail 그래프 chatbot
        self.button_frame = Frame(window)
        self.button_frame.pack()
        self.button_frame.place(x=5, y=705, width=canvas_width, height=85)

        button_width = canvas_width // 3
        self.mail_button = Button(self.button_frame, text="Gmail", command=self.mail, width=button_width)
        self.mail_button.grid(row=0, column=0)
        self.graph_button = Button(self.button_frame, text="그래프", command=self.graph,width=button_width)
        self.graph_button.grid(row=0, column=1)
        self.telegram_button = Button(self.button_frame, text="전송", command=self.telegram,width=button_width)
        self.telegram_button.grid(row=0, column=2)


        window.mainloop()





