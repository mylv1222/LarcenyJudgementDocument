# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 16:48:54 2018

@author: MilesGO
"""

def divideText(file):
    import re
    info=re.findall('被告人?\S*\n',file);
    if len(info)==0:
        return [1,None,None,None,None,None,None]
    
    p1=file.find(info[0])
    s1=file[0:p1]
    s2=file[p1:len(file)]
    
    info=re.findall('(?<=[\n])[\S]*?检\S{1,15}?诉\S*\n',s2);
    if len(info)!=0:
        p2=s2.find(info[0])+len(info[0])
        s3=s2[p2:len(s2)]
        s2=s2[0:p2]
    else:
        info=re.findall('(?<=\n)\S*?指控\S*\n',s2)
        if len(info)==0:
            return [1,None,None,None,None,None,None]
        p2=s2.find(info[0])
        s3=s2[p2:len(s2)]
        s2=s2[0:p2]
    
    info=re.findall(r'(?<=\n)\S*查明\.*',s3)
    if len(info)==0:
        info=re.findall(r'(?<=\n)\S*证据\S*\n',s3)
    if len(info)==0:
        info=re.findall(r'(?<=\n)\S*认定\S*\n',s3)
    if len(info)==0:
        info=re.findall(r'(?<=\n)\S*证实\S*\n',s3)
    if len(info)==0:
        return [1,None,None,None,None,None,None]
    p3=s3.find(info[0])
    s4=s3[p3:len(s3)]
    s3=s3[0:p3]
    
    info=re.findall(r'(?<=\n)\S*判决如下\S*\n',s4)
    if len(info)==0:
        return [1,None,None,None,None,None,None]
    p4=s4.find(info[0])
    s5=s4[p4:len(s4)]
    s4=s4[0:p4]
    
    info=re.findall(r'[正副]本\S{0,20}\n',s5);
    if len(info)==0:
        return [1,None,None,None,None,None,None]
    p5=s5.find(info[0])+len(info[0])
    s6=s5[p5:len(s5)]
    s5=s5[0:p5]    
    return [0,s1,s2,s3,s4,s5,s6]