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
    state=0
    res=[]
    while i<n:
        if(st[i]=='(' or st[i]=='（'):
            state=1
        elif(st[i]==')' or st[i]=='）'):
            state=0
        elif(state==0):
            if(st[i] in pats):
                if(st[i]==',' or st[i]=='，'):
                    if (i>0 and i<n-1 and isnum(st[i-1]) and isnum(st[i+1])):
                        i+=1
                        continue
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