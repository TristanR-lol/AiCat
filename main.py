# Disclaimer: I do not take any responsibility for usage of this script. Use at your own risk.

# Config
# Only A - Z and a - z and certain special characters for punctuation are available.
YourName = "Tristan Ranero"
FloodChatLineMessage = "AI Cat"

# Make sure to set theese coordinates based on your screen
MessageBarX = 1000
MessageBarY = 960

# Code
import tkinter as tk
from pystray import Icon, Menu, MenuItem
from PIL import Image
import threading
import pyautogui
import time
import ctypes

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
    "aicat.tristan.desktop"
)

root = tk.Tk()

root.title("AI Cat")
root.geometry("300x200")

root.protocol("WM_DELETE_WINDOW", root.withdraw)

# Commands

def Available():
    pyautogui.moveTo(MessageBarX, MessageBarY)
    pyautogui.click()
    pyautogui.typewrite("/available")
    pyautogui.press("Enter")
    pyautogui.click()
    pyautogui.typewrite("[ " + YourName + " set their status to *Available* ]")
    pyautogui.press("Enter")

def Busy():
    pyautogui.moveTo(MessageBarX, MessageBarY)
    pyautogui.click()
    pyautogui.typewrite("/busy")
    pyautogui.press("Enter")
    pyautogui.click()
    pyautogui.typewrite("[ " + YourName + " set their status to *Busy* ]")
    pyautogui.press("Enter")

def FloodChatLines():
    pyautogui.moveTo(MessageBarX, MessageBarY)
    pyautogui.click()
    pyautogui.typewrite("/AiCat FloodChatLines")
    pyautogui.press("Enter")

    for i in range(50):
        pyautogui.click()
        pyautogui.typewrite(FloodChatLineMessage)
        time.sleep(0.01)
        pyautogui.press("Enter")
    
    pyautogui.click()
    pyautogui.typewrite("Flooding Complete")
    pyautogui.press("Enter")

    


# Buttons

AvailableButton = tk.Button(root, text="Available", command=Available)
BusyButton = tk.Button(root, text="Busy", command=Busy)
FloodButton = tk.Button(root, text="Flood Chat Lines", command=FloodChatLines)

AvailableButton.pack()
BusyButton.pack()
FloodButton.pack()

def create_icon():
    image = Image.open("icon.png")
    
    menu = Menu(
        MenuItem('Run Commands', root.deiconify),
        MenuItem('Exit AI Cat', root.destroy)
    )

    icon = Icon("AI Cat", image, menu=menu)

    icon.run()

if __name__ == "__main__":
    tray_thread = threading.Thread(target=create_icon, daemon=True)
    tray_thread.start()

root.mainloop()