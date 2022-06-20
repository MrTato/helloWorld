from tkinter import *


def submit():
    print("The temperature is: " + str(scale.get()) + " degrees in C")


window = Tk()

hot_image = PhotoImage(file='like.png')
hot_label = Label(image=hot_image)
hot_label.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,
              tickinterval=10,
              showvalue=FALSE,
              resolution=5,
              troughcolor='#69EAFF',
              fg='#FF1C00',
              bg='#111111'
              )
scale.set(((scale['from'] - scale['to']) / 2) + scale['to'])
scale.pack()

cold_image = PhotoImage(file='like.png')
cold_label = Label(image=cold_image)
cold_label.pack()

button = Button(window, text='submit', command=submit)
button.pack()

window.mainloop()