# -*- coding:utf-8 -*-
# @Description
# @Author: Shimin
# @Copyright
# @Version:0.0.1
from tkinter import *

window = Tk()


def kg_convert():
    print(e1_value.get())
    grams = float(e1_value.get()) * 1000
    pounds = float(e1_value.get()) * 2.20462

    ounces = float(e1_value.get()) * 35.274
    t1.insert(END, grams)
    t2.insert(END, pounds)
    t3.insert(END, ounces)
# need to delete the previous value records

l1 = Label(window, text="Kg", height=1, width=25)
l1.grid(row=0, column=0)
l2 = Label(window, height=1, width=25)
l2.grid(row=0, column=2)

e1_value = StringVar()
e1 = Entry(window, width=20, textvariable=e1_value)
e1.grid(row=0, column=1)

b1 = Button(window, text="Convert", command=kg_convert)
b1.grid(row=0, column=2)

t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)
t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=1)
t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=2)
window.mainloop()
