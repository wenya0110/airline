# -*-coding:utf-8-*-
from tkinter import messagebox
from pyecharts import *
from airport_code import *
from search import *
import webbrowser








style = Style(

            title_top="#fff",
            title_pos = "center",
             width=4800,
            height=2400,
            background_color="#FDF5E6"
                        )
data_path=[[u'长沙',u'三亚'],
[u'哈尔滨',u'北京'],
 [u'哈尔滨',u'上海'],
 [u'哈尔滨',u'长沙'],
 [u'哈尔滨',u'昆明'],
 [u'哈尔滨',u'成都'],
 [u'北京',u'西安'],
 [u'北京',u'长沙'],
 [u'北京',u'乌鲁木齐'],
 [u'北京',u'兰州'],
 [u'北京',u'成都'],
 [u'北京',u'上海'],
 [u'北京',u'沈阳'],
 [u'西安',u'长沙'],
 [u'西安',u'成都'],
 [u'西安',u'昆明'],
 [u'西安',u'兰州'], [u'西安',u'上海'],
 [u'西安',u'乌鲁木齐'],
 [u'西安',u'沈阳'],
 [u'上海',u'长沙'],
 [u'上海',u'成都'],
 [u'上海',u'兰州'],
 [u'上海',u'昆明'],
[u'上海',u'成都'],
 [u'上海',u'乌鲁木齐'],
 [u'昆明',u'成都'],
 [u'昆明',u'长沙'],
 [u'昆明',u'南京'],
 [u'上海',u'南京'],
 [u'乌鲁木齐',u'兰州'],
 [u'兰州',u'成都'],
 [u'兰州',u'长沙'],
 [u'北京',u'昆明'],
 [u'上海',u'银川'],
 [u'重庆',u'郑州'],
[u'长沙',u'张家界'],
 [u'长沙',u'汕头']]
style_geo = style.add(
    border_color='#808080',
    symbol_size='10',
    is_label_show=True,
    line_curve=0.2,
    line_opacity=0.6,
    legend_text_color="#eee",
    legend_pos="right",
    geo_normal_color='#FFFFFF',
    geo_effect_symbol="plane",
    geo_effect_color="#800000",
    geo_effect_symbolsize=15,
    label_color=['#a6c84c', '#ffa022', '#46bee9'],
    label_pos="right",
    label_formatter="{b}",
    label_text_color="#000000",
    label_text_size='15'
        )
geolines = GeoLines(u"航班准点率预测", **style.init_style)
geolines.add('aa', data_path,**style_geo)
geolines.render()
f='quanbu.html'
webbrowser.open(f,new=1)
