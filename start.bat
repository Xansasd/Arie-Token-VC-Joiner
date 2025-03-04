@echo off
title VC Spammer - ARİE
mode con: cols=80 lines=20
chcp 65001 >nul

:: Kırmızı renk için
color 04
cls

:: Animasyonlu ARİE yazısı
echo.
echo  ██████╗  ██████╗  ███╗   ███╗███████╗███████╗██████╗ 
echo  ██╔══██╗██╔═══██╗████╗ ████║██╔════╝██╔════╝██╔══██╗
echo  ██████╔╝██║   ██║██╔████╔██║███████╗█████╗  ██████╔╝
echo  ██╔═══╝ ██║   ██║██║╚██╔╝██║╚════██║██╔══╝  ██╔═══╝ 
echo  ██║     ╚██████╔╝██║ ╚═╝ ██║███████║███████╗██║     
echo  ╚═╝      ╚═════╝ ╚═╝     ╚═╝╚══════╝╚══════╝╚═╝     
timeout /t 2 >nul

:: Python scriptini başlat
python "os.py"
pause
