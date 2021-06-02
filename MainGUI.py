
from tkinter import *
from tkinter import font
from tkinter import ttk
import load_xml
import box_manager
import show_map
import show_graph

WIDTH = 500
HEIGHT = 800
BUTTON_SIZE = 90

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

    def search(self, event=0):
        load_xml.search_and_register(Entry.get(self.to_search))
        self.show_result_frame()
        pass

    def mail(self):
        pass

    def graph(self):
        show_graph.Graph(load_xml.library_list)
        pass
    def telegram(self):
        pass
    def map(self):
        if self.manager is None:
            return
        if self.manager.get_selection() is None:
            return
        show_map.show_map(load_xml.library_list, self.manager.get_selection())


    def __init__(self):
        self.window = Tk()
        self.window.geometry(str(WIDTH)+"x"+str(HEIGHT))
        self.window.resizable(width=False, height=False)
        # 상단 검색 프레임
        s_font = font.Font(self.window, size=17, weight='bold', family='consolas')

        self.to_search = Entry(self.window, font=s_font)
        self.to_search.bind('<Return>', self.search)
        self.to_search.pack()
        self.to_search.place(x=5, y=5, width=390, height=45)

        self.search_button = Button(self.window, text="검색", command=self.search)
        self.search_button.pack()
        self.search_button.place(x=405, y=5, width=90, height=45)

        # 중단 결과 캠버스
        canvas_width = WIDTH - 10
        canvas_height = HEIGHT - 145
        self.manager = None
        self.result_frame = self.result_canvas = self.result_scrollbar = self.actual_result_frame = None
        self.show_result_frame()


        # 하단 버튼 프레임 gmail 그래프 chatbot
        self.button_frame = Frame(self.window)
        self.button_frame.pack()
        self.button_frame.place(x=5, y=750, width=canvas_width, height=85)


        button_width = 15
        self.mail_button = Button(self.button_frame, text="Gmail", command=self.mail, width=button_width)
        self.mail_button.grid(row=0, column=0)
        self.graph_button = Button(self.button_frame, text="그래프", command=self.graph,width=button_width)
        self.graph_button.grid(row=0, column=1)
        self.telegram_button = Button(self.button_frame, text="전송", command=self.telegram,width=button_width)
        self.telegram_button.grid(row=0, column=2)
        self.map_button = Button(self.button_frame, text="지도", command=self.map,width=button_width)
        self.map_button.grid(row=0, column=3)


        self.window.mainloop()





