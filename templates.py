import tkinter as tk
from tkinter import *
from tkmacosx import *
from PIL import ImageTk, Image
import time


def exitbtnhoveron(event):
    exitbtn.configure(bg="white", fg="#6C63FF")


def exitbtnhoveroff(event):
    exitbtn.configure(fg="white", bg="#6C63FF")


def createhoveron(event):
    createbtn.configure(image=img2)


def createhoveroff(event):
    createbtn.configure(image=img1)


def previewhoveron(event):
    previewbtn.configure(image=img4)


def previewhoveroff(event):
    previewbtn.configure(image=img3)


def createdatabase():
    def exitbtnhoveron(event):
        exitbtn.configure(bg="white", fg="#6C63FF")

    def exitbtnhoveroff(event):
        exitbtn.configure(fg="white", bg="#6C63FF")
    Label(window, image=img5).place(x=-2, y=-1)
    exitbtn = Button(window, command=window.destroy, height=40, width=150,
                     text="Exit", font=("Helvetica", 20, "bold"), bg="#6C63FF", fg="white")
    exitbtn.bind("<Enter>", exitbtnhoveron)
    exitbtn.bind("<Leave>", exitbtnhoveroff)
    exitbtn.place(x=5, y=655)
    Frame(window, width=150, height=4, bg="#6C63FF").place(x=5, y=655)
    Frame(window, width=150, height=4, bg="#6C63FF").place(x=5, y=691)
    Frame(window, width=4, height=40, bg="#6C63FF").place(x=5, y=655)
    Frame(window, width=4, height=40, bg="#6C63FF").place(x=151, y=655)


def previewdatabase():
    def exitbtnhoveron(event):
        exitbtn.configure(bg="white", fg="#6C63FF")

    def exitbtnhoveroff(event):
        exitbtn.configure(fg="white", bg="#6C63FF")
    Label(window, image=img6).place(x=-2, y=-1)
    exitbtn = Button(window, command=window.destroy, height=40, width=150,
                     text="Exit", font=("Helvetica", 20, "bold"), bg="#6C63FF", fg="white")
    exitbtn.bind("<Enter>", exitbtnhoveron)
    exitbtn.bind("<Leave>", exitbtnhoveroff)
    exitbtn.place(x=5, y=655)
    Frame(window, width=150, height=4, bg="#6C63FF").place(x=5, y=655)
    Frame(window, width=150, height=4, bg="#6C63FF").place(x=5, y=691)
    Frame(window, width=4, height=40, bg="#6C63FF").place(x=5, y=655)
    Frame(window, width=4, height=40, bg="#6C63FF").place(x=151, y=655)


window = tk.Tk()
window.title("OpenUI")
img0 = ImageTk.PhotoImage(Image.open("bg0.png"))
img1 = ImageTk.PhotoImage(Image.open("bg1.png"))
img2 = ImageTk.PhotoImage(Image.open("bg2.png"))
img3 = ImageTk.PhotoImage(Image.open("bg3.png"))
img4 = ImageTk.PhotoImage(Image.open("bg4.png"))
img5 = ImageTk.PhotoImage(Image.open("bg5.png"))
img6 = ImageTk.PhotoImage(Image.open("bg6.png"))
Label(window, image=img0).place(x=-2, y=-1)
window.resizable(False, False)
x_cordinate = int((window.winfo_screenwidth()/2) - (450))
y_cordinate = int((window.winfo_screenheight()/2) - (350))
window.geometry("{}x{}+{}+{}".format(900, 700, x_cordinate, y_cordinate))
exitbtn = Button(window, command=window.destroy, height=40, width=150,
                 text="Exit", font=("Helvetica", 20, "bold"), bg="#6C63FF", fg="white")
exitbtn.bind("<Enter>", exitbtnhoveron)
exitbtn.bind("<Leave>", exitbtnhoveroff)
exitbtn.place(x=20, y=640)
Frame(window, width=150, height=4, bg="#6C63FF").place(x=20, y=640)
Frame(window, width=150, height=4, bg="#6C63FF").place(x=20, y=676)
Frame(window, width=4, height=40, bg="#6C63FF").place(x=20, y=640)
Frame(window, width=4, height=40, bg="#6C63FF").place(x=166, y=640)
Frame(window, width=900, height=10,
      bg="#e8e6e9").pack()
Label(window, text="Stylish UI from the future for your Database",
      bg="#e8e6e9", font=("Helvetica", 40, "bold")).pack()
createbtn = Button(window, command=createdatabase,
                   width=280, height=220, image=img1)
createbtn.bind("<Enter>", createhoveron)
createbtn.bind("<Leave>", createhoveroff)
createbtn.place(x=140, y=140)
previewbtn = Button(window, command=previewdatabase,
                    width=280, height=220, image=img3)
previewbtn.bind("<Enter>", previewhoveron)
previewbtn.bind("<Leave>", previewhoveroff)
previewbtn.place(x=460, y=140)

window.mainloop()
