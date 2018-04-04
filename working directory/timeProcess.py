# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 12:30:10 2018

@author: MilesGO
"""
import re


cYear=''
cMonth=''
cDay=''
pYear=''
pMonth=''
pDay=''

def extractTime(matcher,name):
    global cYear,cMonth,cDay
    global pYear,pMonth,pDay
    info=matcher.group(name)
    if(info!=None and info!=''):
        print(name+'\n\t',end='')
        if name=='year':
            if(re.match(r'[同当]',info)):
                if(pYear!=''):
                    cYear=pYear
                    info=cYear
                else:
                    print(' '+info+' -年')
                    return
            print(' '+info,end='')
            cYear=info
            print(' -年',end='')
        if name=='imprecise_month':
            print(' -年',end='')
            print(' '+info,end='')
        if name=='season':
            print(' '+info+'季',end='')
        if name=='month':
            if(re.match(r'[同当]',info)):
                if(pMonth!=''):
                    cMonth=pMonth
                    info=cMonth
                else:
                    print(' '+info+' -月')
                    return
            print(' '+info,end='')
            cMonth=info
            print(' -月',end='')
            info=matcher.group('mo')
            if info!=None:
                print(' -'+info,end='')
        if name=='imprecise_day':
            info=matcher.group('id1')
            if info!=None:
                if len(info)==1:
                    print(' -月'+info,end='')
                else:
                    print(' -'+info,end='')
            info=matcher.group('id2')
            if info!=None:
                if len(info)==2:
                    print(' -的'+info,end='')
                else:
                    print(' -'+info,end='')
        if name=='day':
            if(re.match(r'[同当]',info)):
                if(pDay!=''):
                    cDay=pDay
                    info=cDay
                else:
                    print(' '+info+' -日');
                    return
            print(' '+info,end='')
            cDay=info
            print(' -日',end='')
            info=matcher.group('d1')
            if info!=None:
                print(' -'+info,end='')
            info=matcher.group('d2')
            if info!=None:
                if len(info)==2:
                    print(' -的'+info,end='')
                else:
                    print(' -'+info,end='')
        if name=='imprecise_hour':
            print(' -'+info,end='')
        if name=='hour':
            print(' '+info+' -时',end='')
            info=matcher.group('h')
            if info!=None:
                print(' -'+info,end='')
        if name=='minute':
            print(' '+info+' -分',end='')
            info=matcher.group('mi')
            if info!=None:
                print(' -'+info,end='')
        if name=='second':
            print(' '+info+' -秒',end='')
            info=matcher.group('s')
            if info!=None:
                print(' -'+info,end='')
                
        print('\n',end='')

def structTime(time,_preYear,_preMonth,_preDay):
    global pYear,pMonth,pDay
    pYear=_preYear
    pMonth=_preMonth
    pDay=_preDay
    tmp=re.match(r'(?P<year>[0-9]{4,4}|同|当)年(?P<imprecise_month>[末底终初中])?(?:(?P<season>[春夏秋冬])[天季])?(?P<month>[0-9]{1,2}|同|当)月份?(?P<mo>左右)?(?P<imprecise_day>(?P<id1>上旬|中旬|下旬|[末底终初中])?(?P<id2>的一天|一天)?)?(?:(?P<day>(?:[0-9]{1,2}|同|当|某))[日号](?P<d1>左右|前后)?(?P<d2>的?一天)?)?(?P<imprecise_hour>凌晨|早晨|早上|晚上|傍晚|上午|中午|下午|深夜|半夜|夜间|夜晚|夜里|夜|早|中|晚)?(?:(?P<hour>[0-9]{1,2}|某)(?:时|点钟?)(?P<h>左右|前后|许)?)?(?:(?P<minute>[0-9]{1,2}|某)分(?P<mi>左右|前后|许)?)?(?:(?P<second>[0-9]{1,2}|某)秒(?P<s>左右|前后|许)?)?',time);
    print('complete\n\t',end='')
    print(tmp.group(0)+'\n',end='')
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
    return [cYear,cMonth,cDay]
