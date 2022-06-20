from tkinter import *

window = Tk()

photo = PhotoImage(file='like.png')

label = Label(window,
              text="Hello World",
              font=('Arial', 40, 'bold'),
              fg='#00ff00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')
label.pack()  # places label at the center
# label.place(x=0, y=0)

window.mainloop()