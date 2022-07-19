@echo off
set fileNamefor7z=D:\BilibiliDownloadFile\%1\DanmakuAndSubtitles.7z
set fileNameforass=D:\BilibiliDownloadFile\%1\*.ass
set fileNameforxml=D:\BilibiliDownloadFile\%1\*.xml

"C:\Program Files\7-Zip\7z.exe" a -t7z %fileNamefor7z% -mx=9 -mhe=on %fileNameforass%  %fileNameforxml%
del %fileNameforass%
del %fileNameforxml%