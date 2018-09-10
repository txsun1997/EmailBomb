# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 18:42:23 2018

@author: lenovo
"""

import tkinter as tk
import sendInfo

def attach():
    pass

def send():
    message = contentText.get('1.0',tk.END)
    title = subjectEntry.get()
    toAddr = toAddrEntry.get()
    num = int(numEntry.get())
    fromAddr = fromAddrEntry.get()
    sendInfo.sendLoop(title,message,fromAddr,toAddr,num)

def exitP():
    pass

window = tk.Tk()
window.title("基于SMTP协议的邮件伪造和邮件炸弹")
window.geometry('450x300')
        
tk.Label(window, text='   发件箱:').place(x=20, y=20)
tk.Label(window, text='   收件箱:').place(x=20, y=45)
tk.Label(window, text='邮件标题:').place(x=20, y=70)
tk.Label(window, text='邮件内容:').place(x=20, y=95)
tk.Label(window, text='发送数量:').place(x=20, y=185)
tk.Label(window, text='添加附件').place(x=20, y=210)
        
fromAddr = tk.StringVar()
fromAddr.set(" [请输入发件人地址，如xxxxx@example.com]")
fromAddrEntry = tk.Entry(window, textvariable = fromAddr, width = 40)
fromAddrEntry.place(x=80, y=20)
        
toAddr = tk.StringVar()
toAddr.set(" [请输入收件人地址，如xxxxx@example.com]")
toAddrEntry = tk.Entry(window, textvariable = toAddr, width = 40)
toAddrEntry.place(x=80, y=45)
        
subject = tk.StringVar()
subject.set(" [请输入邮件标题...]")
subjectEntry = tk.Entry(window, textvariable = subject, width = 40)
subjectEntry.place(x=80, y=70)
        
contentText = tk.Text(window, width = 40, height = 6)
contentText.place(x=80, y=95)
contentText.insert(tk.END, " 邮件内容...")

attachBtn =  tk.Button(window, text='浏览', command=attach)
attachBtn.place(x=80, y=207)        
        
sendNum = tk.StringVar()
numEntry = tk.Entry(window, textvariable = sendNum, width = 20)
numEntry.place(x=80, y=185)
        
sendBtn = tk.Button(window, text='发送邮件', command=send)
sendBtn.place(x=150, y=250)
        
exitBtn = tk.Button(window, text='退出程序', command=exitP)
exitBtn.place(x=250, y=250)
        
curWidth = window.winfo_width()  # get current width
curHeight = window.winfo_height()  # get current height
scnWidth, scnHeight = window.maxsize()  # get screen width and height
tmpcnf = '+%d+%d' % ((scnWidth - curWidth) / 2, (scnHeight - curHeight) / 2)
window.geometry(tmpcnf)
window.mainloop()







    