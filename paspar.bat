@echo off
set bbdown_path=D:\BilibiliDownloadTools\BBDown_win-x64
cd D:\BilibiliDownloadFile
rd Temporary
md D:\BilibiliDownloadFile\Temporary
%bbdown_path%\BBDown.exe %1 -p %2 --work-dir %3