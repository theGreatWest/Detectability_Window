import os
from glob import glob
import pandas as pd
import random as rd
import tkinter
from tkinter import ttk
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import matplotlib.image as img
from info import name_1, affiliation_1
import shutil as sh
import sys


def res_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


csv_old = res_path(f"result_csv/CATPHAN_{affiliation_1}_{name_1}.csv")
csv_new = res_path(f"../../result_csv/CATPHAN_{affiliation_1}_{name_1}.csv")
sh.copy2(csv_old, csv_new)

window = tkinter.Tk()
window.configure(background='black')
window.title('Detectability for Low Contrast Objects (SNUBH)')
window.geometry("{}x{}+{}+{}".format(1400, 900, 28, 28))
window.resizable(True, True)


def bye():
    window.destroy()


show_info_button = tkinter.Button(window, text="End", command=bye, background='white',
                                  foreground='black', font='Helvetica 24 bold', highlightcolor='white')
show_info_button.place(x=650, y=380)


csv_path = res_path(f"result_csv/CATPHAN_{affiliation_1}_{name_1}.csv")
csv_df = pd.read_csv(csv_path)
selected_column = list(csv_df["Result"])

tot = 0
for v in selected_column:
    if v == 1:
        tot += 1

percentage = round((tot/len(selected_column)) * 100, 2)
tutorial_txt = f"정답률: {percentage}%"  # 중앙 글씨
txt_label = tkinter.Label(window, name="txt_label", text=tutorial_txt,
                          foreground='white', background='black', font='Helvetica 22 bold')
txt_label.place(x=595, y=300)

window.bind("<Return>", bye)

window.mainloop()
