# -*-coding:utf-8-*-
from PIL import *
import json
import sys
import pyglet
from flight_path import *
import tkinter as tk
from tkinter import *
import webbrowser
from airport_code import *
f='quanbu.html'

def searchdata321(a,b):
    x = xlrd.open_workbook('D1.xls')
    sh =x.sheet_by_index(0)
    nrows=sh.nrows
    ncols=sh.ncols
    a=airport_code(a)
    if a==None:
        a='*'
    c = (0,1,2,3,4,5,6)
    columnnum=2
    #表示航班信息表格中第几列
# input the searching string and column
#find the rows which you want to select and write to a txt file
    for i in range(nrows):
        cell_value=sh.cell_value(i, columnnum)
        if a in str(cell_value):
            for j in c:
                outputs=str(sh.cell_value(i,j))
                b=b+outputs
            b=b+'\n'
    if b=='aa':
        b = '无该出发地数据！'
    roo=tk.Tk()
    t=tk.Text(roo,width=800,height=400)
    t.pack()

    t.insert('insert',b)
    roo.title(u'查询结果')
    roo.mainloop()
    return b
def searchdata323(a,b):
    x = xlrd.open_workbook('D1.xls')
    sh =x.sheet_by_index(0)
    nrows=sh.nrows
    ncols=sh.ncols
    a=airport_code(a)
    if a==None:
        a='*'
    c = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
    columnnum=2
    #表示航班信息表格中第几列
# input the searching string and column
#find the rows which you want to select and write to a txt file
    for i in range(nrows):
        cell_value=sh.cell_value(i, columnnum)
        if a in str(cell_value):
            for j in c:
                outputs=str(sh.cell_value(i,j))
                b=b+outputs
            b=b+'\n'
    if b=='aa':
        b = '无该出发地数据！'
    roo=tk.Tk()
    t=tk.Text(roo,width=800,height=400)
    t.pack()

    t.insert('insert',b)
    roo.title(u'查询结果')
    roo.mainloop()
    return b
def searchdata322(a,b):
    x = xlrd.open_workbook('D1.xls')
    sh =x.sheet_by_index(0)
    nrows=sh.nrows
    ncols=sh.ncols
    a=airport_code(a)
    c = (7,8,9,10,11,12,13,14,15)
    columnnum=2
    #表示航班信息表格中第几列
# input the searching string and column
#find the rows which you want to select and write to a txt file
    for i in range(nrows):
        cell_value=sh.cell_value(i, columnnum)
        if a in str(cell_value):
            for j in c:
                outputs=str(sh.cell_value(i,j))
                b=b+outputs
            b=b+'\n'
    if b=='aa':
        b = '无该出发地数据！'
    roo=tk.Tk()
    t=tk.Text(roo,width=800,height=400)
    t.pack()

    t.insert('insert',b)
    roo.title(u'查询结果')
    roo.mainloop()
    return b
def searchdata331(a,b):
    x = xlrd.open_workbook('D1.xls')
    sh =x.sheet_by_index(0)
    nrows=sh.nrows
    ncols=sh.ncols
    a=airport_code(a)
    if a==None:
        a='*'
    c = (0,1,2,3,4,5,6)
    columnnum=3
    #表示航班信息表格中第几列
# input the searching string and column
#find the rows which you want to select and write to a txt file
    for i in range(nrows):
        cell_value=sh.cell_value(i, columnnum)
        if a in str(cell_value):
            for j in c:
                outputs=str(sh.cell_value(i,j))
                b=b+outputs
            b=b+'\n'
    if b=='aa':
        b = '无该目的地数据'
    roo=tk.Tk()
    t=tk.Text(roo,width=800,height=400)
    t.pack()

    t.insert('insert',b)
    roo.title(u'查询结果')
    roo.mainloop()
    return b
def searchdata332(a,b):
    x = xlrd.open_workbook('D1.xls')
    sh =x.sheet_by_index(0)
    nrows=sh.nrows
    ncols=sh.ncols
    a=airport_code(a)
    if a==None:
        a='*'

    c = (7, 8, 9, 10, 11, 12, 13, 14, 15)
    columnnum=3
    #表示航班信息表格中第几列
