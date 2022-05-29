
from tkinter import *
from pytube import YouTube

window = Tk()
window.iconbitmap(r"C:\Users\scuto\Desktop\Projects\YoutubeVideoDownloader\zaa.ico")
window.geometry('750x750')

window.title("YouTube Video Downloader")

lbl = Label(window,text="Video Linkini Yapıştırıp Butona Tıklayınız")

lbl.grid(column=5,row=10)

videolink = Entry(window,width=70)
videolink.grid(column=10,row=12)
abnf = videolink.get()

def downloaderr():
     yt = YouTube(videolink.get())
     yt.streams.get_highest_resolution().download(r"C:\Users\scuto\Desktop\Download")
     
     


btn = Button(window,text= "Click to Download",command=downloaderr)
btn.grid(column=10,row=15)
btn_quit = Button(window,text="Click for Close Application",command=window.destroy)
 
window.mainloop()




