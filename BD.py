from os import system,listdir,path
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
    print("0")
else:
    print("1")