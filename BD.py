from os import system,listdir,path,rename

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

para1 = input("请输入要下载视频的BV号：")
para2 = input("请输入下载视频的P数(如8 或1,2 或3-5 或ALL):")
try:
    rnp = "%s \"%s\" \"%s\""%("D:\BilibiliDownloadTools\paspar.bat",para1, para2)#给paspar.bat传BV号及P数
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
    #print(fileName)
    rename("D:\BilibiliDownloadFile\Temporary","D:\BilibiliDownloadFile\\"+fileName)
else:
    #无mp4
    print("0")