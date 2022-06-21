from tkinter import *


def open_file():
    print("File has been opened")


def save_file():
    print("File has been saved")


def cut():
    print("You cut some text!")


def copy():
    print("You copied some text!")


def paste():
    print("you pasted some text!")


window = Tk()

openImage = PhotoImage(file="like.png")
saveImage = PhotoImage(file="like.png")
exitImage = PhotoImage(file="like.png")

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=open_file, image=openImage, compound='left')
fileMenu.add_command(label="Save", command=save_file, image=saveImage, compound='left')
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit, image=exitImage, compound='left')

editMenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)

window.mainloop()