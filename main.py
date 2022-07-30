import tkinter as tk
import fnmatch
import os
from pygame import mixer
from tkinter import *
from tkinter import filedialog

window = tk.Tk()
window.title("Vilas's music player")
window.geometry("1000x800")
window.config(bg= "black")


pattern = "*.mp3"
mixer.init()

logo_image = PhotoImage(file = 'sample images\\unnamed.png')
prev_image = PhotoImage(file = r'sample images\back-button.png')
next_image = PhotoImage(file = r'sample images\next-button.png')
play_image = PhotoImage(file = 'sample images\play-button.png')
pause_image = PhotoImage(file = 'sample images\pause-button.png')
stop_image = PhotoImage(file = 'sample images\stop-button.png')

def select():
    currentsong.config(text=lb.get('anchor'))
    mixer.music.load(fn+'//'+lb.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    lb.select_clear('active')
    currentsong.config(text='')

def play_next():
    next_song = lb.curselection()
    next_song = next_song[0] + 1
    next_song_name = lb.get(next_song)
    currentsong.config(text = next_song_name)
    mixer.music.load(fn+'//'+next_song_name)
    mixer.music.play()

    lb.select_clear(0,'end')
    lb.activate(next_song)
    lb.select_set(next_song)

def play_prev():
    next_song = lb.curselection()
    next_song = next_song[0] - 1
    next_song_name = lb.get(next_song)
    currentsong.config(text = next_song_name)
    mixer.music.load(fn+'//'+next_song_name)
    mixer.music.play()

    lb.select_clear(0,'end')
    lb.activate(next_song)
    lb.select_set(next_song)


def browseFiles():
    global fn
    fn = filedialog.askdirectory()
    for root,dirs,files in os.walk(fn):
        for filename in fnmatch.filter(files,pattern):
            lb.insert('end',filename)


def pause_song():
    if pausebt["text"] == "Pause":
        mixer.music.pause()
        pausebt["text"] = "Play"
    else:
        mixer.music.unpause()
        pausebt["text"] = "Pause"


top = Frame(window,bg="black")
top.pack(padx=15,pady=5,anchor='center')
lb1 = Label(window,text="Music Player" ,font=("Tahoma",20),fg="lightblue",bg="black").pack(in_=top,side="bottom")
lb2 = Label(window,text="Music Player" ,font=("Tahoma",30),fg="white",bg="black",image = logo_image,relief="solid").pack(in_=top,side="top")



button_explore = Button(window,text = "Select music folder",font = ("Tahoma",13),fg="lightblue",bg="black",command = browseFiles)                                                        
button_explore.pack(pady=(40,20))

lb = tk.Listbox(window,fg = "lightblue",bg = "black",relief="solid",width =100 , font = ("Tahoma",15))
lb.pack(padx=50)

control = Frame(window,bg = "black")
control.pack(padx=15,pady=5,anchor='center')

prevbt = Button(window,text = "Prev",bg = "black",fg="white",font = ("Tahoma",10),image = prev_image,borderwidth=0,command=play_prev).pack(in_=control,padx=5,pady=10,side="left")
stopbt = Button(window,text = "Stop",bg = "black",fg="white",font = ("Tahoma",10),image = stop_image,borderwidth=0,command=stop).pack(in_=control,padx=5,pady=10,side="left")
pausebt = Button(window,text = "Pause",bg = "black",fg="white",font = ("Tahoma",10),image = pause_image,borderwidth=0,command=pause_song)
pausebt.pack(in_=control,padx=5,pady=10,side="left")
playbt = Button(window,text = "Play",bg = "black",fg="white",font = ("Tahoma",10),image = play_image,borderwidth=0,command=select).pack(in_=control,padx=5,pady=10,side="left")
nextbt = Button(window,text = "Next",bg = "black",fg="white",font = ("Tahoma",10),image = next_image,borderwidth=0,command=play_next).pack(in_=control,padx=5,pady=10,side="left")

currentsong = Label(window,text='',bg = "black",fg='lightblue',font = ("Tahoma",15))
currentsong.pack(pady=(25,25))

window.mainloop()