# input the searching string and column
#find the rows which you want to select and write to a txt file
    for i in range(nrows):
        cell_value=sh.cell_value(i, columnnum)
        if a in str(cell_value):
            for j in c:
                outputs=str(sh.cell_value(i,j))
                b=b+outputs
            b=b+'\n'
    if b=='aa':
        b = '无该目的地数据'
    roo=tk.Tk()
    t=tk.Text(roo,width=800,height=400)
    t.pack()

    t.insert('insert',b)
    roo.title(u'查询结果')
    roo.mainloop()
    return b
def searchdata333(a,b):
    x = xlrd.open_workbook('D1.xls')
    sh =x.sheet_by_index(0)
    nrows=sh.nrows
    ncols=sh.ncols
    a=airport_code(a)
    if a==None:
        a='*'
    c = (0,1,2,3,4,5,6,7, 8, 9, 10, 11, 12, 13, 14, 15)
    columnnum=3
    #表示航班信息表格中第几列
# input the searching string and column
#find the rows which you want to select and write to a txt file
    for i in range(nrows):
        cell_value=sh.cell_value(i, columnnum)
        if a in str(cell_value):
            for j in c:
                outputs=str(sh.cell_value(i,j))
                b=b+outputs
            b=b+'\n'
    if b=='aa':
        b = '无该目的地数据'
    roo=tk.Tk()
    t=tk.Text(roo,width=800,height=400)
    t.pack()

    t.insert('insert',b)
    roo.title(u'查询结果')
    roo.mainloop()
    return b
def searchdata351(a,b):
    x = xlrd.open_workbook('D1.xls')
    sh =x.sheet_by_index(0)
    nrows=sh.nrows
    ncols=sh.ncols
    c = (0,1,2,3,4,5,6)
    columnnum=6
    #表示航班信息表格中第几列
# input the searching string and column
#find the rows which you want to select and write to a txt file
    for i in range(nrows):
        cell_value=sh.cell_value(i, columnnum)
        if a in str(cell_value):
            for j in c:
                outputs=str(sh.cell_value(i,j))
                b=b+outputs
            b=b+'\n'
    if b=='aa':
        b = '请输入括号内的的状态'

    roo=tk.Tk()
    t=tk.Text(roo,width=800,height=400)
    t.pack()

    t.insert('insert',b)
    roo.title(u'查询结果')
    roo.mainloop()
    return b
def searchdata352(a,b):
    x = xlrd.open_workbook('D1.xls')
    sh =x.sheet_by_index(0)
    nrows=sh.nrows
    ncols=sh.ncols

    c = (7, 8, 9, 10, 11, 12, 13, 14, 15)
    columnnum=6
    #表示航班信息表格中第几列
# input the searching string and column
#find the rows which you want to select and write to a txt file
    for i in range(nrows):
        cell_value=sh.cell_value(i, columnnum)
        if a in str(cell_value):
            for j in c:
                outputs=str(sh.cell_value(i,j))
                b=b+outputs
            b=b+'\n'
    if b=='aa':
        b = '请输入括号内的的状态'
    roo=tk.Tk()
    t=tk.Text(roo,width=800,height=400)
    t.pack()

    t.insert('insert',b)
    roo.title(u'查询结果')
    roo.mainloop()
    return b
def searchdata353(a,b):
    x = xlrd.open_workbook('D1.xls')
    sh =x.sheet_by_index(0)
    nrows=sh.nrows
    ncols=sh.ncols

    c = (0,1,2,3,4,5,6,7, 8, 9, 10, 11, 12, 13, 14, 15)
    columnnum=6
    #表示航班信息表格中第几列
