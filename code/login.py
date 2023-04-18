import os
from glob import glob
import pandas as pd
import random as rd
import tkinter
from tkinter import ttk
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import matplotlib.image as img
from info import info

window = tkinter.Tk()
window.configure(background='black')
window.title('Detectability for Low Contrast Objects (SNUBH)')
window.geometry("{}x{}+{}+{}".format(1400, 900, 28, 28))
window.resizable(True, True)

name_label = tkinter.Label(window, text="Name  ", background='black', foreground='white', font='Helvetica 20 bold')
name_label.place(x=490, y=350)
name_entry = tkinter.Entry(window, background='gray30', foreground='white', font='Helvetica 20 bold')
name_entry.place(x=670, y=350)

affiliation_label = tkinter.Label(
    window, text="Affiliation  ", background='black', foreground='white', font='Helvetica 20 bold')
affiliation_label.place(x=490, y=400)
affiliation_entry = tkinter.Entry(
    window, background='gray30', foreground='white', font='Helvetica 20 bold')
affiliation_entry.place(x=670, y=400)

name_1 = ""
affiliation_1 = ""

def show_warning():
    top = tkinter.Toplevel()
    top.title("Warning")
    tkinter.Label(top, text="Please enter your name and affiliation").pack(
        side="top")
    tkinter.Button(top, text="OK", command=top.destroy).pack()

    # 창의 크기 및 위치 설정
    top.withdraw()
    top.update_idletasks()
    x = (top.winfo_screenwidth() - top.winfo_reqwidth()) // 2
    y = (top.winfo_screenheight() - top.winfo_reqheight()) // 2
    top.geometry("+{}+{}".format(x, y))
    top.deiconify()
    top.bind('<Return>', lambda event: top.destroy())

def show_info():
    global name_1
    global affiliation_1
    name = name_entry.get()
    affiliation = affiliation_entry.get()
    if name and affiliation:
        name_1 = name
        affiliation_1 = affiliation
        info(name_1, affiliation_1)
        window.destroy()
        import tutorial
    else:
        name_1 = ""
        affiliation_1 = ""
        show_warning()

def go(event):
    show_info()

show_info_button = tkinter.Button(window, text="Submit and Start", command=show_info,background='white', foreground='black', font='Helvetica 14 bold', highlightbackground='white')
show_info_button.place(x=1010, y=399.5)

window.bind("<Return>", go)

window.mainloop()