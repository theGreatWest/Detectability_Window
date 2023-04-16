import os
from glob import glob
import time
import pandas as pd
import random as rd
import tkinter
from tkinter import ttk
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import matplotlib.image as img
from answer import get_answer, get_num, set_num, get_answer
import sys

def res_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

tutorial_answer_path = res_path("fold_db/tutorial_answer")

window = tkinter.Tk()
window.configure(background='black')
window.title('Detectability for Low Contrast Objects (SNUBH)')
window.geometry("{}x{}+{}+{}".format(1400, 920, 28, 28))
window.resizable(True, True)

def score(value):
    if value == 1:
        txt = 'Definitely Absent'
    elif value == 2:
        txt = 'Probably Absent'
    elif value == 3:
        txt = 'Indeterminate'
    elif value == 4:
        txt = 'Probably Present'
    else:
        txt = 'Definitely Present'
    return txt

def res(value):
    if value == 1:
        txt = 'Correct'
    else:
        txt = 'Incorrect'
    return txt

def aw(value):
    if value == 1:
        txt = 'Present'
    else:
        txt = 'Absent'

photo_list = []
answer_list = []
score_list = []
result_list = []
for row in (get_answer()):
    photo_list.append(tkinter.PhotoImage(file=row[1]))
    answer_list.append(aw(row[3]))
    score_list.append(score(row[2]))
    result_list.append(res(row[4]))
answer_img = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10"]
i = 0
for photo in photo_list:
    answer_img[i] = tkinter.Label(window, image=photo, background='black',border=2, width=310, height=310, highlightcolor='white')
    i += 1

expla = []
for i in range(10):
    scp = f"{score_list[i]} ({result_list[i]})"
    expla.append(scp)

answer_img[0].place(x=0, y=0)
a = tkinter.Label(window, text=expla[0], background="white",foreground='black', font='Helvetica 14 bold')
a.place(x=0, y=0)

answer_img[1].place(x=367, y=0)
b = tkinter.Label(window, text=expla[1], background="white", foreground='black', font='Helvetica 14 bold')
b.place(x=367, y=0)

answer_img[2].place(x=734, y=0)
c = tkinter.Label(window, text=expla[2], background="white", foreground='black', font='Helvetica 14 bold')
c.place(x=734, y=0)

answer_img[3].place(x=1100, y=0)
d = tkinter.Label(window, text=expla[3], background="white", foreground='black', font='Helvetica 14 bold')
d.place(x=1100, y=0)

answer_img[4].place(x=0, y=310)
e = tkinter.Label(window, text=expla[4], background="white", foreground='black', font='Helvetica 14 bold')
e.place(x=0, y=310)

answer_img[5].place(x=367, y=310)
f = tkinter.Label(window, text=expla[5], background="white",  foreground='black', font='Helvetica 14 bold')
f.place(x=367, y=310)

answer_img[6].place(x=734, y=310)
g = tkinter.Label(window, text=expla[6], background="white", foreground='black', font='Helvetica 14 bold')
g.place(x=734, y=310)

answer_img[7].place(x=1100, y=310)
h = tkinter.Label(window, text=expla[7], background="white", foreground='black', font='Helvetica 14 bold')
h.place(x=1100, y=310)

answer_img[8].place(x=0, y=620)
i = tkinter.Label(window, text=expla[8], background="white", foreground='black', font='Helvetica 14 bold')
i.place(x=0, y=620)

answer_img[9].place(x=367, y=620)
j = tkinter.Label(window, text=expla[9], background="white",  foreground='black', font='Helvetica 14 bold')
j.place(x=367, y=620)

ex = [a, b, c, d, e, f, g, h, i, j]
i = 0
for target in ex:
    if result_list[i] == 1:
        ex[i].config(fg="red")
    i += 1

def retry_tutorial():
    window.destroy()
    import tutorial2

def bye():
    retry_tutorial()

def start():
    window.destroy()
    import detectability

nt = tkinter.Label(window, text="Tutorial Finished",background='black', foreground='white', font='Helvetica 14 bold')
nt.place(x=990, y=700)

retry = tkinter.Button(window, text='', background='white', foreground='black', font='Helvetica 16 bold',relief='groove', borderwidth=1, width=14, height=2, highlightcolor='white', highlightbackground='white')
if get_num() == 2:
    retry.config(text='Start')
    retry.config(command=start)
else:
    retry.config(text='Retry')
    retry.config(command=bye)
retry.place(x=990, y=740)

def on_key_press(event):
    if retry['text'] == 'Start':
        start()
    else:
        bye()


window.bind("<Return>", on_key_press)

window.mainloop()