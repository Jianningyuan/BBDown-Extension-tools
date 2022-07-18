from fileinput import filename
from os import system,listdir,path,rename
from re import sub

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
	new_title = sub(rstr, "_", title) # 替换为下划线
	return new_title


para1 = input("请输入要下载视频的BV号：")
para2 = input("请输入下载视频的P数(如8 或1,2 或3-5 或ALL):")
if "," in para2 or "-" in para2 or "ALL" in para2:
    try:
        rnp1 = "%s \"%s\" \"%s\" \"%s\""%("D:\BilibiliDownloadTools\pasparmu.bat",para1, para2,"D:\BilibiliDownloadFile")
        system(rnp1)
    except Exception as e1:
        print(e1)
else:
    try:
        rnp = "%s \"%s\" \"%s\" \"%s\""%("D:\BilibiliDownloadTools\paspar.bat",para1, para2,"D:\BilibiliDownloadFile\Temporary")#给paspar.bat传BV号及P数
        system(rnp)
    except Exception as e:
        print(e)
    Files=listdir("D:\BilibiliDownloadFile\Temporary")
    for k in range(len(Files)):
        Files[k]=path.splitext(Files[k])[1]# 提取文件夹内所有文件的后缀

    Str2=['.mp4']
    if len(list(set(Str2).intersection(set(Files))))==len(Str2):
        #有MP4
        fileName=getFileName1("D:\BilibiliDownloadFile\Temporary",".mp4")
        fileName=fileName[0]
        fileName=validateTitle(fileName)
        rename("D:\BilibiliDownloadFile\Temporary","D:\BilibiliDownloadFile\\"+fileName)
        fileNamefor7zroot="C:\\Program\000Files\\7-Zip\\7z.exe"
        fileNamefor7z="D:\\BilibiliDownloadFile\\"+fileName+"\\"+fileName+"DanmakuAndSubtitles.7z"
        fileNameforass="D:\\BilibiliDownloadFile\\"+fileName+"\\*.ass" + " D:\\BilibiliDownloadFile\\"+fileName+"\\*.xml"
        print(fileNamefor7zroot)
        print(fileNamefor7z)
        print(fileNameforass)

        #fileNameforxml=
        try:
            yasuo="%s \"%s\" \"%s\" \"%s\" \"%s\" \"%s\" \"%s\""%(fileNamefor7zroot,"a","-t7z",fileNamefor7z,"-mx=9","-mhe=on",fileNameforass)#,fileNameforxml)
            system(yasuo)
        except Exception as e2:
            print(e2)