from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle') # from Turtle module
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5) # normaly the turtle object is 20x20, with this we are changing it to 10x10
        self.color('red')
        self.speed('fastest')
        self.go_random_location()

    def go_random_location(self):
        random_x = random.randint(-200,200)
        random_y = random.randint(-200,200)
        self.goto(random_x,random_y)
