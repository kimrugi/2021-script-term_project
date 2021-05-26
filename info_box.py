from tkinter import *
from PIL import Image, ImageDraw, ImageFont, ImageTk
import textwrap

class InfoBox:
    def __init__(self, frame, data, size, command):
        self.height = size
        self.body_canvas = Canvas(frame, width=490, height=self.height)
        self.body_canvas.pack()
        self.body = Frame(self.body_canvas, relief="solid", bd=2)

        Label(self.body, text=data["LIBRRY_NM"]).pack()
        Label(self.body, text=data["ADDRESS"]).pack()
        Button(self.body, text="선택", command=command).pack()
        self.body_canvas.create_window((0, 0), window=self.body, anchor="nw", height=self.height, width=450)

        pass




