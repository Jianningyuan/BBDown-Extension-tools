from tkinter import Label, Tk
from tkinter.ttk import Entry,Button
from tkinter.messagebox import showerror
from sv_ttk import set_theme,use_dark_theme
import ctypes
from BD import *
from threading import Thread


win=Tk()
win.resizable(False,False)
win.iconbitmap('favicon.ico')
win.title("B站视频下载器")
set_theme("dark")
use_dark_theme()
ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
win.tk.call('tk', 'scaling', ScaleFactor/40)


def ThreadsOfDownload1P(BV):
        t1 = Thread(target=DownLoad, args=(BV,1))
        t1.start()
        win.destroy()
        t1.join()  # join() 等待线程终止，要不然一直挂起


def EntryOfPGet(entey):
    Result=entey.get()
    return Result


def RunShow(self):
    Show()


def ThreadOfDownloadMultiP():
    BV=EntryOfPGet(entry)
    P=EntryOfPGet(entryOfP)
    tOfMulti=Thread(target=DownLoad, args=(BV,P))
    tOfMulti.start()
    win.destroy()
    tOfMulti.join()


def Show():
    strbvid=entry.get()
    yesAndNoOfVideo=DownLoadInit(strbvid)
    if str(yesAndNoOfVideo) == "0":   #有无视频
        if ngp(strbvid) == "1":       #是否为1p
            ThreadsOfDownload1P(strbvid)
        else:
            Butt.destroy()
            Label(win,text="请输入下载视频的P数(如8 或1,2 或3-5 或ALL)").grid(row=1,column=0)
            entryOfP.grid(row=2,column=0)
            bu1.grid(row=3,column=0)
    else:
        showerror("错误","视频不存在!")


bu1=Button(win,text="下载",command=ThreadOfDownloadMultiP)
entryOfP=Entry(win)
entry=Entry(win)
entry.grid(row=0)
Butt=Button(win,text="下载",command=Show)
Butt.grid(row=1,column=0)
entry.bind("<Return>",RunShow)
win.mainloop()