@echo off
echo Installing Dependencies...
pip install pyautogui pystray pillow
echo Installation Complete :D
echo Running AI Cat
TIMEOUT /T 3
start pythonw.exe main.py