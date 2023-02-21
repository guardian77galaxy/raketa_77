import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox


class RaketaWindowApp:
    def __init__(self, name_app, size_window, bg_color):
        self.root = Tk()
        self.name_app = name_app
        self.size_window = size_window
        self.bg_color = bg_color

    def add_window(self):
        self.root.title(self.name_app)
        self.root.geometry(self.size_window)
        self.root.resizable(False, False)
        self.root.config(bg=self.bg_color)

        self.root.mainloop()

    def add_label(self, width, height, text, font, fg, bg, relx, y, anchor):
        my_label = tkinter.Label(self.root,
                                 width=width,
                                 height=height,
                                 text=text,
                                 font=font,
                                 fg=fg,
                                 bg=bg,
                                 justify="center")

        my_label.place(relx=relx, y=y, anchor=anchor)




