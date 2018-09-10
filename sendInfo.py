# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 12:46:27 2018

@author: trist
"""

#sendInfo.py  
#!/usr/bin/env python 
#_*_coding:utf8_*_ 
import smtplib,config,threading
from email.header import Header
from email.mime.text import MIMEText


def connect():#定义一个方法，用来连接到邮箱服务器 
    try: 
        server=smtplib.SMTP(config.smtpServer,config.smtpPort) 
        server.ehlo()
        print("正在登录")
        server.login(config.smtpUser,config.smtpPwd) 
        return server 
    except Exception: 
        print("无法连接到邮箱服务器！") 

def sendInfo(server,to,subject,content,nickname):
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Mime-Version']='1.0' 
    msg['From']= Header(nickname, 'utf-8')    #这里可以进行伪造
    msg['To'] = Header(to , 'utf-8')
    msg['Subject'] = Header(subject , 'utf-8')

    #mailinfo = 
    server.sendmail(config.smtpUser,to,str(msg))


def myfunc(contents, subject, to, nickname): 
    server=connect() 
    sendInfo(server,to,subject,contents,nickname) 

def sendLoop(subject,contents,nickname,toAddr,num):
    cur = 0
    while cur < num: 
        timer=threading.Timer(0, myfunc(contents, subject, toAddr, nickname))
        timer.start() 
        cur = cur + 1
