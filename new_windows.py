from tkinter import *


def create_window():
    new_window = Tk()
    window.destroy()
    top_level_window = Toplevel()


window = Tk()

Button(window, text="create new window", command=create_window).pack()

window.mainloop()