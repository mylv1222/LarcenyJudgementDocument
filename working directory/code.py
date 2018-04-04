# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 18:00:44 2018

@author: MilesGO
"""

debug=1 #debug模式
nn=[] #从头部信息抽取出来的被告人姓名列表
#datetime=[]
ths=[]

def printList(List): #打印列表的函数
    for item in List:
            print('\n\t'+item,end='')
    print('')
    

def extractInformation(text): #抽取信息的函数
    flag=-1
    lines=text.split('\n')
    exist_time=set()
    preYear=''
    preMonth=''
    preDay=''
    for line in lines:
        time=None
        names=None
        locations=None
        things=None
        money=None
        if line.find("陈述")!=-1 or line.find("供述")!=-1 or line.find("证实")!=-1 or line.find("证据")!=-1:
            continue
        
        #time=re.search(r'[\d同]+年[\d同]+月\w*?\b',line)
        #time=re.search(r'(?P<year>[0-9]{4,4}|同|当)年(?P<imprecise_month>[末底终初中])?(?:(?P<season>[春夏秋冬])[天季])?(?P<month>[0-9]{1,2}|同|当)月份?(?P<mo>左右)?(?P<imprecise_day>(?P<id1>上旬|中旬|下旬|[末底终初中])?(?P<id2>的一天|一天)?)?(?:(?P<day>(?:[0-9]{1,2}|同|当|某))[日号](?P<d1>左右|前后)?(?P<d2>的?一天)?)?(?P<imprecise_hour>凌晨|早晨|早上|晚上|傍晚|上午|中午|下午|深夜|半夜|夜间|夜晚|夜里|夜|早|中|晚)?(?:(?P<hour>[0-9]{1,2}|某)(?:时|点钟?)(?P<h>左右|前后|许)?)?(?:(?P<minute>[0-9]{1,2}|某)分(?P<mi>左右|前后|许)?)?(?:(?P<second>[0-9]{1,2}|某)秒(?P<s>左右|前后|许)?)?\b',line)
        time=re.search(r'(?P<Year>[0-9]{4,4}|同|当)年(?P<Imprecise_month>[末底终初中])?(?:(?P<Season>[春夏秋冬])[天季])?(?P<Month>[0-9]{1,2}|同|当)月份?(?P<Mo>左右)?(?P<Imprecise_day>(?P<Id1>上旬|中旬|下旬|[末底终初中])?(?P<Id2>的一天|一天)?)?(?:(?P<Day>(?:[0-9]{1,2}|同|当|某))[日号](?P<D1>左右|前后)?(?P<D2>的?一天)?)?(?P<Imprecise_hour>凌晨|早晨|早上|晚上|傍晚|上午|中午|下午|深夜|半夜|夜间|夜晚|夜里|夜|早|中|晚)?(?:(?P<Hour>[0-9]{1,2}|某)(?:时|点钟?)(?P<H>左右|前后|许)?)?(?:(?P<Minute>[0-9]{1,2}|某)分(?P<Mi>左右|前后|许)?)?(?:(?P<Second>[0-9]{1,2}|某)秒(?P<S>左右|前后|许)?)?\b',line);
        #if time==None:
            #time=re.search(r'[\d同]+年\w*\b',line)
        if time==None:
            continue
        time=time.group(0)
        
        if len(re.findall(r'月',time))>1 or len(re.findall(r'日',time))>1:
            continue 
        if exist_time.intersection(set([time]))!=set():
            continue #如果已包含该事件
        ptr=time.find("被告人")
        if ptr!=-1:
            time=time[0:ptr]
        if debug==1:
            print(time)
        
        names=re.search(r'被告人((?:[\w“”＊－·—]{2,6}?(?:（[^（）]*）)?(?:[、与及和]|伙同))*?[\w“”＊－·—]{2,6}?(?:（[^（）]*）)?)(?=(?:[0-9一二三四五六七八九十]+?人)?(?:同|结伙|共同|合伙|一起|酒后)?(?:多次|从|使用|利用|窜至|通过|途经|转悠|预谋|驾驶|流窜|逃窜|去到|携带|夹带|拿着|盗窃|盗得|窃得|偷得|盗走|窃走|偷走|盗取|窃取|偷取|扒得|扒走|扒取|取走|拿走|顺走|夹走|抢走|带走|推走|骑走|提走|提取|取款|夹出|扒窃|盗出|取出|[盗窃偷扒趁去转为来再途经预谋在至到流逃窜把将驾驶骑，,]))',line)
        if names==None:
            names=re.search(r'，([\w“”＊－（）、·—]*)(?:使用|利用|窜至|通过|途经|转悠|预谋|驾驶|流窜|逃窜|去到|携带|夹带|拿着|盗得|窃得|偷得|盗走|窃走|偷走|盗取|窃取|偷取|扒得|扒走|扒取|取走|拿走|顺走|夹走|抢走|带走|推走|骑走|提走|提取|取款|夹出|扒窃|盗出|取出|[趁去转为来再途经预谋在至到流逃窜把将驾驶骑，,])',line)
        if names==None:
            names=[]
            for name in nn:
                if(line.find(name)!=-1):
                    names.append(name)
        else:
            names=re.split(r'、|，|,|伙同|与|及|和|被告人',names.group(1))
            if names.count(""):
                names.remove("")
            ok=0
            for aname in names:
                if nn.count(aname)!=0:
                    ok=1
                if ok==1:
                    break
            if ok==0:
                for name in nn:
                    if(line.find(name)!=-1):
                        names.append(name)
            for i in range(len(names)):
                ptr=names[i].find("至")
                if ptr==-1:
                    ptr=names[i].find("到")
                if ptr!=-1:
                    names[i]=names[i][0:ptr]
        if debug==1:
            print(names)
        
        locations=re.search(r'(?:[\w（）()＊－·—]*?)(?:同|结伙|共同|一起|合伙)?(?:(?:在(?!逃)|[至到]))([\w（）\(\)\"“”\'‘’、\-＊－·—\.]+?)(?:采取|实施|结伙|预谋|以|伺机|共同|一起|合伙|[时内外旁边，。,盗窃偷])',line)
        if locations==None:
            locations=re.search(r'(?:[\w（）()＊－·—]*?)(?:同|结伙|共同|一起|合伙)?(?:翻入|去到|途经|窜至|潜入|逃至|窜到|路过|来到|进入)([\w（）\(\)\"“”\'‘’、\-＊－·—\.]+?)(?:采取|结伙|预谋|以|伺机|共同|一起|合伙|[内外旁边，。,盗窃偷])',line)
        if locations==None:
            locations=re.search(r'[将把]([\w（）\(\)\"“”\'‘’、\-＊－·—\.]+[内外旁边中])的',line)
        if locations==None:
            locations=re.search(r'位?于([\w\-\"\'‘’“”\.\(\)（）＊－·—]*的[\w\-\"\'‘’“”\.\(\)（）＊－·—]*)',line)
        if locations==None:
            locations=re.search(r'从([\w\-\"\'‘’“”\.\(\)（）＊－·—]*)(?:盗窃|盗得|窃得|偷得|盗走|窃走|偷走|盗取|窃取|偷取|扒得|扒走|扒取|取走|拿走|顺走|夹走|抢走|带走|推走|骑走|提走|提取|取款|夹出|盗出|取出|扒窃)',line)
        if locations==None:
            locations=re.search(r'(?:盗窃|盗得|窃得|偷得|盗走|窃走|偷走|盗取|窃取|偷取|扒得|扒走|扒取|取走|拿走|顺走|夹走|抢走|带走|推走|骑走|提走|提取|取款|夹出|盗出|取出|扒窃|在|位于|处于|到|至|窜至|途经|经过)((?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*市)(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*县)?(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*区)?(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*镇)?(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*路)?(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*村)?(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*家)?)',line)
        if locations==None:
            locations=re.search(r'(?:盗窃|盗得|窃得|偷得|盗走|窃走|偷走|盗取|窃取|偷取|扒得|扒走|扒取|取走|拿走|顺走|夹走|抢走|带走|推走|骑走|提走|提取|取款|夹出|盗出|取出|扒窃|在|位于|处于|到|至|窜至|途经|经过)((?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*市)?(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*县)(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*区)?(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*镇)?(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*路)?(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*村)?(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*家)?)',line)
        if locations==None:
            locations=re.search(r'(?:盗窃|盗得|窃得|偷得|盗走|窃走|偷走|盗取|窃取|偷取|扒得|扒走|扒取|取走|拿走|顺走|夹走|抢走|带走|推走|骑走|提走|提取|取款|夹出|盗出|取出|扒窃|在|位于|处于|到|至|窜至|途经|经过)((?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*市)?(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*县)?(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*区)(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*镇)?(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*路)?(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*村)?(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*家)?)',line)
        if locations==None:
            locations=re.search(r'(?:盗窃|盗得|窃得|偷得|盗走|窃走|偷走|盗取|窃取|偷取|扒得|扒走|扒取|取走|拿走|顺走|夹走|抢走|带走|推走|骑走|提走|提取|取款|夹出|盗出|取出|扒窃|在|位于|处于|到|至|窜至|途经|经过)((?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*市)?(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*县)?(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*区)?(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*镇)(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*路)?(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*村)?(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*家)?)',line)
        if locations==None:
            locations=re.search(r'(?:盗窃|盗得|窃得|偷得|盗走|窃走|偷走|盗取|窃取|偷取|扒得|扒走|扒取|取走|拿走|顺走|夹走|抢走|带走|推走|骑走|提走|提取|取款|夹出|盗出|取出|扒窃|在|位于|处于|到|至|窜至|途经|经过)((?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*市)?(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*县)?(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*区)?(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*镇)?(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*路)?(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*村)(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*家)?)',line)
        if locations==None:
            locations=re.search(r'(?:盗窃|盗得|窃得|偷得|盗走|窃走|偷走|盗取|窃取|偷取|扒得|扒走|扒取|取走|拿走|顺走|夹走|抢走|带走|推走|骑走|提走|提取|取款|夹出|盗出|取出|扒窃|在|位于|处于|到|至|窜至|途经|经过)((?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*市)?(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*县)?(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*区)?(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*镇)?(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*路)?(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*村)?(?:[\w\-\"\'‘’“”\.\(\)（）＊－·—]*家))',line)
        if locations==None:
            continue
        if debug==1:
            print(locations.group(1))
        
        #假设同一文书对于盗窃内容的描述方式一致
        things=[]
        th=re.findall(r'[将把](?:其)?((?:(?:(?:\d[,，]\d)|[\w\-\"\'‘’“”\.\(\)＊－·—]|(?:（[^（）]*?）))+?[、和及与])*(?:(?:(?:\d[,，]\d)|[\w\-\"\'‘’“”\.\(\)＊－·—]|(?:（[^（）]*?）))+?))(?:盗走|窃走|偷走|扒走|取走|顺走|拿走|提走|扒窃走|抢走|推走|骑走|放入)(?:了)?[\w\-\"\'‘’“”\.\(\)（）＊－·—]*\b',line)
        things.extend(th)
        things=list(set(things))
        if things.count(""):
            things.remove("")
        
        if len(things)==0:
            th=re.findall(r'对((?:(?:(?:\d[,，]\d)|[\w\-\"\'‘’“”\.\(\)＊－·—]|(?:（[^（）]*?）))+?[、和及与])*(?:(?:(?:\d[,，]\d)|[\w\-\"\'‘’“”\.\(\)＊－·—]|(?:（[^（）]*?）))+?))实施(?:了|其)?盗窃',line)
            things.extend(th)
        things=list(set(things))
        if things.count(""):
            things.remove("")
            
        if len(things)==0:
            th=re.findall(r'(?:(?:盗得)|(?:窃得)|(?:偷得)|(?:盗走)|(?:窃走)|(?:偷走)|(?:盗取)|(?:窃取)|(?:偷取)|(?:扒得)|(?:扒走)|(?:扒取)|(?:取走)|(?:拿走)|(?:顺走)|(?:夹走)|(?:抢走)|(?:带走)|(?:推走)|(?:骑走)|(?:提走)|(?:提取)|(?:取款)|(?:夹出)|(?:盗出)|(?:取出)|(?:扒窃))(?:了|其)?((?:(?:(?:\d[,，]\d)|[\w\-\"\'‘’“”\.\(\)＊－·—]|(?:（[^（）]*?）))+?[、和及与])*(?:(?:(?:\d[,，]\d)|[\w\-\"\'‘’“”\.\(\)＊－·—]|(?:（[^（）]*?）))+?))[并后，。,；;]',line)
            things.extend(th)
        things=list(set(things))
        if things.count(""):
            things.remove("")
            
        if len(things)==0:
            th=re.findall(r'(?:(?:盗窃)|[盗窃偷扒])(?:了|其)?((?:(?:(?:\d[,，]\d)|[\w\-\"\'‘’“”\.\(\)＊－·—]|(?:（[^（）]*?）))+?[、和及与])*(?:(?:(?:\d[,，]\d)|[\w\-\"\'‘’“”\.\(\)＊－·—]|(?:（[^（）]*?）))+?))[并后，。,；;（）\(\)]',line)
            things.extend(th)
        things=list(set(things))
        if things.count(""):
            things.remove("")
            
        if len(things)==0:
            th=re.findall(r'(?:(?:盗得)|(?:窃得)|(?:偷得)|(?:盗走)|(?:窃走)|(?:偷走)|(?:盗取)|(?:窃取)|(?:偷取)|(?:扒得)|(?:扒走)|(?:扒取)|(?:取走)|(?:拿走)|(?:顺走)|(?:夹走)|(?:带走)|(?:提走)|(?:抢走)|(?:推走)|(?:骑走)|(?:提取)|(?:取款)|(?:夹出)|(?:盗出)|(?:取出))((?:(?:(?:\d[,，]\d)|[\w\-\"\'‘’“”\.\(\)＊－·—]|(?:（[^（）]*?）))+?[、和及与])*(?:(?:(?:\d[,，]\d)|[\w\-\"\'‘’“”\.\(\)＊－·—]|(?:（[^（）]*?）))+?))[并后，。,；;]',line)
            things.extend(th)
        things=list(set(things))
        if things.count(""):
            things.remove("")
            
        if len(things)==0:
            th=re.findall(r'((?:(?:(?:\d[,，]\d)|[\w\-\"\'‘’“”\.\(\)＊－·—]|(?:（[^（）]*?）))+?[、和及与])*(?:(?:(?:\d[,，]\d)|[\w\-\"\'‘’“”\.\(\)＊－·—]|(?:（[^（）]*?）))+?))(?:(?:盗走)|(?:窃走)|(?:偷走)|(?:扒走)|(?:取走)|(?:拿走)|(?:顺走)|(?:提走)|(?:夹走)|(?:带走)|(?:抢走)|(?:夹出)|(?:盗出)|(?:取出)|(?:推走)|(?:骑走))',line)
            things.extend(th)
        things=list(set(things))
        if things.count(""):
            things.remove("")
            
        if len(things)==0:
            continue
        
        money=re.findall(r'((?:总|共|共计)?(?:价值|估值|价格)?(?:认定|鉴定)?(?:为|是)?(?:现金)?(?:人民币|港币|美金)?(?:[0-9一二三四五六七八九十百千万,，\.壹贰叁肆伍陆柒捌玖拾佰仟亿零整余]+元)(?:[0-9一二三四五六七八九十百千万,，\.壹贰叁肆伍陆柒捌玖拾佰仟亿零整余]+角)?(?:[0-9一二三四五六七八九十百千万,，\.壹贰叁肆伍陆柒捌玖拾佰仟亿零整余]+分)?(?:现金|人民币|港币|美金)?)',line)
        if money==None:
            continue
        
        if names==[]:
            continue
        if locations.group(1)=="":
            continue
        if things=="":
            continue
        
        print('################')
        print("Time")
        [preYear,preMonth,preDay]=timeProcess.structTime(time,preYear,preMonth,preDay)
        #datetime.append(time)  #datetime存储时间
        
        cp=names.copy()
        for name in cp:
            if len(name)>=10:
                names.remove(name)
        print("Criminal",end="")
        printList(names)
        
        print("Location\n\t",end="")
        locations=locations.group(1)
        ptr=locations.find("至")
        if ptr==-1:
            ptr=locations.find("到")
        if ptr==-1:
            ptr=locations.find("在")
        locations=locations[ptr+1:len(locations)]
        print(locations)
        
        cp=money.copy()
        for mm in cp:
            ptr=mm.find("现金")
            if ptr!=-1:
                ok=1
                for tt in things:
                    if tt.find(mm)!=-1:
                        ok=0
                    if ok==0:
                        break
                if ok==1:
                    things.insert(0,mm)
                money.remove(mm)
        
        cp=money.copy()
        for mm in cp:
            for tt in things:
                if tt.find(mm)!=-1:
                    money.remove(mm)
                    break
        
        
        print("Items",end="")
        printList(things)
        ths.extend(things)
        ths.append("");
        
        cp=money.copy()
        for mm in cp:
            ptr=mm.find("价值")
            if ptr==-1:
                ptr=mm.find("估价")
            if ptr==-1:
                ptr=mm.find("估值")
            if ptr==-1:
                money.remove(mm)
        
        print("Value",end="")
        printList(money)
        
        flag=1
    return flag

if __name__=='__main__':
    import re
    import sys
    import timeProcess
    debug=0
    old=sys.stdout
    if debug!=1:
        f=open("0.txt","r",encoding='utf8')
    else:
        f=open("tmp.txt","r",encoding='utf8')
    outf=open("out.txt","w",encoding="utf8")
    sys.stdout=outf
    files=f.read()
    f.close()
    files=re.split(r'(?<=\n)\*{5}(?!\*)',files);#分割不同的文书
    n=len(files)
    
    i=0
    file_count=0
    error_count=0
    not_count=0
    for file in files:
        if re.match(r'^[\s]*$',file):
            continue#如果整篇文章是空的
        file_count=file_count+1
        i=i+1#不同判决书之间的分割线
        
        info=re.findall('被告人?\S*\n',file);
        if len(info)==0:
            error_count=error_count+1
            continue
        
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
                error_count=error_count+1
                continue
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
            error_count=error_count+1
            continue
        p3=s3.find(info[0])
        s4=s3[p3:len(s3)]
        s3=s3[0:p3]
        
        info=re.findall(r'(?<=\n)\S*判决如下\S*\n',s4)
        if len(info)==0:
            error_count=error_count+1
            continue
        p4=s4.find(info[0])
        s5=s4[p4:len(s4)]
        s4=s4[0:p4]
        
        info=re.findall(r'[正副]本\S{0,20}\n',s5);
        if len(info)==0:
            error_count=error_count+1
            continue
        p5=s5.find(info[0])+len(info[0])
        s6=s5[p5:len(s5)]
        s5=s5[0:p5]    
      
        print(s1)
        
        #从s2中抽取出被告人姓名
        nn=[]
        lines=s2.split('\n')
        for line in lines:
            info=re.match('被告人(\w{2,5})[（）\(\),，\.。]',line)
            if info:
                nn.append(info.group(1))
        
        rec3=0
        rec4=0
        flag=-1
        pt=s3.find('审理查明')
        if pt!=-1:
            rec3=1
            flag=extractInformation(s3)
            if flag==1:
                print('**********************')
                continue
        pt=s4.find('审理查明')
        if pt!=-1:
            rec4=1
            flag=extractInformation(s4)
            if flag==1:
                print('**********************')
                continue
        pt=s3.find('指控')
        if pt!=-1:
            rec3=1
            flag=extractInformation(s3)
            if flag==1:
                print('**********************')
                continue
        if rec3==0:
            flag=extractInformation(s3)
            if flag==1:
                print('**********************')
                continue
        if rec4==0:
            flag=extractInformation(s4)
            if flag==1:
                print('**********************')
                continue
        not_count=not_count+1
    
    
    print("\n文书总数：",file_count)
    print("\n未识别裁判文书数: ",error_count)
    print("\n提取失败文书数：",not_count)
    
    '''
    df=open('datetime.txt','w',encoding='utf8')
    for dt in datetime:
        df.write(dt)
        df.write('\n')
    df.close()
    '''
    
    df=open('ths.txt','w',encoding='utf8')
    for th in ths:
        df.write(th+'\n')
    df.close()
    
    sys.stdout=old
    outf.close()