# -*-coding:utf-8-*-

airport1={
    'HRB': u'哈尔滨',
    'PEK':u'北京',
    'KMG':u'昆明',
    'CTU':u'成都',
    'NKG':u'南京',
    'CSX':u'长沙',
    'LHW':u'兰州',
    'PVG':u'上海',
    'SHA':u'上海',
    'URC':u'乌鲁木齐',
    'INC':u'银川',
    'XIY':u'西安',
    'SHE':u'沈阳',
    'JGN':u'酒泉',
    'SYX':u'三亚',
    'CKG':u'重庆',
    'CGO':u'郑州',
    'DYG':u'张家界',
    'LZY':u'林芝',
    'SWA':u'汕头',
}
airport2={
       u'哈尔滨':'HRB',
       u'北京':'PEK',
       u'昆明':'KMG',
       u'成都':'CTU',
       u'南京':'NKG',
       u'长沙':'CSX',
       u'兰州':'LHW',
       u'上海浦东':'PVG',
       u'上海虹桥':'SHA',
       u'乌鲁木齐':'URC',
       u'银川':'INC',
       u'西安':'XIY',
       u'沈阳':'SHE',
      u'酒泉':'JGN'


}


def airport_ch(a):

   if a>=u'鿿' or a<=u'一':
        return airport1.get(a)
   else:
       return a

def airport_code(b):
    if b >= u'鿿' or b <= u'一':
        return b
    else:
        return airport2.get(b)
