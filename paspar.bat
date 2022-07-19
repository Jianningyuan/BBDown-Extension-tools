@echo off
set bbdown_path=D:\BilibiliDownloadTools\BBDown_v1.4.8_20220127_win-x64
cd D:\BilibiliDownloadFile
rd Temporary
md D:\BilibiliDownloadFile\Temporary
%bbdown_path%\BBDown.exe %1 -p %2 --work-dir %3