# input the searching string and column
#find the rows which you want to select and write to a txt file
    for i in range(nrows):
        cell_value=sh.cell_value(i, columnnum)
        if a in str(cell_value):
            for j in c:
                outputs=str(sh.cell_value(i,j))
                b=b+outputs
            b=b+'\n'
    if b=='aa':
        b = '请输入括号内的的状态'
    roo=tk.Tk()
    t=tk.Text(roo,width=800,height=400)
    t.pack()

    t.insert('insert',b)
    roo.title(u'查询结果')
    roo.mainloop()
    return b
def searchdata343(a1,a2,b):
    x = xlrd.open_workbook('D1.xls')
    sh =x.sheet_by_index(0)
    nrows=sh.nrows
    ncols=sh.ncols
    a1=airport_code(a1)
    a2=airport_code(a2)
    if (a1==None)|(a2==None):
        a1='*'
        a2='*'
    c = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
    columnnum1=2
    columnnum2 =3
    #表示航班信息表格中第几列
# input the searching string and column
#find the rows which you want to select and write to a txt file
    for i in range(nrows):
        cell_value1 = sh.cell_value(i, columnnum1)
        cell_value2 = sh.cell_value(i, columnnum2)
        if (a1 in str(cell_value1)) & (a2 in str(cell_value2)):
            for j in c:
                outputs = str(sh.cell_value(i , j))
                b = b+outputs
            b = b+'\n'
    if b == 'aa':
        b = u'数据庞杂难以整理，暂无该航线数据！'

    roo = tk.Tk()
    roo.title('提示')
    t = tk.Text(roo, width=800, height=400)
    t.pack()

    t.insert('insert', b)
    roo.title(u'查询结果')
    roo.mainloop()
    return b
def searchdata341(a1,a2,b):
    x = xlrd.open_workbook('D1.xls')
    sh =x.sheet_by_index(0)
    nrows=sh.nrows
    ncols=sh.ncols
    a1=airport_code(a1)
    a2=airport_code(a2)
    if (a1==None)|(a2==None):
        a1='*'
        a2='*'
    c=(0,1,2,3,4,5,6)
    columnnum1=2
    columnnum2 =3
    #表示航班信息表格中第几列
# input the searching string and column
#find the rows which you want to select and write to a txt file
    for i in range(nrows):
        cell_value1=sh.cell_value(i, columnnum1)
        cell_value2 = sh.cell_value(i, columnnum2)
        if a1 in str(cell_value1):
            if a2 in str(cell_value2):
                for j in c:
                    outputs=str(sh.cell_value(i,j))
                    b=b+outputs
            b=b+'\n'
    if b=='aa':
        b = u'数据庞杂难以整理，暂无该航线数据！'
    roo = tk.Tk()
    t = tk.Text(roo, width=800, height=400)
    t.pack()

    t.insert('insert', b)
    roo.title(u'查询结果')
    roo.mainloop()
    return b
def searchdata342(a1,a2,b):
    x = xlrd.open_workbook('D1.xls')
    sh =x.sheet_by_index(0)
    nrows=sh.nrows
    ncols=sh.ncols
    a1=airport_code(a1)
    a2=airport_code(a2)
    if (a1==None)|(a2==None):
        a1='*'
        a2='*'
    c=(7,8,9,10,11,12,13,14,15)
    columnnum1=2
    columnnum2 =3
    #表示航班信息表格中第几列
# input the searching string and column
#find the rows which you want to select and write to a txt file
    for i in range(nrows):
        cell_value1=sh.cell_value(i, columnnum1)
        cell_value2 = sh.cell_value(i, columnnum2)
        if a1 in str(cell_value1):
            if a2 in str(cell_value2):
                for j in c:
                    outputs=str(sh.cell_value(i,j))
                    b=b+outputs
            b=b+'\n'

    if b=='aa':
        b = '数据庞杂难以整理，暂无该航线数据！'
    roo=tk.Tk()
    t=tk.Text(roo,width=800,height=400)
    t.pack()

    t.insert('insert',b)
    roo.title(u'查询结果')
    roo.mainloop()
    return b
