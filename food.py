from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.shapesize(0.5)
        self.color("red")
        self.penup()
        x_pos = random.randint(-260, 260)
        y_pos = random.randint(-260, 260)
        self.hideturtle()
        self.goto(x_pos, y_pos)
        self.showturtle()

    def refresh(self):
        x_pos = random.randint(-290, 290)
        y_pos = random.randint(-290, 290)
        self.hideturtle()
        self.goto(x_pos, y_pos)
        self.showturtle()