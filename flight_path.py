# -*-coding:utf-8-*-
import xlrd

from tkinter import messagebox
from pyecharts import *
from airport_code import *
from search import *
import webbrowser
data=xlrd.open_workbook('d.xls')
sh=data.sheets()[0]
rows=sh.nrows
cols=sh.ncols
list_a=sh.col_values(2)
list_b=sh.col_values(3)
def path(a,b):
    try:
        a=airport_code(a)
        b=airport_code(b)
        x1=[]
        x1=search(a,b)

        if x1[0]!=True:
            raise RuntimeError('1')
        i=[u'延误概率：',str(x1[1])]
        l=''.join(i)





        a=airport_ch(a)
        b=airport_ch(b)



        style = Style(
            page_title = "基于echarts库的航班信息可视化系统",
            title_top="#fff",
            title_pos = "center",
            width=1200,
            height=600,
            background_color="#A9A9A9"
                        )
        data_path=[[a,b]]

        style_geo = style.add(
    #title = "基于echarts库的航班信息可视化系统",
    border_color='#000000',
    symbol_size='50',
    is_label_show=True,
    line_curve=0.2,
    line_opacity=0.6,
    legend_text_color="#000000",
    legend_pos="right",
    geo_normal_color='#FFFFFF',
    geo_effect_symbol="plane",
    geo_effect_color="#800000",
    geo_effect_symbolsize=15,
    label_color=['#a6c84c', '#ffa022', '#46bee9'],
    label_pos="right",
    label_formatter="{b}",
    label_text_color="#000000",
    label_text_size='25',
    label_text_font='宋体'
        )
        geolines = GeoLines(u"基于echarts库的航班信息可视化系统", **style.init_style)
        geolines.add(l, data_path,**style_geo)

        geolines.render()

        f='render.html'

        webbrowser.open(f,new=1)
    except:
        messagebox.showinfo(u"提示",u"没有找到数据")

        return 0
