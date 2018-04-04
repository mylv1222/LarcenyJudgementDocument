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
    if(matcher.group(name)!=None):
        info=matcher.group(name)
        if(info==''):
            return
        outf.write(name)
        outf.write('： ')
        outf.write(info)
        outf.write('\n')

for time in times:
    #outf.write(time)
    #p1='[\d同]'
    #tmp=re.match(r'%s+年%s+月\w*?\b'%(p1,p1),time)
    #tmp=re.match(r'(?P<year>[0-9]{4,4}年)(?P<month>[0-9]{1,2}月)(?P<day>[0-9]{1,2}日)?',time)
    #tmp=re.match(r'(?P<year>[0-9]{4,4}|同|当)年(?P<imprecise_month>初|底|中|终)?(?P<season>[春夏秋冬][天季])?(?P<month>[0-9]{1,2}|同|当)月份?(?P<imprecise_day>(?:[底初中]|上旬|中旬|下旬)(?:的一天|一天)?)?(?P<day>(?:[0-9]{1,2}|同|当|某)[日号](?:左右|前后))?(?P<imprecise_hour>凌晨|早|中|晚|早上|晚上|傍晚|上午|中午|下午|深夜|半夜|夜间|夜晚|夜里)?(?P<hour>[0-9]{1,2}(?:时|点钟?)(?:左右|前后|许))?(?P<minute>[0-9]{1,2}分(?:左右|前后))?(?P<second>[0-9]{1,2}秒(?:左右|前后))?',time);
    outf.write('*******************\n')
    outf.write(time)
    outf.write('\n')
    tmp=re.match(r'(?P<year>[0-9]{4,4}|同|当)年(?P<imprecise_month>[末底终初中])?(?P<season>[春夏秋冬][天季])?(?P<month>[0-9]{1,2}|同|当)月份?(?:左右)?(?P<imprecise_day>(?:上旬|中旬|下旬|[末底终初中])?(?:的一天|一天)?)?(?P<day>(?:[0-9]{1,2}|同|当|某)[天日号](?:左右|前后)?(?:的?一天)?)?(?P<imprecise_hour>凌晨|早晨|早上|晚上|傍晚|上午|中午|下午|深夜|半夜|夜间|夜晚|夜里|夜|早|中|晚)?(?P<hour>[0-9]{1,2}(?:时|点钟?)(?:左右|前后|许)?)?(?P<minute>[0-9]{1,2}分(?:左右|前后|许)?)?(?P<second>[0-9]{1,2}秒(?:左右|前后|许)?)?\b',time);
    if tmp:
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