def searchdata313(a,b):
    x = xlrd.open_workbook('D1.xls')
    sh =x.sheet_by_index(0)
    nrows=sh.nrows
    ncols=sh.ncols

    c = (0,1,2,3,4,5,6,7, 8, 9, 10, 11, 12, 13, 14, 15)
    columnnum=0
    #表示航班信息表格中第几列
# input the searching string and column
#find the rows which you want to select and write to a txt file
    for i in range(nrows):
        cell_value=sh.cell_value(i, columnnum)
        if a in str(cell_value):
            for j in c:
                outputs=str(sh.cell_value(i,j))
                b=b+outputs
            b=b+'\n'
    if b=='aa':
        b = '该日期下没有找到数据！'
    roo=tk.Tk()
    t=tk.Text(roo,width=800,height=400)
    t.pack()

    t.insert('insert',b)
    roo.title(u'查询结果')
    roo.mainloop()
    return b
def searchdata312(a,b):
    x = xlrd.open_workbook('D1.xls')
    sh =x.sheet_by_index(0)
    nrows=sh.nrows
    ncols=sh.ncols

    c=(7,8,9,10,11,12,13,14,15)
    columnnum=0
    #表示航班信息表格中第几列
# input the searching string and column
#find the rows which you want to select and write to a txt file
    for i in range(nrows):
        cell_value=sh.cell_value(i, columnnum)
        if a in str(cell_value):
            for j in c:
                outputs=str(sh.cell_value(i,j))
                b=b+outputs
            b=b+'\n'

    if b=='aa':
        b = '该日期下没有找到数据！'
    roo=tk.Tk()
    t=tk.Text(roo,width=800,height=400)
    t.pack()

    t.insert('insert',b)
    roo.title(u'查询结果')
    roo.mainloop()
    return b
def searchdata311(a,b):
    x = xlrd.open_workbook('D1.xls')
    sh =x.sheet_by_index(0)
    nrows=sh.nrows
    ncols=sh.ncols

    c=(0,1,2,3,4,5,6)
    columnnum=0
    #表示航班信息表格中第几列
# input the searching string and column
#find the rows which you want to select and write to a txt file
    for i in range(nrows):
        cell_value=sh.cell_value(i, columnnum)
        if a in str(cell_value):
            for j in c:
                outputs=str(sh.cell_value(i,j))
                b=b+outputs
            b=b+'\n'

    if b=='aa':
        b='该日期下没有找到数据！'
    roo=tk.Tk()
    t=tk.Text(roo,width=800,height=400)
    t.pack()

    t.insert('insert',b)
    roo.title(u'查询结果')
    roo.mainloop()
    return b
class basedesk():
    def __init__(self, master):
        self.root = master

        self.root.config()

        self.root.title('Base page')

        self.root.geometry('1600x800')
        root.title('基于echarts库的航班信息可视化系统')
        initface(self.root)


class initface():
    def __init__(self, master):
        self.master = master

        self.master.config()

        # 基准界面initface

        self.initface = tk.Frame(self.master, )

        self.initface.pack()

        Lab = tk.Label(self.initface, text='欢迎使用基于echarts库的航班信息可视化系统', compound='center', font=('微软雅黑', 30))
        Lab.pack()  # 设置主界面


        btn1 = tk.Button(self.initface, text='航线信息可视化', command=self.change1)
        btn1.pack()
        btn2 = tk.Button(self.initface, text='航班航线准点率预测', command=self.change2)
        btn2.pack()

        btn = tk.Button(self.initface, text='航班信息集成查询', command=self.change3)
        btn.pack()


    def change1(self,):
        webbrowser.open(f,new=1)
    def change2(self, ):
        self.initface.destroy()

        face2(self.master)
    def change3(self, ):
        self.initface.destroy()

        face3(self.master)

