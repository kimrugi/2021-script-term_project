from tkinter import *
class MainGUI:
    def search(self, event=0):
        pass

    def __init__(self):
        window = Tk()
        self.frame1 = Frame(window)
        self.frame1.pack()
        self.to_search = Entry(self.frame1)
        self.to_search.bind('<Return>', self.search)
        self.to_search.pack(side=LEFT)
        self.search_button = Button(self.frame1, text="검색", command=self.search)
        self.search_button.pack(side=LEFT)
        self.frame2 = Frame(window)
        self.frame2.pack()
        window.mainloop()





