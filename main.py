# Disclaimer: I do not take any responsibility for usage of this script. Use at your own risk.

import tkinter as tk
from pystray import Icon, Menu, MenuItem
from PIL import Image
import threading
import pyautogui
import time
import sys
import os

def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

YourName = "John Smith"
FloodChatLineMessage = "AI Cat"

MessageBarX = 0
MessageBarY = 0

root = tk.Tk()
root.title("AI Cat")
root.geometry("550x300")
root.configure(bg="#ccf2cd")


root.protocol("WM_DELETE_WINDOW", root.withdraw)


def Type(text):
    pyautogui.moveTo(MessageBarX, MessageBarY)
    pyautogui.click()
    pyautogui.typewrite(text, 0.01)
    time.sleep(0.01)
    pyautogui.press("enter")
    time.sleep(0.1)


def Available():
    Type("/available")
    Type("[ " + YourName + " set their status to *Available* ]")

def Busy():
    Type("/busy")
    Type("[ " + YourName + " set their status to *Busy* ]")

def Reset():
    Type("/reset")
    Type("[ " + YourName + " *Reset* their status ]")

def FloodChatLines():
    import tkinter as tk
from tkinter import messagebox

def show_warning():
    messagebox.showwarning(
        "Are you sure?",
        "Are you sure? This can harm your chat and you may have to delete it."
    )

root = tk.Tk()
root.title("Main Window")

btn = tk.Button(root, text="Click me", command=show_warning)
btn.pack(padx=20, pady=20)
Type("/AICat FloodChatLines")
    for _ in range(50):
        Type(FloodChatLineMessage)
    Type("Flooding Complete")
root.mainloop()

def SetPoint():
    time.sleep(5)
    global MessageBarX, MessageBarY
    MessageBarX, MessageBarY = pyautogui.position()
    pyautogui.click()
    pyautogui.click()
    pyautogui.typewrite("Messages will now send from this position :)", 0.05)

def SetName():
    global YourName
    YourName = NameInputBox.get()


ConfigFrame = tk.LabelFrame(root, text="Configuration", padx=10, pady=10, bg="#ccf2cd")
CommandsFrame = tk.LabelFrame(root, text="Commands", padx=10, pady=10, bg="#ccf2cd")

SetPointButton = tk.Button(
    ConfigFrame,
    text="Set Message Box Point (5s delay)",
    command=lambda: threading.Thread(target=SetPoint, daemon=True).start()
)

NameLabel = tk.Label(ConfigFrame, text="Enter Your Name", bg="#ccf2cd")
NameInputBox = tk.Entry(ConfigFrame)
NameInputButton = tk.Button(ConfigFrame, text="Set Name", command=SetName)

AvailableButton = tk.Button(CommandsFrame, text="Available", command=Available)
BusyButton = tk.Button(CommandsFrame, text="Busy", command=Busy)
ResetButton = tk.Button(CommandsFrame, text="Reset Status", command=Reset)
FloodButton = tk.Button(CommandsFrame, text="Flood Chat Lines", command=FloodChatLines)


SetPointButton.pack(pady=2)
NameLabel.pack()
NameInputBox.pack()
NameInputButton.pack(pady=5)


AvailableButton.pack(fill="x")
BusyButton.pack(fill="x")
ResetButton.pack(fill="x")
FloodButton.pack(fill="x")

ConfigFrame.grid(padx=10, pady=10, column=1, row=0)
CommandsFrame.grid(padx=10, pady=10, column=0, row=0)


def create_icon():
    image = Image.open(resource_path("icon.png"))

    menu = Menu(
        MenuItem("Open AI Cat", lambda: root.after(0, root.deiconify)),
        MenuItem("Exit AI Cat", lambda: root.after(0, root.destroy))
    )

    icon = Icon("AI Cat", image, "AI Cat", menu)
    icon.run_detached()


threading.Thread(target=create_icon, daemon=True).start()

root.mainloop()

