import os
from glob import glob
import pandas as pd
import random as rd
import tkinter
from tkinter import *
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import matplotlib.image as img
from answer import set_answer, get_num, set_num, get_answer
import sys

def res_path(relative_path):
    try:
        base_path=sys._MEIPASS
    except Exception:
        base_path=os.path.abspath(".")
    return os.path.join(base_path,relative_path)

tutorial_path = res_path("fold_db/tutorial")
tp = os.listdir(tutorial_path)
tutorial_answer_path = res_path("fold_db/tutorial_answer")

qna = []

def select_tutorial():
    global tp
    tutorial_10 = []
    for _ in range(10):
        idx = rd.randint(0, len(tp)-1)
        tutorial_10.append(tp[idx])
        tp.remove(tp[idx])
    return tutorial_10

window = tkinter.Tk()
window.configure(background='black')
window.title('Detectability for Low Contrast Objects (SNUBH)')
window.geometry("{}x{}+{}+{}".format(1400, 900, 28, 28))
window.resizable(True, True)

select_10 = select_tutorial()
select_real = [tkinter.PhotoImage(file=os.path.join(
    tutorial_path, filename)) for filename in select_10]
tmp = []
for q in select_10:
    if q.split("_")[0] == "background":
        a_path = os.path.join(tutorial_answer_path, q)
    else:
        a_path = f"{tutorial_answer_path}/answer_{q}"
    tmp.append(a_path)
select_answer_real = [tkinter.PhotoImage(file=path) for path in tmp]

tutorial_list = [os.path.join(tutorial_path, filename) for filename in select_10]
c_img = [Image.open(path) for path in tutorial_list]
c_pthoto = [ImageTk.PhotoImage(li) for li in c_img]

total = 1
cnt = 0
tutorial_txt = f"Tutorial # {cnt} / 10"  # 중앙 글씨
txt_label = tkinter.Label(window, name="txt_label", text=tutorial_txt, foreground='white', background='black', font='Helvetica 28 bold')
txt_label.place(x=570, y=130)
right_answer = ""

if cnt == 0:
    img = c_img[0]  # 중앙 이미지
    middle_img_label = Canvas(width=img.width, height=img.height, bd=0, bg='black', highlightcolor='black', highlightbackground='black')
    middle_img_label.create_image(180, 180, image=c_pthoto[0])
    middle_img_label.place(x=500, y=200)

right_img_label = Canvas()
left_img_label = Canvas()

def add_func(score):
    global txt_label
    middle_img_label.delete('all')

    global right_img_label
    global left_img_label
    global select_real
    global select_10
    global total
    global right_answer
    global cnt
    global qna

    q_path = os.path.join(tutorial_path, select_10[cnt])
    if select_10[cnt].split("_")[0] == "background":
        right_answer = 0
        a_path = os.path.join(tutorial_answer_path, select_10[cnt])
    else:
        right_answer = 1
        a_path = f"{tutorial_answer_path}/answer_{select_10[cnt]}"

    if (score >= 3 and right_answer == 1) or (score < 3 and right_answer == 0):
        result = 1
    else:
        result = 0

    qna.append([q_path, a_path, score, right_answer, result])

    # 이미지 처리
    if cnt % 2 == 0:
        right_img_label.delete('all')
        img = c_img[cnt]  # 중앙 이미지
        left_img_label = Canvas(width=img.width, height=img.height, bd=0,
                                bg='black', highlightcolor='black', highlightbackground='black')
        left_img_label.create_image(180, 180, image=c_pthoto[cnt])
        left_img_label.place(x=300, y=200)

    else:
        left_img_label.delete('all')
        img = c_img[cnt]  # 중앙 이미지
        right_img_label = Canvas(width=img.width, height=img.height, bd=0, bg='black', highlightcolor='black', highlightbackground='black')
        right_img_label.create_image(180, 180, image=c_pthoto[cnt])
        right_img_label.place(x=680, y=200)

    cnt += 1
    tutorial_txt = f"Tutorial # {cnt} / 10"  # 중앙 글씨
    txt_label.config(text=tutorial_txt)
    if cnt == 10:
        set_num(1)
        set_answer(qna)
        window.destroy()
        import result_a

def on_key_press(event):
    if event.char == "1":
        b1.invoke()
    elif event.char == "2":
        b2.invoke()
    elif event.char == "3":
        b3.invoke()
    elif event.char == "4":
        b4.invoke()
    elif event.char == "5":
        b5.invoke()

def stop_start(event):
    btn_list = [b1, b2, b3, b4, b5]
    if b1["state"] == 'normal':
        for btn in btn_list:
            btn.config(state='disabled')
    else:
        for btn in btn_list:
            btn.config(state='normal')

b1 = tkinter.Button(window, text='[1]\nDefinitely Absent', background='white', foreground='black', font='Helvetica 16 bold',
                    relief='groove', borderwidth=1, width=14, height=2, highlightcolor='white', command=lambda: add_func(1), highlightbackground='white')
b2 = tkinter.Button(window, text='[2]\nProbably Absent', background='white', foreground='black', font='Helvetica 16 bold', relief='groove',
                    borderwidth=1, width=14, height=2, highlightcolor='white', command=lambda: add_func(2), highlightbackground='white')
b3 = tkinter.Button(window, text='[3]\nIndeterminate', background='white', foreground='black', font='Helvetica 16 bold', relief='groove',
                    borderwidth=1, width=14, height=2, highlightcolor='white', command=lambda: add_func(3), highlightbackground='white')
b4 = tkinter.Button(window, text='[4]\nProbably Present', background='white', foreground='black', font='Helvetica 16 bold',
                    relief='groove', borderwidth=1, width=14, height=2, highlightcolor='white', command=lambda: add_func(4), highlightbackground='white')
b5 = tkinter.Button(window, text='[5]\nDefinitely Present', background='white', foreground='black', font='Helvetica 16 bold',
                    relief='groove', borderwidth=1, width=14, height=2, highlightcolor='white', command=lambda: add_func(5), highlightbackground='white')

btn_list = [b1, b2, b3, b4, b5]
btn_interval = 1
for btn in btn_list:
    btn.place(x=200*btn_interval, y=650)
    btn_interval += 1

window.bind("<KeyPress>", on_key_press)
window.bind("<Return>", stop_start)

window.mainloop()