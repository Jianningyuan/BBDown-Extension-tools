from json import dumps, loads
from os import listdir, mkdir, path, remove, rename
from re import sub
from subprocess import call
from requests import get
import configparser as ConfigParser
from win32api import SetFileAttributes
from win32con import FILE_ATTRIBUTE_HIDDEN,FILE_ATTRIBUTE_NORMAL

def GetConfig(section, key):
    config = ConfigParser.ConfigParser()
    pathOfConfig = path.split(path.realpath(__file__))[0] + '/BD.config'
    config.read(pathOfConfig)
    return config.get(section, key)


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
    call(ConfigOfBBDown+" "+BV+" -p "+P+" --work-dir "+workDir,shell=True)


def SingleVideoDownload(BV,workDir,P):
    # call("@echo off")
    mkdir(workDir)#"D:\BilibiliDownloadFile\Temporary")
    SetFileAttributes(workDir,FILE_ATTRIBUTE_HIDDEN)
    call(ConfigOfBBDown+" "+BV+" -p "+P+" --work-dir "+workDir,shell=True)


def Compress(dirOf7z,fileNameFor7z,fileNameForAss,fileNameForXml,mx,mhe):
    call(dirOf7z+" a -t7z "+fileNameFor7z+" -mx="+mx+" -mhe="+mhe+" "+fileNameForAss+" "+fileNameForXml,shell=True)


def DownLoadInit(para1):
    findVideo=bv2av(para1)
    findVideo=FindVideo(findVideo)
    return findVideo


def DownLoad(para1,P):
    global ConfigOfBBDown
    ConfigOfBBDown=GetConfig("DefaultDirectory","BBDownDirectory")
    ConfigOfDownloadTheDefaultDirectory=GetConfig("DefaultDirectory","DownloadTheDefaultDirectory")
    ConfigOfDirectoryOf7z=GetConfig("DefaultDirectory","DirectoryOf7z")
    para2=str(1)
    findVideo=DownLoadInit(para1)
    if str(findVideo)=="0":
        if ngp(para1) == "1":
            para2=str(1)
            try:
                SingleVideoDownload(para1,ConfigOfDownloadTheDefaultDirectory+"Temporary",para2)
            except Exception as e:
                print(e)
            Files=listdir(ConfigOfDownloadTheDefaultDirectory+"Temporary")
            for k in range(len(Files)):
                Files[k]=path.splitext(Files[k])[1]# 提取文件夹内所有文件的后缀
            Str2=['.mp4']
            if len(list(set(Str2).intersection(set(Files))))==len(Str2):
                #有MP4
                fileName=getFileName1(ConfigOfDownloadTheDefaultDirectory+"Temporary",".mp4")
                fileName=fileName[0]
                fileName=validateTitle(fileName)
                rename(ConfigOfDownloadTheDefaultDirectory+"Temporary",ConfigOfDownloadTheDefaultDirectory+fileName)
                SetFileAttributes(ConfigOfDownloadTheDefaultDirectory+fileName,FILE_ATTRIBUTE_NORMAL)
                try:
                    dirOf7z=ConfigOfDirectoryOf7z
                    fileNameFor7z=ConfigOfDownloadTheDefaultDirectory+fileName+"\\DanmakuAndSubtitles.7z"
                    fileNameForAss=ConfigOfDownloadTheDefaultDirectory+fileName+"\\*.ass"
                    fileNameForXml=ConfigOfDownloadTheDefaultDirectory+fileName+"\\*.xml"
                    myPath=ConfigOfDownloadTheDefaultDirectory+fileName
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
            para2 = P
            try:
                MultiVidieoDownload(para1,ConfigOfDownloadTheDefaultDirectory,para2)
            except Exception as e1:
                print(e1)