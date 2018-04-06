# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 18:00:44 2018

@author: MilesGO
"""

if __name__=='__main__':
    import re
    import sys
    import myFunction
    old=sys.stdout
    f=open("0.txt","r",encoding='utf8')
    outf=open("out.txt","w",encoding="utf8")
    sys.stdout=outf
    files=f.read()
    f.close()
    files=re.split(r'(?<=\n)\*{5}(?!\*)',files);#分割不同的文书
    n=len(files)#一共有n个文书
    
    i=0
    file_count=0
    error_count=0
    not_count=0
    for file in files:
        if re.match(r'^[\s]*$',file):
            continue#如果整篇文章是空的
        file_count=file_count+1
        i=i+1
        
        [flag,s1,s2,s3,s4,s5,s6]=myFunction.divideText(file)
        if flag==1:
            error_count+=1
            continue

        #裁判文书识别码
        code=re.search(r'[0-9A-Z\-]{36}',s1)
        code=code.group(0)
        
        #从s2中抽取出被告人姓名
        nn=[]
        lines=s2.split('\n')
        for line in lines:
            info=re.match('被告人(\w{2,5})[（）\(\),，\.。]',line)
            if info:
                nn.append(info.group(1))
        
        #从s3或s4中抽取结构化信息
        rec3=0
        rec4=0
        flag=-1
        pt=s3.find('审理查明')
        if pt!=-1:
            rec3=1
            flag=myFunction.extractInformation(s3,code,nn)
            if flag==1:
                continue
        pt=s4.find('审理查明')
        if pt!=-1:
            rec4=1
            flag=myFunction.extractInformation(s4,code,nn)
            if flag==1:
                continue
        pt=s3.find('指控')
        if pt!=-1:
            rec3=1
            flag=myFunction.extractInformation(s3,code,nn)
            if flag==1:
                continue
        if rec3==0:
            flag=myFunction.extractInformation(s3,code,nn)
            if flag==1:
                continue
        if rec4==0:
            flag=myFunction.extractInformation(s4,code,nn)
            if flag==1:
                continue
        not_count=not_count+1
    
    
    print("\n文书总数：",file_count)
    print("\n未识别裁判文书数: ",error_count)
    print("\n提取失败文书数：",not_count)
    
    sys.stdout=old
    outf.close()