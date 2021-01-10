import tkinter as tk
from tkinter import *
from tkmacosx import *
from PIL import ImageTk, Image
import time
import connect


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

    def nextbtnhoveron(event):
        nextbtn.configure(fg="black")

    def nextbtnhoveroff(event):
        nextbtn.configure(fg="#6C63FF")

    def nextdone():
        name = databasename.get()
        tname = tablename.get()
        if len(name) < 1:
            errr.config(
                text="Database name is required.", bg="red")
        else:
            if len(tname) < 1:
                errr.config(
                    text="Table name is required.", bg="red")
            else:
                if connect.databaseexistcheck(name) == True:
                    errr.config(bg="red", text="A Database with name- '" +
                                name+"' already exists.")
                else:
                    connect.createdatabase(name)
                    if connect.tableexistcheck(tname, name) == True:
                        errr.config(bg="red", text="A Table with name- '" +
                                    tname+"' already exists.")
                    else:
                        def exitbtnhoveron(event):
                            exitbtn.configure(bg="white", fg="#6C63FF")

                        def exitbtnhoveroff(event):
                            exitbtn.configure(fg="white", bg="#6C63FF")
                        Label(window, image=img7).place(x=-2, y=-1)
                        exitbtn = Button(window, command=window.destroy, height=40, width=150,
                                         text="Exit", font=("Helvetica", 20, "bold"), bg="#6C63FF", fg="white")
                        exitbtn.bind("<Enter>", exitbtnhoveron)
                        exitbtn.bind("<Leave>", exitbtnhoveroff)
                        exitbtn.place(x=5, y=655)
                        Frame(window, width=150, height=4,
                              bg="#6C63FF").place(x=5, y=655)
                        Frame(window, width=150, height=4,
                              bg="#6C63FF").place(x=5, y=691)
                        Frame(window, width=4, height=40,
                              bg="#6C63FF").place(x=5, y=655)
                        Frame(window, width=4, height=40,
                              bg="#6C63FF").place(x=151, y=655)
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
    Label(window, text="Provide a name for your Database.",
          bg="#e8e6e9", font=("Helvetica", 40, "bold")).pack()
    Label(window, text="",
          bg="#e8e6e9", font=("Helvetica", 40, "bold")).pack()
    databasename = tk.Entry(window, justify='center', bd=3, fg="black",
                            font=("Helvetica", 30, "bold"))
    databasename.pack()
    Frame(window, width=350, height=4, bg="white").place(x=275, y=174)
    Frame(window, width=4, height=42, bg="white").place(x=275, y=174)
    Frame(window, width=4, height=42, bg="white").place(x=620, y=174)
    Frame(window, width=350, height=3, bg="black").place(x=275, y=216)
    Label(window, text="",
          bg="#e8e6e9", font=("Helvetica", 40, "bold")).pack()
    Label(window, text="Give a name to your table",
          bg="#e8e6e9", font=("Helvetica", 20, "bold")).pack()
    tablename = tk.Entry(window, justify='center', bd=3, fg="black",
                         font=("Helvetica", 30, "bold"))
    tablename.pack()
    Frame(window, width=350, height=4, bg="white").place(x=275, y=308)
    Frame(window, width=4, height=42, bg="white").place(x=275, y=308)
    Frame(window, width=4, height=42, bg="white").place(x=620, y=308)
    Frame(window, width=350, height=3, bg="black").place(x=275, y=350)
    Label(window, text="How many feilds do you need for your table.",
          bg="#e8e6e9", font=("Helvetica", 20, "bold")).pack()
    Label(window, text="",
          bg="#e8e6e9", font=("Helvetica", 40, "bold")).pack()
    variable = StringVar(window)
    variable.set(1)
    feildsize = OptionMenu(window, variable, 1, 2, 3, 4, 5,
                           6, 7, 8, 9, 10)
    feildsize.config(bg="#6C63FF")
    feildsize.pack(ipadx=50, ipady=10)
    nextbtn = Button(window, command=nextdone, height=40, width=200,
                     text="Next", font=("Helvetica", 20, "bold"), fg="#6C63FF", bg="white")
    nextbtn.bind("<Enter>", nextbtnhoveron)
    nextbtn.bind("<Leave>", nextbtnhoveroff)
    nextbtn.place(x=350, y=505)
    Frame(window, width=200, height=4, bg="white").place(x=350, y=505)
    Frame(window, width=4, height=40, bg="white").place(x=350, y=504)
    Frame(window, width=4, height=39, bg="white").place(x=546, y=505)
    Frame(window, width=200, height=4, bg="white").place(x=350, y=541)
    errr = Label(window, text="",
                 bg="white", font=("Helvetica", 12, "bold"))
    errr.pack()


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
img7 = ImageTk.PhotoImage(Image.open("bg7.png"))
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
