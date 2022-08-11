from tkinter import END, Tk
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
def RunShow(self):
    Show()
def Show():
    str1=entry.get()
    entry.delete(0,END)
    str2=DownLoadInit(str1)
    if str(str2) == "0":
        t1 = Thread(target=DownLoad, args=(str1,))
        t1.start()
        win.destroy()
        t1.join()  # join() 等待线程终止，要不然一直挂起
    else:
        showerror("错误","视频不存在!")
entry=Entry(win)
entry.grid(row=0)
Button(win,text="下载",command=Show).grid(row=1,column=0)
entry.bind("<Return>",RunShow)
win.mainloop()