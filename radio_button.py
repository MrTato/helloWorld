from tkinter import *

food = ["pizza", "hamburger", "hotdog"]


def order():
    if x.get() == 0:
        print("You ordered pizza!")
    elif x.get() == 1:
        print("You ordered a hamburger!")
    elif x.get() == 2:
        print("You ordered a hotdog!")
    else:
        print("huh?")


window = Tk()

pizza_image = PhotoImage(file='like.png')
hamburger_image = PhotoImage(file='like.png')
hotdog_image = PhotoImage(file='like.png')
foodImages = [pizza_image, hamburger_image, hotdog_image]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],
                              variable=x,
                              value=index,
                              padx=25,
                              font=("Impact", 50),
                              image=foodImages[index],
                              compound='left',
                              indicatoron=FALSE,
                              width=675,
                              command=order,
                              )
    radiobutton.pack(anchor=W)

window.mainloop()
