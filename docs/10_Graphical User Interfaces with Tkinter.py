# -*- coding:utf-8 -*-
# @Description
# @Author: Shimin
# @Copyright
# @Version:0.0.1
from tkinter import *

window = Tk()


def km_to_miles():
    print(e1_value.get())
    miles = float(e1_value.get()) * 1.6
    t1.insert(END, miles)


b1 = Button(window, text="Execute", command=km_to_miles)
b1.grid(row=0, column=0)   # "Execute" button in (0,0) of window

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)    # Entry() a place where we can input begin at (0,1)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)
window.mainloop()