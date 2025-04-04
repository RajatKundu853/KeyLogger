@echo off
cd /d "%~dp0"

:: Open Command Prompt as Administrator, kill pythonw.exe, and display a message
powershell -Command "Start-Process cmd -ArgumentList '/k cd /d \"%CD%\" && taskkill /F /IM pythonw.exe && echo You can close the terminal.' -Verb RunAs"

exit
