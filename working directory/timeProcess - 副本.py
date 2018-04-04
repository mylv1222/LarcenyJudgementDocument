# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 12:30:10 2018

@author: 16417
"""

import re

f=open('datetime.txt','r',encoding='utf8')
outf=open('time_structured.txt','w',encoding='utf8')
times=f.readlines()
f.close()


def extractTime(matcher,name):
    info=matcher.group(name)
    if(info!=None and info!=''):
        outf.write(name+'\n\t')
        if name=='year':
            outf.write(' '+info)
            outf.write(' -年')
        if name=='imprecise_month':
            outf.write(' -年')
            outf.write(' '+info)
        if name=='season':
            outf.write(' '+info+'季')
        if name=='month':
            outf.write(' '+info)
            outf.write(' -月')
            info=matcher.group('mo')
            if info!=None:
                outf.write(' -'+info)
        if name=='imprecise_day':
            info=matcher.group('id1')
            if info!=None:
                if len(info)==1:
                    outf.write(' -月'+info)
                else:
                    outf.write(' -'+info)
            info=matcher.group('id2')
            if info!=None:
                if len(info)==2:
                    outf.write(' -的'+info)
                else:
                    outf.write(' -'+info)
        if name=='day':
            outf.write(' '+info)
            outf.write(' -日')
            info=matcher.group('d1')
            if info!=None:
                outf.write(' -'+info)
            info=matcher.group('d2')
            if info!=None:
                if len(info)==2:
                    outf.write(' -的'+info)
                else:
                    outf.write(' -'+info)
        if name=='imprecise_hour':
            outf.write(' -'+info)
        if name=='hour':
            outf.write(' '+info+' -时')
            info=matcher.group('h')
            if info!=None:
                outf.write(' -'+info)
        if name=='minute':
            outf.write(' '+info+' -分')
            info=matcher.group('mi')
            if info!=None:
                outf.write(' -'+info)
        if name=='second':
            outf.write(' '+info+' -秒')
            info=matcher.group('s')
            if info!=None:
                outf.write(' -'+info)
                
        outf.write('\n')

for time in times:
    outf.write('*******************\n')
    outf.write('origin\n\t'+time+'\n')
    tmp=re.match(r'(?P<year>[0-9]{4,4}|同|当)年(?P<imprecise_month>[末底终初中])?(?:(?P<season>[春夏秋冬])[天季])?(?P<month>[0-9]{1,2}|同|当)月份?(?P<mo>左右)?(?P<imprecise_day>(?P<id1>上旬|中旬|下旬|[末底终初中])?(?P<id2>的一天|一天)?)?(?:(?P<day>(?:[0-9]{1,2}|同|当|某))[日号](?P<d1>左右|前后)?(?P<d2>的?一天)?)?(?P<imprecise_hour>凌晨|早晨|早上|晚上|傍晚|上午|中午|下午|深夜|半夜|夜间|夜晚|夜里|夜|早|中|晚)?(?:(?P<hour>[0-9]{1,2}|某)(?:时|点钟?)(?P<h>左右|前后|许)?)?(?:(?P<minute>[0-9]{1,2}|某)分(?P<mi>左右|前后|许)?)?(?:(?P<second>[0-9]{1,2}|某)秒(?P<s>左右|前后|许)?)?',time);
    if tmp:
        outf.write('complete\n\t')
        outf.write(tmp.group(0)+'\n')
        extractTime(tmp,'year')
        extractTime(tmp,'imprecise_month')
        extractTime(tmp,'season')
        extractTime(tmp,'month')
        extractTime(tmp,'imprecise_day')
        extractTime(tmp,'day')
        extractTime(tmp,'imprecise_hour')
        extractTime(tmp,'hour')
        extractTime(tmp,'minute')
        extractTime(tmp,'second')
    else:
        outf.write('no\n');
