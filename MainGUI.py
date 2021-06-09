
from tkinter import *
from tkinter import font
from tkinter import ttk
import load_xml
import box_manager
import show_map
import show_graph
import send_mail

WIDTH = 500
HEIGHT = 800
BUTTON_SIZE = 90
SIGUN_LIST = ['가평군', '고양시', '과천시', '광명시', '광주시', '구리시', '군포시', '김포시', '남양주시',
              '동두천시', '부천시', '성남시', '수원시', '시흥시', '안산시', '안성시', '안양시', '양평군',
              '양주시', '여주시', '연천군', '오산시', '용인시', '의왕시', '의정부시', '이천시', '파주시',
              '평택시', '포천시', '하남시', '화성시']
class MainGUI:
    def show_result_frame(self):
        canvas_width = WIDTH - 10
        canvas_height = HEIGHT - 145
        self.manager = None
        if self.actual_result_frame is not None:
            self.actual_result_frame.destroy()
        if self.result_scrollbar is not None:
            self.result_scrollbar.destroy()
        if self.result_canvas is not None:
            self.result_canvas.destroy()
        if self.result_frame is not None:
            self.result_frame.destroy()

        self.result_frame = Frame(self.window)
        self.result_frame.place(x=5, y=55, width=canvas_width, height=canvas_height)
        self.result_canvas = Canvas(self.result_frame, width=450)
        self.result_canvas.pack(side=LEFT, fill="y")
        self.result_scrollbar = ttk.Scrollbar(self.result_frame, orient="vertical",
                                              command=self.result_canvas.yview)
        self.result_scrollbar.pack(side=RIGHT, fill="y")
        self.result_canvas.configure(yscrollcommand=self.result_scrollbar.set)
        self.result_canvas.bind("<Configure>", lambda e: self.result_canvas.configure(
            scrollregion=self.result_canvas.bbox("all")))
        self.actual_result_frame = Frame(self.result_canvas)
        self.result_canvas.create_window((0, 0), window=self.actual_result_frame, anchor="nw", width=450)
        self.manager = box_manager.BoxManager(self.actual_result_frame, load_xml.library_list)

    def search_sigun(self, event=0):
        load_xml.search_and_register(ttk.Combobox.get(self.sigun))
        self.to_search.delete(0,"end")
        self.show_result_frame()

    def search_name(self, event=0):
        load_xml.search_name_and_register(Entry.get(self.to_search))
        self.show_result_frame()

    def mail(self):
        if not load_xml.library_list:
            return
        if self.manager.get_selection() is not None:
            send_mail.Mail(load_xml.library_list[self.manager.get_selection()])


    def graph(self):
        if not load_xml.library_list:
            return
        show_graph.Graph(load_xml.library_list)

    def map(self):
        if not load_xml.library_list:
            return
        if self.manager.get_selection() is None:
            show_map.show_map(load_xml.library_list)
        show_map.show_map(load_xml.library_list, self.manager.get_selection())

    def __init__(self):
        self.window = Tk()
        self.window.geometry(str(WIDTH)+"x"+str(HEIGHT))
        self.window.resizable(width=False, height=False)
        self.window.title("경기도 도서관 검색")
        # 상단 검색 프레임
        s_font = font.Font(self.window, size=17, weight='bold', family='consolas')

        self.sigun = ttk.Combobox(self.window, value=SIGUN_LIST, font=s_font, state="readonly")
        self.sigun.place(x=5, y=5, width=120, height=45)
        self.sigun.set("지역")
        self.sigun.bind("<<ComboboxSelected>>", self.search_sigun)

        self.to_search = Entry(self.window, font=s_font)
        self.to_search.bind('<Return>', self.search_name)
        #self.to_search.pack()
        self.to_search.place(x=130, y=5, width=270, height=45)

        self.search_button = Button(self.window, text="검색", command=self.search_name)
        #self.search_button.pack()
        self.search_button.place(x=405, y=5, width=90, height=45)

        # 중단 결과 캠버스
        canvas_width = WIDTH - 10
        canvas_height = HEIGHT - 145
        self.manager = None
        self.result_frame = self.result_canvas = self.result_scrollbar = self.actual_result_frame = None
        self.show_result_frame()

        # 하단 버튼 프레임 gmail 그래프 chatbot
        self.button_frame = Frame(self.window)
        # self.button_frame.pack()
        self.button_frame.place(x=5, y=710, width=canvas_width)

        button_width = 21
        mail_image = PhotoImage(file="image/gmail.png")
        graph_image = PhotoImage(file="image/graph.png")
        map_image = PhotoImage(file="image/map.png")

        self.mail_button = Button(self.button_frame, image=mail_image, command=self.mail)
        self.graph_button = Button(self.button_frame, image=graph_image, command=self.graph)
        self.map_button = Button(self.button_frame, image=map_image, command=self.map)

        Label(self.button_frame, text="", height=100).pack(side=RIGHT)
        self.mail_button.place(x=50, y=0)
        self.graph_button.place(x=200, y=0)
        self.map_button.place(x=350, y=0)
        self.window.mainloop()





