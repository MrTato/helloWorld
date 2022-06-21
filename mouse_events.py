from tkinter import *


def do_something(event):
    print("You did a thing! " + str(event.x) + ", " + str(event.y))


window = Tk()

window.bind("<Button-1>", do_something)
window.bind("<Button-2>", do_something)
window.bind("<Button-3>", do_something)
window.bind("<ButtonRelease>", do_something)
window.bind("<Enter>", do_something)
window.bind("<Leave>", do_something)
window.bind("<Motion>", do_something)

window.mainloop()