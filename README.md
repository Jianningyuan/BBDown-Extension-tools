# BBDown-Extension-tools
**一个可选功能完全没有的垃圾的BBDownGUI实现(可通过BBDown.config实现配置)，但有输入校验与文件自动整理功能，需要自行准备BBDown.exe**

- **请在程序根目录添加icon.ico文件，否则会报错**   
- 请自行修改BD.config文件：  
- **第一行不要改**   
- 第二行为BBDown.exe的路径(**可为相对路径或绝对路径**)   
- 第三行为下载的目标目录，请自行更改（**默认为C:\BilibiliDownloadFile**)  
- 第四行为7 zip的目录(**不支持WinRAR**)(**可以在这一行的等号后写False或等号后为空来不压缩，但等号前面要留下**)   

以下为一个BD.config的实例:   
  ```
  [DefaultDirectory]
  BBDownDirectory=BBDown_win-x64\BBDown.exe
  DownloadTheDefaultDirectory=D:\BilibiliDownloadFile\
  DirectoryOf7z=C:\Program Files\7-Zip\7z.exe
  ```

**不提供二进制文件**

## 感谢名单：
https://github.com/nilaoda/BBDown  
https://github.com/Jianningyuan/bilibili-API-collect
## 特别鸣谢：
由Microsoft提供的独立源代码编辑器  
**VSCode**  

![VSCode](https://user-images.githubusercontent.com/102419562/184617892-8f1d0fed-34b0-44cc-b7c3-cab19a5d23f6.png)
