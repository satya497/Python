from tkinter import *
from random import randint

#uipath%123
root = Tk()
root.title("Balls")
root.resizable(True,False)
canvas = Canvas(root, width = 600, height = 600)
canvas.pack()

# create two ball objects and animate them
ball = canvas.create_oval(10,10,30,30, fill="red")
ball2 = canvas.create_oval(10,50,30,70, fill="green")
ball2 = canvas.create_oval(10,90,30,110, fill="green")
ball3 = canvas.create_oval(10,130,30,150, fill="black")

root.mainloop()