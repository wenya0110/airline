# -*-coding:utf-8-*-
import pandas as pd
import xlrd

def search(a,b):
    df = pd.read_excel('D.xls')

    x = []
    x = df[((df[u'aa']) == a) & ((df[u'bb']) == b)]['cc']
    y=x.values

    if y[0]!=-1:
        return [True,y[0]]
