# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 12:30:10 2018

@author: 16417
"""

import re

f=open('datetime.txt','r',encoding='utf8')
outf=open('time_structured','w',encoding='utf8')
times=f.readlines()
f.close()

for time in times:
    outf.write(time)
    p1='[\d同]'
    tmp=re.match(r'%s+年%s+月\w*?\b'%(p1,p1),time)
    if tmp:
        outf.write('   yes')
        outf.write('\n')
    else:
        outf.write('   no')
        outf.write('\n')