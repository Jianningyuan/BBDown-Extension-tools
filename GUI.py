from cProfile import label
from tkinter import END, Tk
from tkinter.ttk import Entry,Button
from sv_ttk import set_theme,use_dark_theme
import ctypes
from BD import *


win=Tk()
win.iconbitmap('favicon.ico')
win.title("B站视频下载器")
set_theme("dark")
use_dark_theme()
ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
win.tk.call('tk', 'scaling', ScaleFactor/40)
def Show():
    str=entry.get()
    entry.delete(0,END)
    DownLoad(str)
    win.destroy()
entry=Entry(win)
entry.grid(row=0)
Button(win,text="下载",command=Show).grid(row=1,column=0)
win.mainloop()