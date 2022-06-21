from tkinter import *
import time

WIDTH = 500
HEIGHT = 500
xVelocity = 10
yVelocity = 6
window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

photo_image = PhotoImage(file='like.png')
my_image = canvas.create_image(0, 0, image=photo_image, anchor=NW)

image_width = photo_image.width()
image_height = photo_image.height()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if coordinates[0] >= WIDTH - image_width or coordinates[0] < 0:
        xVelocity *= -1
    if coordinates[1] >= HEIGHT - image_height or coordinates[1] < 0:
        yVelocity *= -1
    canvas.move(my_image, xVelocity, yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()