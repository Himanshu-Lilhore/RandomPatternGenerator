from tkinter import *
from random import randint


root = Tk()
width = 700
height = 700
root.geometry(f"{width}x{height}")
canvasWidget = Canvas(root, width=width, height=height - 80)
canvasWidget.grid()
colours = ["red", 'green', 'white', 'black', 'lime', 'brown', 'pink', 'grey', 'violet',
           'blue', 'cyan', 'yellow', 'magenta']


def rann():
    return randint(0, 700)


def perform():
    canvasWidget.configure(bg=colours[randint(0, len(colours) - 1)])
    for i in range(100):
        for i in range(randint(1, 5)):
            canvasWidget.create_line(
                rann(), rann(), rann(), rann(), fill=colours[randint(0, len(colours) - 1)], width=randint(1, 6))
        for i in range(randint(1, 5)):
            canvasWidget.create_oval(
                rann(), rann(), rann(), rann(), outline=colours[randint(0, len(colours) - 1)], width=randint(1, 5))


def clean():
    canvasWidget.delete("all")
    canvasWidget.configure(bg="white")


def changebg():
    canvasWidget.configure(bg=colours[randint(0, len(colours) - 1)])


Button(root, text="Draw", command=perform).grid(row=1, column=0)
Button(root, text="Clear", command=clean).grid(row=2, column=0)
Button(root, text="Change BG", command=changebg).grid(row=3, column=0)


root.mainloop()
