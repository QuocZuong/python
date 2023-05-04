from turtle import Turtle


class LittleTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(0, -280)

    def move_forward(self):
        self.setheading(90)
        self.forward(10)

    def move_backward(self):
        self.setheading(270)
        self.forward(10)

    def return_to_begin(self):
        self.goto(0, -280)
