# Disclaimer: I do not take any responsibility for usage of this script. Use at your own risk.

YourName = "John Smith"
FloodChatLineMessage = "AI Cat"

MessageBarX = 0
MessageBarY = 0

import tkinter as tk
from pystray import Icon, Menu, MenuItem
from PIL import Image
import threading
import pyautogui
import time

root = tk.Tk()

root.title("AI Cat")
root.geometry("550x200")

root.protocol("WM_DELETE_WINDOW", root.withdraw)

def Type(text):
    pyautogui.moveTo(MessageBarX, MessageBarY)
    pyautogui.click()
    pyautogui.typewrite(text, 0.01)
    time.sleep(0.01)
    pyautogui.press("Enter")
    time.sleep(0.1)

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

ConfigFrame = tk.LabelFrame(root, text="Configuration", padx=10, pady=10)
CommandsFrame = tk.LabelFrame(root, text="Commands", padx=10, pady=10)
AvailableButton = tk.Button(CommandsFrame, text="Available", command=Available)
BusyButton = tk.Button(CommandsFrame, text="Busy", command=Busy)
FloodButton = tk.Button(CommandsFrame, text="Flood Chat Lines", command=FloodChatLines)
SetPointButton = tk.Button(ConfigFrame, text="Set Message Box Point (Saves 5 seconds after)", command=SetPoint)
NameLabel = tk.Label(ConfigFrame, text="Enter Your Name")
NameInputBox = tk.Entry(ConfigFrame)
NameInputButton = tk.Button(ConfigFrame, text="Set Name", command=lambda: setattr(__import__('__main__'), 'YourName', NameInputBox.get()))
#HappyFaceButton = tk.Button(root, text=":)", command=HappyFace)

SetPointButton.pack()
NameLabel.pack()
NameInputBox.pack()
NameInputButton.pack()
AvailableButton.pack()
BusyButton.pack()
FloodButton.pack()
ConfigFrame.grid(padx=10, column=1, row=1)
CommandsFrame.grid(padx=10, column=0, row=1)

#HappyFaceButton.pack()

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