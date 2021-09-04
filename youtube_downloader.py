from tkinter import *
from pytube import YouTube
from PIL import ImageTk,Image

root = Tk()

w = 500
h = 500
btn_w = 20
x_btn = (w-btn_w)/2
root.title("YouTube Downloader")
root.iconbitmap("icon.ico")
root.geometry(f"{w}x{h}")

#heading
heading = Label(root,text="KN's Downloader", font=("Arial Black",35)).place(relx = 0.5, rely = 0.2,anchor= "center")
#input
Label(root,text="Paste a youtube link here:",font = ("default",15)).place(relx = 0.5, rely = 0.4,anchor= "center")
input_url = Entry(root, width = 30, font=("default",20))
input_url.place(relx = 0.5, rely = 0.4,anchor= "center")

#radio buttons
v = IntVar()
choice = "video"
def radio_clicked():
	global choice
	
	if v.get() == 0:
		choice = "video"
	elif v.get() == 1:
		choice = "sound"


Radiobutton(root,text = "Video",font=("default",20),variable = v, value = 0,command = radio_clicked).place(relx = 0.1, rely = 0.6)
Radiobutton(root,text = "Sound",font=("default",20),variable = v, value = 1,command = radio_clicked).place(relx = 0.7, rely = 0.6)

#download button
def get_url():
	# if input_url.get() == "":
	# print(input_url.get())
btn = Button(root, text="Download",font=("Arial",15), width = btn_w, height = 2,command = get_url).place(relx = 0.5, rely = 0.9,anchor= "center")

root.mainloop()