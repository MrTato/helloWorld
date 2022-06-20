from tkinter import *

window = Tk()
count = 0


def click():
    global count
    count += 1
    print(count)


photo = PhotoImage(file='like.png')

button = Button(window,
                text="click me!",
                command=click,
                font=('Comic Sans', 30),
                fg="#00ff00",
                bg="black",
                activeforeground="#00ff00",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound='top')
button.pack()

window.mainloop()
