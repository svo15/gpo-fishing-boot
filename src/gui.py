import tkinter as tk
from tkinter import ttk
from time import sleep,time

class GUI():
    def __init__(self,root):
        self.root=root
        self.root.title('GPO Autofish')
        self.root.attributes('-topmost', True)
        self.root.geometry("400x400")

        self.main_frame=ttk.Frame(self.root)
        self.main_frame.grid()

        ttk.Button(self.main_frame,text="fishing-bot",command=self.fishing_setup).grid(column=0,row=0)
    def fishing_setup(self):
        import pyautogui

        pyautogui.click(x=960,y=540)
        pyautogui.scroll(-10)
        pyautogui.scroll(7)