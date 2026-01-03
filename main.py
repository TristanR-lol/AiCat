# Disclaimer: I do not take any responsibility for usage of this script. Use at your own risk.

YourName = "Jhon Smith"
FloodChatLineMessage = "AI Cat"

MessageBarX = 1000
MessageBarY = 960

ConfigDirectory = "C:\Program Files\AiCat"

import tkinter as tk
from pystray import Icon, Menu, MenuItem
from PIL import Image
import threading
import pyautogui
import time
import ctypes
import os

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
    "aicat.tristan.desktop"
)

root = tk.Tk()

root.title("AI Cat")
root.geometry("500x300")

root.protocol("WM_DELETE_WINDOW", root.withdraw)

def Type(text):
    pyautogui.moveTo(MessageBarX, MessageBarY)
    pyautogui.click()
    pyautogui.typewrite(text)
    time.sleep(0.01)
    pyautogui.press("Enter")

# Commands

def Available():
    Type("/available")
    Type("[ " + YourName + " set their status to *Available* ]")

def Busy():
    Type("/busy")
    Type("[ " + YourName + " set their status to *Busy* ]")

def FloodChatLines():
    Type("/AICat FloodChatLines")

    for i in range(50):
        Type(FloodChatLineMessage)

    Type("Flooding Complete")

def SetPoint():
    time.sleep(5)
    global MessageBarX, MessageBarY
    MessageBarX, MessageBarY = pyautogui.position()
    print("Set Message Box Point to: " + str(MessageBarX) + ", " + str(MessageBarY))
    pyautogui.click()
    pyautogui.click()
    pyautogui.typewrite("Messages will now send from this position :)", 0.05)

def HappyFace():
    pyautogui.moveTo(MessageBarX, MessageBarY)
    pyautogui.click()
    pyautogui.typewrite(": )")
    pyautogui.press(["left", "backspace"], interval=0)

# Buttons

AvailableButton = tk.Button(root, text="Available", command=Available)
BusyButton = tk.Button(root, text="Busy", command=Busy)
FloodButton = tk.Button(root, text="Flood Chat Lines", command=FloodChatLines)
SetPointButton = tk.Button(root, text="Set Message Box Point (Saves 5 seconds after)", command=SetPoint)
HappyFaceButton = tk.Button(root, text=":)", command=HappyFace)

SetPointButton.pack()
AvailableButton.pack()
BusyButton.pack()
FloodButton.pack()
HappyFaceButton.pack()

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