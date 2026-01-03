@echo off

echo Getting Dependencies...
pip install -r Dependencies.txt

echo Building Executable...
pyinstaller --onefile --windowed --add-data "icon.png;." main.py

echo Build Complete!
echo Thank you for using AI Cat
echo The build can be found in the 'dist' folder.
pause