class face2():
    def __init__(self, master):
        self.master = master

        self.master.config()

        self.face2 = tk.Frame(self.master, )

        self.face2.pack()

        root.title('基于echarts库的航班信息可视化系统')
        var1 = StringVar()
        var2 = StringVar()

        label1 = tk.Label(self.face2, text=u"出发地（城市或机场代码）")
        label1.pack()
        en =tk.Entry(self.face2, textvariable=var1)
        en.pack()
        label2 = tk.Label(self.face2, text=u"目的地（城市或机场代码）")
        label2.pack()
        en1 =tk.Entry(self.face2, textvariable=var2)
        en1.pack()
        B =tk.Button(self.face2, text=u"搜索", command=lambda: path(var1.get(), var2.get()))
        B.pack()

        btn_back = tk.Button(self.face2, text='返回', command=self.back)
        btn_back.pack()




    def back(self):
        self.face2.destroy()

        initface(self.master)
class face3():
    def __init__(self, master):
        self.master = master

        self.master.config()

        self.face3 = tk.Frame(self.master, )

        self.face3.pack()
        root.title('基于echarts库的航班信息可视化系统')
        btn_back = tk.Button(self.face3, text='返回', command=self.back)

        btn_back.pack()

        bt1 = tk.Button(self.face3, text='按日期搜索航班信息', command=lambda: self.change1())
        bt1.pack()

        bt2 = tk.Button(self.face3, text='按出发地点搜索航班信息', command=lambda: self.change2())
        bt2.pack()

        bt3 = tk.Button(self.face3, text='按目的地点搜索航班信息', command=lambda: self.change3())
        bt3.pack()

        bt4 = tk.Button(self.face3, text='按航线搜索航班信息', command=lambda: self.change4())
        bt4.pack()

        bt5 = tk.Button(self.face3, text='按晚点状况搜索航班信息', command=lambda: self.change5())
        bt5.pack()

    def change1(self):
        self.face3.destroy()
        face3_1(self.master)

    def change2(self):
        self.face3.destroy()
        face3_2(self.master)

    def change3(self):
        self.face3.destroy()
        face3_3(self.master)

    def change4(self):
        self.face3.destroy()
        face3_4(self.master)

    def change5(self):
        self.face3.destroy()
        face3_5(self.master)


    def back(self):
        self.face3.destroy()
        initface(self.master)


class face3_1():
    #按日期搜索
    def __init__(self, master):
        self.master = master


        self.master.config()

        self.face3_1 = tk.Frame(self.master, )

        self.face3_1.pack()
        root.title('基于echarts库的航班信息可视化系统')
        var1=StringVar()
        b='aa'
        label1 = tk.Label(self.face3_1, text=u"请按标准格式输入日期信息（xx.xx.xx）:")
        label1.pack()

        en2 = tk.Entry(self.face3_1, textvariable=var1)
        en2.pack()
        B1 = tk.Button(self.face3_1, text='显示航班基本信息', command=lambda :searchdata311(var1.get(),b))
        B1.pack()
        B2 = tk.Button(self.face3_1, text='显示航班天气信息', command=lambda: searchdata312(var1.get(), b))
        B2.pack()
        B3 = tk.Button(self.face3_1, text='显示航班全部信息', command=lambda: searchdata313(var1.get(), b))
        B3.pack()
        btn_back = tk.Button(self.face3_1, text='返回', command=self.back)

        btn_back.pack()

    def back(self):
        self.face3_1.destroy()
        face3(self.master)
class face3_2():
    #按出发地搜索
    def __init__(self, master):
        self.master = master
        b='aa'
        self.master.config()

        self.face3_2 = tk.Frame(self.master, )

        self.face3_2.pack()
        root.title('基于echarts库的航班信息可视化系统')
        label1 = tk.Label(self.face3_2, text=u"请输入出发地点（城市或机场代码）")
        label1.pack()

        var1 = StringVar()
        en = tk.Entry(self.face3_2, textvariable=var1)
        en.pack()
        B1 = tk.Button(self.face3_2, text='显示航班基本信息',command=lambda :searchdata321(var1.get(),b))
        B1.pack()
        b2=tk.Button(self.face3_2, text='显示航班天气信息',command=lambda :searchdata322(var1.get(),b))
        b2.pack()
        b3=tk.Button(self.face3_2,text='显示航班全部信息',command=lambda :searchdata323(var1.get(),b))
        b3.pack()
        btn_back = tk.Button(self.face3_2, text='返回', command=self.back)

        btn_back.pack()

    def back(self):
        self.face3_2.destroy()
        face3(self.master)
