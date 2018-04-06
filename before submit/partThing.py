# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 21:23:27 2018

@author: MilesGO
"""

#在st字符串中，找到pat字符的每一个出现位置

def isnum(ch):
    return ord(ch)>=ord('0') and ord(ch)<=ord('9')

def partThing(st): #按照一些分隔词和标点分离出多个物品
    pats=set(['和','及','与','、','，',','])
    n=len(st)
    i=0
    state1=0
    state2=0
    res=[]
    while i<n:
        if(st[i]=='(' or st[i]=='（'):
            state1=1#其实括号问题最准确的做法是用栈（但是这样直接用一个state应该不会有太大的问题）
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
                if(i<n-1 and st[i]=='及' and st[i+1]=='其'):
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

def getValue(th):
    import re
    tmp=re.search(r'(?:鉴定价格?|购买价|咨询价|进货价|售价|面值|面额|价值|折值|约值|总值|共值|估值|估价|价格|总价|总计|值)为?(?:人民币)?(?P<Value>[0-9,，\.零一二三四五六七八九十百千万零一二三四五六七八九十百千万壹贰叁肆伍陆柒捌玖拾佰仟亿]+)[多余]?元',th)
    if(tmp):
        return tmp.group('Value')
    return None
    #先找到价值，然后直接把括号去掉
    
def delThing(things,names):
    import re#删除一些提取错误的情况
    cp=things.copy()
    for th in cp:
        if(len(th)<3):
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
            
def getAttribute(vec):#提取物品的属性信息，例如颜色、品牌、型号等
    import re
    #color
    color=None
    tmp=re.search(r'(?=款|型号?|牌|[（）\(\)\"“”\'‘’、\-＊－·—\./]|\b)[\w（）\(\)\"“”\'‘’、\-＊－·—\./]+?色',vec[-1])
    if(tmp!=None):
        color=tmp.group(0)
        vec[-1]=re.subn(r'%s'%color,'',vec[-1])[0]
        
    #brand
    brand=None
    if(re.search(r'[金银铜]牌',vec[-1])==None):
        tmp=re.search(r'(?=款|型号?|[（）\(\)\"“”\'‘’、\-＊－·—\./]|\b)[\w（）\(\)\"“”\'‘’、\-＊－·—\./]+?牌',vec[-1])
        if(tmp!=None):
            brand=tmp.group(0)
            vec[-1]=re.subn(r'%s'%brand,'',vec[-1])[0]
    
    #my_type
    my_type=None
    tmp=re.search(r'(?=[（）\(\)\"“”\'‘’、\-＊－·—\./]|\b)[\w（）\(\)\"“”\'‘’、\-＊－·—\./]+(?:款|型号?)',vec[-1])
    if(tmp!=None):
        my_type=tmp.group(0)
        vec[-1]=re.subn(r'%s'%my_type,'',vec[-1])[0]
    return [vec,color,brand,my_type]

def outputPolishedThing(ths):#结构化程度更高的处理，并输出
    import re
    for th in ths:
        if(len(th)==0): #如果是空的就跳过
            continue
        
        val=getValue(th) #获取价值信息
        
        tmp=''#去掉括号内的内容
        state=0
        for ch in th:
            if(ch=='(' or ch=='（'):
                state=1
            elif(ch==')' or ch=='）'):
                state=0
            elif(state==0):
                tmp+=ch
        th=tmp
        
        vec=re.split(r'的',th) #按照的拆分出定语，这里默认物品在最后一个部分
        
        n=len(vec)#下面搜索有关价值的定语，如果单独作为一个定语，就去掉，如果是某个定语的一部分，则只删除关于价值的文字
        for i in range(n):#并删除“等物品”之类的后缀
            j=n-1-i
            tmp=re.search(r'(?:鉴定价格?|购买价|咨询价|进货价|售价|面值|面额|价值|折值|约值|总值|共值|估值|估价|价格|总价|总计|值)为?(?:人民币)?(?P<Value>[0-9,，\.零一二三四五六七八九十百千万零一二三四五六七八九十百千万壹贰叁肆伍陆柒捌玖拾佰仟亿]+[多余]?元)',vec[j]);
            if(tmp!=None):
                if((len(vec[j])-len(tmp.group(0)))<3):
                    vec.pop(j)
                    continue
                else:
                    vec[j]=re.subn(r'%s'%tmp.group(0),'',vec[j])[0]
            tmp=re.search(r'等(?:物品|赃物|财物|钱财|物)?',vec[j])
            if(tmp!=None):
                vec[j]=re.subn(r'%s'%tmp.group(0),'',vec[j])[0]
        
        if(len(vec)==0 or vec[-1]==''):
            continue
        
        #量词抽取
        tmp=re.search(r'(?:大?约|共计?|总共|合计?|各)?(?P<Num>[0-9\.]+|[两零一二三四五六七八九十百千万]+)[余多]?(?P<Word>公?[桶套付对组部只个包辆袋件块枚捆瓶箱斤条Kk根米盒张吨副升位匹头颗棵片株粒朵份把顶架支幅道面发门台])',vec[-1])
        amount=None
        if(tmp!=None and tmp.group('Num')!=None and tmp.group('Word')!=None):
            vec[-1]=re.subn(r'%s'%tmp.group(0),'',vec[-1])[0]
            amount=tmp.group('Num')+tmp.group('Word')
            if(amount=='零部'):
                amount=None
            else:
                amount=re.subn(r'各','',amount)[0]
                

        #XXXX内，一般认为是定语，抽取出来，插入到定语中
        n=len(vec)
        tmp=re.match('.*?内',vec[-1])
        if(tmp):
            tmp=tmp.group(0)
            vec[-1]=re.subn(r'%s'%tmp,'',vec[-1])[0]
            vec.insert(n-1,tmp)
            n+=1
        
        #颜色、品牌、型号等属性的抽取
        [vec,color,brand,my_type]=getAttribute(vec)
        
        #如果是物品是现金
        tmp=re.search('(?:(?P<Cash>[0-9，,\.零一二三四五六七八九十百千万壹贰叁肆伍陆柒捌玖拾佰仟亿]+)[余多]?元)',vec[-1])
        if(tmp):
            tmp=tmp.group('Cash')
            val=tmp
            vec=['现金']

        #如果物品开头是被害人李某某之类的，前整个物品的长度和被害人信息长度相近，则认为是错误信息
        tmp=re.match('(?:被害人)?\w{1,2}[某甲乙丙]{1,3}',vec[-1])
        if(tmp):
            tmp=tmp.group(0)
            if(len(vec[-1])-len(tmp)<3):
                vec=[]
        if(len(vec)==0 or vec[-1]==''):
            continue
        
            
        #在前面的定语中寻找颜色
        '''#这样处理后，又会引发新的问题，所以暂时先注释掉了
        if(color==None):
            n=len(vec)
            for i in range(n-1):
                tmp=re.match(r'\w{1,2}色',vec[i])
                if tmp:
                    color=tmp.group(0)
                    print('color hhhhh\t'+vec[i]+'\t'+color)
                    vec.pop(i)
                    break
        if(brand==None):
            n=len(vec)
            for i in range(n-1):
                tmp=re.search(r'(?=款|型号?|色|[（）\(\)\"“”\'‘’、\-＊－·—\./]|\b)[\w（）\(\)\"“”\'‘’、\-＊－·—\./]+牌',vec[i])
                if tmp:
                    brand=tmp.group(0)
                    print('brand hhhhh\t'+vec[i]+'\t'+brand)
                    vec[i]=re.subn(r'%s'%brand,'',vec[i])[0]
                    if(vec[i]==""):
                        vec.pop(i)
                    break
            
        if(my_type==None):
            n=len(vec)
            for i in range(n-1):
                tmp=re.search(r'(?=牌|色|[（）\(\)\"“”\'‘’、\-＊－·—\./]|\b)[\w（）\(\)\"“”\'‘’、\-＊－·—\./]+(?:型号?|款)',vec[i])
                if tmp:
                    my_type=tmp.group(0)
                    print('type hhhhh\t'+vec[i]+'\t'+my_type)
                    vec[i]=re.subn(r'%s'%my_type,'',vec[i])[0]
                    if(vec[i]==""):
                        vec.pop(i)
                    break
                
        if(amount==None):
            n=len(vec)
            for i in range(n-1):
                tmp=re.search(r'(?:大?约|共计?|总共|合计?|各)?(?:[0-9\.]+|[两零一二三四五六七八九十百千万]+)[余多]?公?[套付对组部只个包辆袋件块枚捆瓶箱斤条Kk根米盒张吨副升位匹头颗棵片株粒朵份把顶架支幅道面发门台]',vec[i])
                if tmp:
                    amount=tmp.group(0)
                    print('amount hhhhh\t'+vec[i]+'\t'+amount)
                    vec[i]=re.subn(r'%s'%amount,'',vec[i])[0]
                    if(vec[i]==""):
                        vec.pop(i)
                    break
        '''
        n=len(vec)
        print("Item")
        if(n>1):
            print('\tModifier:',end="")
            for i in range(n-1):
                print('\t'+vec[i]+'的',end="")
            print("")
        if(color!=None):
            print('\tColor:',end="")
            print('\t'+color)
        if(brand!=None):
            print('\tBrand:',end="")
            print('\t'+brand)
        if(my_type!=None):
            print('\tType:',end="")
            print('\t'+my_type)
        print('\tName:\t'+vec[-1])
        if(amount!=None):
            print('\tAmount:',end="")
            print('\t'+amount)
        if(val!=None):
            print('\tValue:',end="")
            print('\t'+val+'元')