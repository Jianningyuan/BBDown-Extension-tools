from tkinter import Label, Tk, END
from tkinter.ttk import Entry,Button
from tkinter.messagebox import showerror,showinfo
from sv_ttk import set_theme,use_dark_theme
import ctypes
from BD import *
from threading import Thread

win=Tk()
win.resizable(False,False)
win.iconbitmap('icon.ico')
win.title("B站视频下载器")
set_theme("dark")
use_dark_theme()
ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
win.tk.call('tk', 'scaling', ScaleFactor/40)


def SplitTextAndCompareNumber(text,splitChar,compareNumber):
    splitTextArr=str(text).split(str(splitChar))
    splitTextArr.sort()
    for i in splitTextArr:
        if i=="":
            return False
    resultOfsplitText=splitTextArr[len(splitTextArr)-1]
    if int(resultOfsplitText)<=int(compareNumber):
        return True
    else:
        return False


def VerifyThatTheInputIsLegitimateOfP(legitimateOfP):
    text=entryOfP.get()
    if text:
        try:
            num=int(text)
            if num<=int(legitimateOfP):
                return True
            else:
                return False
        except Exception as e:
            if "," in text or "-" in text or "ALL" in text or "all" in text:
                listOfPOrd=["48","49","50","51","52","53","54","55","56","57","45","44","65","97","76","108"] # 分别为 0，1，2，3，4，5，6，7，8，9，“-”，“,”,A,a,L,l(均为str)
                for i in text:
                    if str(ord(i)) in listOfPOrd:
                        pass
                    else:
                        return False
                if "," in text:
                    #查看“，”后的数值是否小于等于legitimate
                    resultOfDouHao=SplitTextAndCompareNumber(text,",",legitimateOfP)      # 返回值合法为Ture，不合法为False
                    return resultOfDouHao
                elif "-" in text:
                    #查看“-”后的数值是否小于等于legitimate
                    resultOfHengGang=SplitTextAndCompareNumber(text,"-",legitimateOfP)    # 返回值合法为Ture，不合法为False
                    return resultOfHengGang
            else:
                return False
    else:
        return False


def ThreadsOfDownload1P(BV):
        t1 = Thread(target=DownLoad, args=(BV,1))
        t1.start()
        buttonOfBV.grid(row=2,column=0)
        t1.join()  # join() 等待线程终止，要不然一直挂起


def EntryOfPGet(entey):
    Result=entey.get()
    return Result


def RunShow(self):
    Show()


def ThreadOfDownloadMultiP():
    BV=EntryOfPGet(entry)
    P=EntryOfPGet(entryOfP)
    if VerifyThatTheInputIsLegitimateOfP(ngp(BV))==True:
        tOfMulti=Thread(target=DownLoad, args=(BV,P))
        tOfMulti.start()
        tOfMulti.join()
        lab.grid_forget()
        entryOfP.grid_forget()
        entry.config(state="enable")
        entry.delete(0,END)
        bu1.grid_forget()
        Butt.grid(row=3,column=0)
        buttonOfBV.grid(row=4,column=0)
    else:
        showerror("警告","P数超出范围或输入有误!")


def RunThreadOfDownloadMultiP(self):
    ThreadOfDownloadMultiP()

def Show():
    global lab
    strbvid=entry.get()
    if str(len(strbvid))=="12":
        yesAndNoOfVideo=DownLoadInit(strbvid)
        if str(yesAndNoOfVideo) == "0":   #有无视频
            if ngp(strbvid) == "1":       #是否为1p
                ThreadsOfDownload1P(strbvid)
                entry.delete(0,END)
            else:
                entry.config(state='disable')
                Butt.grid_forget()
                buttonOfBV.grid_forget()
                lab=Label(win,text="请输入下载视频的P数(如8 或1,2 或3-5 或ALL)")
                lab.grid(row=1,column=0)
                entryOfP.grid(row=2,column=0)
                bu1.grid(row=3,column=0)
        else:
            showerror("错误","视频不存在!")
    else:
        showerror("警告","BV号不正确!")


def ExitOfWindow():
    win.destroy()


bu1=Button(win,text="下载",command=ThreadOfDownloadMultiP)
buttonOfBV=Button(win,text="取消",command=ExitOfWindow)
entryOfP=Entry(win)
entryOfP.bind("<Return>",RunThreadOfDownloadMultiP)
entry=Entry(win)
entry.grid(row=0)
Butt=Button(win,text="下载",command=Show)
Butt.grid(row=1,column=0)
entry.bind("<Return>",RunShow)
win.mainloop()