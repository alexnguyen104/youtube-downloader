from tkinter import *
from pytube import YouTube
from PIL import ImageTk,Image
import os
import os.path
root = Tk()

w = 500
h = 500
btn_w = 20
x_btn = (w-btn_w)/2
root.title("YouTube Downloader")
root.iconbitmap("icon.ico")
root.geometry(f"{w}x{h}")

#heading
heading = Label(root,text="KN's Downloader", font=("Arial Black",35)).place(relx = 0.5, rely = 0.15,anchor= "center")
#input
Label(root,text="Paste a youtube link here:",font = ("default",15)).place(relx = 0.5, rely = 0.3,anchor= "center")
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


Radiobutton(root,text = "VIDEO",font=("default",15),variable = v, value = 0,command = radio_clicked).place(relx = 0.1, rely = 0.45)
Radiobutton(root,text = "AUDIO",font=("default",15),variable = v, value = 1,command = radio_clicked).place(relx = 0.7, rely = 0.45)


Label(root,text="Paste file location here:",font = ("default",15)).place(relx = 0.5, rely = 0.625,anchor= "center")
location = Entry(root, width = 30, font=("default",20))
location.place(relx = 0.5,rely = 0.71,anchor = "center")

#download button

def get_url():
        global location

        url = input_url.get()
        check_dir = os.path.isdir(location.get())

        try:
                video_sound = YouTube(url)
        except Exception:
                alert = Label(root,text = "Invalid URL", font = ("default",18),fg = "red")
                alert.place(relx = 0.5, rely = 0.5, anchor="center")
                return
        if check_dir == True:
                if choice == "video":
                                video_sound = video_sound.streams.get_highest_resolution()
                        except Exception:
                                Label(root,text = "URL error, try again",width = 100, font = ("default",15),fg ="red").place(relx = 0.5, rely = 0.475, anchor = "center")
                        video_sound.download(location.get())

                elif choice == "sound":
                        try:
                                video_sound = video_sound.streams.filter(only_audio= True).first()
                        except Exception:
                                Label(root,text = "URL error, try again",width = 100, font = ("default",15),fg ="red").place(relx = 0.5, rely = 0.8, anchor = "center")
                        out_file = video_sound.download(location.get())
                        base, ext = os.path.splitext(out_file)
                        new_file = base + '.mp3'
                        os.rename(out_file, new_file)

                Label(root,text = "Successfully Dowloaded", font = ("default",15),fg ="green").place(relx = 0.5, rely = 0.8, anchor = "center")
        else:
                Label(root,text = "Invalid Location",width = 100, font = ("default",15),fg = "red").place(relx = 0.5, rely = 0.8, anchor = "center")


btn = Button(root, text="Download",font=("Arial",15), width = btn_w, height = 2,command = get_url).place(relx = 0.5, rely = 0.9,anchor= "center")

root.mainloop()
