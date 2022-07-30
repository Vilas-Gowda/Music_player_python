import tkinter as tk
import fnmatch
import os
from pygame import mixer
from tkinter import *

window = tk.Tk()
window.title("Vilas's music player")
window.geometry("600x800")
window.config(bg= "black")

samplemusic = "sample music"
pattern = "*.mp3"
filename='/'
lb = tk.Listbox(window,fg = "black",width =100 , font = ("Tahoma",15))
lb.pack(padx=15,pady=100)

for root,dirs,files in os.walk(filename):
    for filename in fnmatch.filter(files,pattern):
        lb.insert('end',filename)

window.mainloop()