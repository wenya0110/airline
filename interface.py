# -*-coding:utf-8-*-
from Tkinter import *
from flight_path import path
from airport_code import *
root=Tk()
var1=StringVar()
var2=StringVar()

label1=Label(root,text=u"出发地（城市或机场代码）").grid(row=0)

en=Entry(root,textvariable=var1).grid(row=0,column=1)

label2=Label(root,text=u"目的地（城市或机场代码）").grid(row=1)

en1=Entry(root,textvariable=var2).grid(row=1,column=1)


B = Button(root, text=u"搜索",command=lambda :path(var1.get(),var2.get())).grid(row=2)


