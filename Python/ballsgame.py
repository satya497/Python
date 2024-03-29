from tkinter import *
from random import randint

class Ball:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas
        self.ball = canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="red")

    def move_ball(self):
        deltax = randint(0,30)
        deltay = randint(0,30)
        self.canvas.move(self.ball, deltax, deltay)
        self.canvas.after(100, self.move_ball)

# initialize root Window and canvas
root = Tk()
root.title("Balls")
root.resizable(False,False)
canvas = Canvas(root, width = 600, height = 600)
canvas.pack()

# create two ball objects and animate them
ball1 = Ball(canvas, 10, 10, 30, 30)
ball2 = Ball(canvas, 10, 50, 30, 70)
ball3 = Ball(canvas, 10, 90, 30, 110)
ball1.move_ball()
ball2.move_ball()
ball3.move_ball()
root.mainloop()