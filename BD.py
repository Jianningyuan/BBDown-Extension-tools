from fileinput import filename
from os import listdir,path,rename,mkdir,remove,walk
from re import sub
from requests import get
from urllib import response
from requests import get
from json import dumps,loads
from time import sleep
from subprocess import call


# bv2av用于bv号转av号
def bv2av(x):
    table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF' # 码表
    tr = {} # 反查码表
    # 初始化反查码表
    for i in range(58):
        tr[table[i]] = i
    s = [11, 10, 3, 8, 4, 6] # 位置编码表
    XOR = 177451812 # 固定异或值
    ADD = 8728348608 # 固定加法值
    r = 0
    for i in range(6):
        r += tr[x[s[i]]] * 58 ** i
    return (r - ADD) ^ XOR


# 用于获取视频状态
def FindVideo(avid):
    url = 'http://api.bilibili.com/archive_stat/stat?aid='+str(avid)  # 使用？携带参数
    rfv=get(url).json()
    json_str=dumps(rfv)
    data2=loads(json_str)
    data3=data2['code']
    return data3


def getFileName1(lpath,suffix):
    # 获取指定目录下的所有指定后缀的文件名 
    input_template_All=[]
    f_list = listdir(lpath)#返回文件名
    for i in f_list:
        # path.splitext():分离文件名与扩展名
        if path.splitext(i)[1] ==suffix:
           input_template_All.append(path.splitext(i)[0])
        #print(i)
    return input_template_All


def validateTitle(title):
	rstr = r"[\/\\\:\*\?\"\<\>\|]" # '/ \ : * ? " < > |'
	new_title = sub(rstr, "_", title).replace(" ","_") # 替换为下划线
	return new_title


def ngp(bvid): #B站获取视频信息的api
    url = 'http://api.bilibili.com/x/web-interface/view?bvid='+str(bvid)  # 使用？携带参数
    rsp=get(url).json()
    json_str=dumps(rsp)
    data2=loads(json_str)
    data3=data2['data']
    json_str1=dumps(data3)
    data4=loads(json_str1)
    fin=str(data4["videos"])
    return fin


def MultiVidieoDownload(BV,workDir,P):
    call("D:\\BilibiliDownloadTools\\BBDown_win-x64\\BBDown.exe "+BV+" -p "+P+" --work-dir "+workDir,shell=True)


def SingleVideoDownload(BV,workDir,P):
    # call("@echo off")
    mkdir(workDir)#"D:\BilibiliDownloadFile\Temporary")
    call("D:\\BilibiliDownloadTools\\BBDown_win-x64\\BBDown.exe "+BV+" -p "+P+" --work-dir "+workDir,shell=True)


def Compress(dirOf7z,fileNameFor7z,fileNameForAss,fileNameForXml,mx,mhe):
    call(dirOf7z+" a -t7z "+fileNameFor7z+" -mx="+mx+" -mhe="+mhe+" "+fileNameForAss+" "+fileNameForXml,shell=True)


if __name__ == '__main__':
    para2=str(1)
    para1 = input("请输入要下载视频的BV号: ")
    findVideo=bv2av(para1)
    findVideo=FindVideo(findVideo)
    if str(findVideo)=="0":
        if ngp(para1) == "1":
            para2=str(1)
        else:
            para2 = input("请输入下载视频的P数(如8 或1,2 或3-5 或ALL):")
        if "," in para2 or "-" in para2 or "ALL" in para2:
            try:
                MultiVidieoDownload(para1,"D:\\BilibiliDownloadFile",para2)
            except Exception as e1:
                print(e1)
        else:
            try:
                SingleVideoDownload(para1,"D:\\BilibiliDownloadFile\\Temporary",para2)
            except Exception as e:
                print(e)
                print("_________")
            Files=listdir("D:\\BilibiliDownloadFile\\Temporary")
            for k in range(len(Files)):
                Files[k]=path.splitext(Files[k])[1]# 提取文件夹内所有文件的后缀
            Str2=['.mp4']
            if len(list(set(Str2).intersection(set(Files))))==len(Str2):
                #有MP4
                fileName=getFileName1("D:\BilibiliDownloadFile\Temporary",".mp4")
                fileName=fileName[0]
                fileName=validateTitle(fileName)
                rename("D:\BilibiliDownloadFile\Temporary","D:\BilibiliDownloadFile\\"+fileName)
                try:
                    dirOf7z="\"C:\\Program Files\\7-Zip\\7z.exe\""
                    fileNameFor7z="D:\\BilibiliDownloadFile\\"+fileName+"\\DanmakuAndSubtitles.7z"
                    fileNameForAss="D:\\BilibiliDownloadFile\\"+fileName+"\\*.ass"
                    fileNameForXml="D:\\BilibiliDownloadFile\\"+fileName+"\\*.xml"
                    myPath="D:\\BilibiliDownloadFile\\"+fileName
                    mx="9"
                    mhe="on"
                    Compress(dirOf7z,fileNameFor7z,fileNameForAss,fileNameForXml,mx,mhe)
                    
                    assfileName=myPath+"\\"+getFileName1(myPath,".ass")[0]+".ass"
                    xmlfileName=myPath+"\\"+getFileName1(myPath,".xml")[0]+".xml"
                    remove(assfileName)
                    remove(xmlfileName)
                except Exception as e2:
                    print(e2)
    else:
        print("视频不存在！")
        sleep(1)