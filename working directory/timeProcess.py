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
        print('\t'+name+':',end='')
        if name=='Year':
            if(re.match(r'[同当]',info)):
                if(pYear!=''):
                    cYear=pYear
                    info=cYear
                else:
                    print('\t'+info+'年')
                    return
            print('\t'+info,end='')
            cYear=info
            print('年')
        if name=='Imprecise_month':
            print('\t年',end='')
            print(info)
        if name=='Season':
            print('\t'+info+'季')
        if name=='Month':
            if(re.match(r'[同当]',info)):
                if(pMonth!=''):
                    cMonth=pMonth
                    info=cMonth
                else:
                    print('\t'+info+'月')
                    return
            print('\t'+info+'月',end='')
            cMonth=info
            info=matcher.group('Mo')
            if info!=None:
                print('\t'+info,end='')
            print("")
        if name=='Imprecise_day':
            info=matcher.group('Id1')
            if info!=None:
                if len(info)==1:
                    print('\t月'+info,end='')
                else:
                    print('\t'+info,end='')
            info=matcher.group('Id2')
            if info!=None:
                if len(info)==2:
                    print('\t的'+info,end='')
                else:
                    print('\t'+info,end='')
            print("")
        if name=='Day':
            if(re.match(r'[同当]',info)):
                if(pDay!=''):
                    cDay=pDay
                    info=cDay
                else:
                    print('\t'+info+'日');
                    return
            print('\t'+info+'日',end='')
            cDay=info
            info=matcher.group('D1')
            if info!=None:
                print('\t'+info,end='')
            info=matcher.group('D2')
            if info!=None:
                if len(info)==2:
                    print('\t的'+info,end='')
                else:
                    print('\t'+info,end='')
            print("")
        if name=='Imprecise_hour':
            print('\t'+info)
        if name=='Hour':
            print('\t'+info+'时',end='')
            info=matcher.group('H')
            if info!=None:
                print('\t'+info,end='')
            print("")
        if name=='Minute':
            print('\t'+info+'分',end='')
            info=matcher.group('Mi')
            if info!=None:
                print('\t'+info,end='')
            print("")
        if name=='Second':
            print('\t'+info+'秒',end='')
            info=matcher.group('S')
            if info!=None:
                print('\t'+info,end='')
            print("")


def structTime(time,_preYear,_preMonth,_preDay):
    global pYear,pMonth,pDay
    pYear=_preYear
    pMonth=_preMonth
    pDay=_preDay
    
    #不带中文数字版
    #tmp=re.match(r'(?P<Year>[0-9]{4,4}|同|当)年(?P<Imprecise_month>[末底终初中])?(?:(?P<Season>[春夏秋冬])[天季])?(?P<Month>[0-9]{1,2}|同|当)月份?(?P<Mo>左右)?(?P<Imprecise_day>(?P<Id1>上旬|中旬|下旬|[末底终初中])?(?P<Id2>的一天|一天)?)?(?:(?P<Day>(?:[0-9]{1,2}|同|当|某))[日号](?P<D1>左右|前后)?(?P<D2>的?一天)?)?(?P<Imprecise_hour>凌晨|早晨|早上|晚上|傍晚|上午|中午|下午|深夜|半夜|夜间|夜晚|夜里|夜|早|中|晚)?(?:(?P<Hour>[0-9]{1,2}|某)(?:时|点钟?)(?P<H>左右|前后|许)?)?(?:(?P<Minute>[0-9]{1,2}|某)分(?P<Mi>左右|前后|许)?)?(?:(?P<Second>[0-9]{1,2}|某)秒(?P<S>左右|前后|许)?)?',time);
    #带中文数字版
    tmp=re.match(r'(?P<Year>[0-9零一二三四五六七八九]{4,4}|同|当)年(?P<Imprecise_month>[末底终初中])?(?:(?P<Season>[春夏秋冬])[天季])?(?P<Month>[0-9零一二三四五六七八九]{1,2}|同|当)月份?(?P<Mo>左右)?(?P<Imprecise_day>(?P<Id1>上旬|中旬|下旬|[末底终初中])?(?P<Id2>的一天|一天)?)?(?:(?P<Day>(?:[0-9零一二三四五六七八九]{1,2}|同|当|某))[日号](?P<D1>左右|前后)?(?P<D2>的?一天)?)?(?P<Imprecise_hour>凌晨|早晨|早上|晚上|傍晚|上午|中午|下午|深夜|半夜|夜间|夜晚|夜里|夜|早|中|晚)?(?:(?P<Hour>[0-9零一二三四五六七八九]{1,2}|某)(?:时|点钟?)(?P<H>左右|前后|许)?)?(?:(?P<Minute>[0-9零一二三四五六七八九]{1,2}|某)分(?P<Mi>左右|前后|许)?)?(?:(?P<Second>[0-9零一二三四五六七八九]{1,2}|某)秒(?P<S>左右|前后|许)?)?\b',time)
    
    print('\tComplete:\t',end='')
    print(tmp.group(0))
    extractTime(tmp,'Year')
    extractTime(tmp,'Imprecise_month')
    extractTime(tmp,'Season')
    extractTime(tmp,'Month')
    extractTime(tmp,'Imprecise_day')
    extractTime(tmp,'Day')
    extractTime(tmp,'Imprecise_hour')
    extractTime(tmp,'Hour')
    extractTime(tmp,'Minute')
    extractTime(tmp,'Second')
    return [cYear,cMonth,cDay]
