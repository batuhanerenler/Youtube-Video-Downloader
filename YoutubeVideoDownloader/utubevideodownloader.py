

from sqlite3 import Row
from tkinter import *
import tkinter
from pytube import YouTube
import wget
import threading
import time



window = Tk()
window.iconbitmap(r"C:\Users\scuto\Desktop\Projects\YoutubeVideoDownloader\zaa.ico")
window.geometry('1920x1080')

window.title("YouTube Video Downloader")

lbl = Label(window,text="Video Linkini Yapıştırıp Butona Tıklayınız")

lbl.grid(column=5,row=10)

videolink = Entry(window,width=70)
videolink.grid(column=10,row=12)

def takevid():
     yt = YouTube(videolink.get())
     titlee = yt.title
     lbl_title = Label(window,text="Video Name: "+titlee).place(x=250,y=250)

     
def downloaderr():
     yt = YouTube(videolink.get())
     yt.streams.get_highest_resolution().download(r"C:\Users\scuto\Desktop\Download")
    
         
     
btn = Button(window,text= "Click to Download",command=threading.Thread(target=downloaderr).start)
btn.grid(column=10,row=25)
btn_getvid = Button(window,text="Click to Get Video Info",command=threading.Thread(target=takevid).start)
btn_getvid.grid(column=10,row=28)
btn_quit = Button(window,text="Click for Close Application",command=window.destroy)
btn_quit.grid(column=20,row=20) 
window.mainloop()






