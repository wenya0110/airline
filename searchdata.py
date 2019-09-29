# -*-coding:utf-8-*-
import json
import xlrd
import pandas
import sys
import tkinter as tk
from maininterface import face3_1
reload(sys)
sys.setdefaultencoding('utf8')


x = xlrd.open_workbook('D1.xls')
sh =x.sheet_by_index(0)
nrows=sh.nrows
ncols=sh.ncols


columnnum=0
    #表示航班信息表格中第几列
# input the searching string and column




#find the rows which you want to select and write to a txt file
for i in range(nrows):
    cell_value=sh.cell_value(i, columnnum)
    if a in str(cell_value):
        outputs=sh.row_values(i)

