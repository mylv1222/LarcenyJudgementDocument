# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 21:23:27 2018

@author: MilesGO
"""

#在st字符串中，找到pat字符的每一个出现位置

def isnum(ch):
    return ord(ch)>=ord('0') and ord(ch)<=ord('9')

#其实括号问题最准确的做法是用栈（但是这样直接用一个state应该不会有太大的问题）
def partThing(st):
    pats=set(['和','及','与','、','，',','])
    n=len(st)
    i=0
    state1=0
    state2=0
    res=[]
    while i<n:
        if(st[i]=='(' or st[i]=='（'):
            state1=1
        elif(st[i]==')' or st[i]=='）'):
            state1=0
        elif(state2==0 and (st[i]=='\'' or st[i]=='‘' or st[i]=='"' or st[i]=='“')):
            state2=1
        elif(state2==1 and (st[i]=='\'' or st[i]=='’' or st[i]=='"' or st[i]=='”')):
            state2=0
        elif(state1==0 and state2==0):
            if(st[i] in pats):
                if(st[i]==',' or st[i]=='，'):
                    if (i>0 and i<n-1 and isnum(st[i-1]) and isnum(st[i+1])):
                        i+=1
                        continue
                if(i>0 and st[i-1]=='以' and st[i]=='及'):
                    if(i>1):
                        res.append(st[0:i-1])
                    if(i+1<n):
                        st=st[i+1:]
                        i=0
                        n=len(st)
                        continue
                    else:
                        break
                if(i>0):
                    res.append(st[0:i])
                if(i+1<n):
                    st=st[i+1:]
                    i=0
                    n=len(st)
                    continue
        i+=1
    if(st!=''):
        res.append(st)
    return res

class item:
    def __init__(self):
        self.value=''
        self.name=''

def getValue(th):
    import re
    tmp=re.search(r'(?:鉴定价格?|购买价|咨询价|进货价|售价|面值|面额|价值|折值|约值|总值|共值|估值|估价|价格|总价|总计|值)为?(?:人民币)?(?P<Value>[0-9,，零一二三四五六七八九十百千万]+元)',th)
    if(tmp):
        return tmp.group('Value')
    return None
    #先找到价值，然后直接把括号去掉
    
def delThing(things,names):
    import re
    cp=things.copy()
    for th in cp:
        if(th==""):
            things.remove(th)
            continue
        if(re.search(r'被告人|销赃|作案|卖|次',th)):
            things.remove(th)
            continue
        if(re.search(r'以.*的?价格',th)):
            things.remove(th)
            continue
        if(th[0]=='的'):
            things.remove(th)
            continue
        for name in names:
            if(th.find(name)!=-1):
                things.remove(th)
                break