#-*- coding:utf-8 -*-

import urllib
import urllib2
import re
import webbrowser as web
import time

user=raw_input(b'请输入用户账号\n')
html='http://feeds.qzone.qq.com/cgi-bin/cgi_rss_out?uin='+user

name=[] #日志名字
url=[]  #日志地址
pubdate=[] #发日志时间
i=1
j=0

con=urllib.urlopen(html).read()

lognamere=re.compile(r'<title><!\[CDATA\[(.+?)\]\]></title>')
name=lognamere.findall(con)

urlre=re.compile(r'<link>(.+?)</link>')
url=urlre.findall(con)


#获取空间名
desre=re.compile(r'<description><!\[CDATA\[(.+?)\]\]></description>')
description=desre.findall(con)
if(description[0]!=''):
    print 'This Qzone\'s name is '+description[0].decode('utf-8')+'\n'
else:
    print 'Warning:This QQzone is limited!'


#获取用户名
if name!=[]:                       #判定是否限制用户
    username=name[0].decode('utf-8')
    print 'This user\'s name is '+username+'\n'
else:
    pass


datere=re.compile(r'<pubDate>(.+?)</pubDate>')
if url[0]!='':
    del url[0]
    for item in url:
        print item
        pubdate=datere.findall(con)
        print 'This article delivered on '+pubdate[i]+'\n'
        i+=1
    if(i!=1):     #判定是否限制用户
        print'Find end!\nThis page contains '+str(i-1)+' logs\n\n'

while j<i:
    print 'Opening',name[j].decode('utf-8'),':',url[j]
    web.open_new_tab(url[j])  
    time.sleep(5) 
    j+=1
else:
    pass