class face3_3():
    #按目的地搜索
    def __init__(self, master):
        self.master = master

        self.master.config()

        self.face3_3 = tk.Frame(self.master, )
        b='aa'
        self.face3_3.pack()
        root.title('基于echarts库的航班信息可视化系统')
        label1 = tk.Label(self.face3_3, text=u"请输入目的地点（城市或机场代码）")
        label1.pack()

        var1 = StringVar()
        en = tk.Entry(self.face3_3, textvariable=var1)
        en.pack()
        B1 = tk.Button(self.face3_3, text='显示航班基本信息',command=lambda :searchdata331(var1.get(),b))
        B1.pack()
        b2 = tk.Button(self.face3_3, text='显示航班天气信息',command=lambda :searchdata332(var1.get(),b))
        b2.pack()
        b3 = tk.Button(self.face3_3, text='显示航班全部信息',command=lambda :searchdata333(var1.get(),b))
        b3.pack()
        btn_back = tk.Button(self.face3_3, text='返回', command=self.back)

        btn_back.pack()

    def back(self):
        self.face3_3.destroy()
        face3(self.master)

class face3_4():
    #按航线搜索
    def __init__(self, master):
        self.master = master
        b='aa'
        self.master.config()

        self.face3_4 = tk.Frame(self.master, )

        self.face3_4.pack()
        root.title('基于echarts库的航班信息可视化系统')
        label1 = tk.Label(self.face3_4, text=u"请输入出发地点（城市或机场代码）")
        label1.pack()
        var1 = StringVar()
        en = tk.Entry(self.face3_4, textvariable=var1)
        en.pack()
        label2 = tk.Label(self.face3_4, text=u"请输入目的地点（城市或机场代码）")
        label2.pack()

        var2 = StringVar()
        en2 = tk.Entry(self.face3_4, textvariable=var2)
        en2.pack()
        B1 = tk.Button(self.face3_4, text='显示航班基本信息',command=lambda :searchdata341(var1.get(),var2.get(),b))
        B1.pack()
        b2 = tk.Button(self.face3_4, text='显示航班天气信息',command=lambda :searchdata342(var1.get(),var2.get(),b))
        b2.pack()
        b3 = tk.Button(self.face3_4, text='显示航班全部信息',command=lambda :searchdata343(var1.get(),var2.get(),b))
        b3.pack()
        btn_back = tk.Button(self.face3_4, text='返回', command=self.back)

        btn_back.pack()

    def back(self):
        self.face3_4.destroy()
        face3(self.master)


class face3_5():
    #按晚点情况搜索
    def __init__(self, master):
        self.master = master

        self.master.config()

        self.face3_5 = tk.Frame(self.master, )
        b='aa'
        self.face3_5.pack()
        root.title('基于echarts库的航班信息可视化系统')
        label1 = tk.Label(self.face3_5, text=u"请按规定格式输入航班状况（晚点，备降，取消，正常）:")
        label1.pack()

        var1 = StringVar()
        en = tk.Entry(self.face3_5, textvariable=var1)
        en.pack()
        B1 = tk.Button(self.face3_5, text='显示航班基本信息',command=lambda :searchdata351(var1.get(),b))
        B1.pack()
        b2 = tk.Button(self.face3_5, text='显示航班天气信息',command=lambda :searchdata352(var1.get(),b))
        b2.pack()
        b3 = tk.Button(self.face3_5, text='显示航班全部信息',command=lambda :searchdata353(var1.get(),b))
        b3.pack()
        btn_back = tk.Button(self.face3_5, text='返回', command=self.back)

        btn_back.pack()

    def back(self):
        self.face3_5.destroy()
        face3(self.master)


if __name__=='__main__':
    root = tk.Tk()

    basedesk(root)
    root.mainloop()
