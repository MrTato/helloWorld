from tkinter import *

window = Tk()

Label(window, text="Enter your info", font=("Arial", 25)).grid(row=0, column=0, columnspan=2)

Label(window, text="First name: ").grid(row=1, column=0)
Entry(window).grid(row=1, column=1)

Label(window, text="Last name: ").grid(row=2, column=0)
Entry(window).grid(row=2, column=1)

Label(window, text="email: ").grid(row=3, column=0)
Entry(window).grid(row=3, column=1)

Button(window, text="Submit").grid(row=4, column=0, columnspan=2)

window.mainloop()