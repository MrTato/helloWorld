from tkinter import *

window = Tk()  # instantiate a window
window.geometry("420x420")
window.title("Bro Code first GUI program")

icon = PhotoImage(file='like.png')
window.iconphoto(True, icon)
window.config(background="#000000")

window.mainloop()  # place window on computer screen

