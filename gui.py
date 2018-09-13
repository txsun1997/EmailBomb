# -*- coding: utf-8 -*-

import tkinter as tk
import sendInfo, config
import tkinter.filedialog

def send():
    message = contentText.get('1.0',tk.END)
    title = subjectEntry.get()
    toAddr = toAddrEntry.get()
    num = int(numEntry.get())
    fromAddr = fromAddrEntry.get()
    filePath = filePathEntry.get()
    sendInfo.sendLoop(title,message,fromAddr,toAddr,num,filePath)
    state.set('已成功发送' + str(config.succNum) + '封邮件')

def login():
    server = sendInfo.connect()
    state.set(config.globalStr)

def attach():
    filename = tkinter.filedialog.askopenfilename()
    if filename != '':
        filePath.set(filename);
	
window = tk.Tk()
window.title("基于SMTP协议的邮件伪造和邮件炸弹")
window.geometry('450x320')
        
tk.Label(window, text='   发件箱:').place(x=20, y=20)
tk.Label(window, text='   收件箱:').place(x=20, y=45)
tk.Label(window, text='邮件标题:').place(x=20, y=70)
tk.Label(window, text='邮件内容:').place(x=20, y=95)
tk.Label(window, text='发送数量:').place(x=20, y=185)
tk.Label(window, text='添加附件').place(x=20, y=210)
tk.Label(window, text='当前状态:').place(x=20, y=240)

state = tk.StringVar()
state.set(config.globalStr)
stateLabel = tk.Label(window, textvariable=state, fg='red')
stateLabel.place(x=80, y=240)

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

filePath = tk.StringVar()
filePathEntry = tk.Entry(window, textvariable = filePath, width = 35)
filePathEntry.place(x=80, y=210)
     
attachBtn =  tk.Button(window, text='浏览', command=attach)
attachBtn.place(x=330, y=207)        
        
sendNum = tk.StringVar()
numEntry = tk.Entry(window, textvariable = sendNum, width = 20)
numEntry.place(x=80, y=185)
        
sendBtn = tk.Button(window, text='  登   录  ', command=login)
sendBtn.place(x=100, y=280)

sendBtn = tk.Button(window, text='发送邮件', command=send)
sendBtn.place(x=176, y=280)
        
exitBtn = tk.Button(window, text='退出程序', command=window.destroy)
exitBtn.place(x=250, y=280)

window.mainloop()
    
