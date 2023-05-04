from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.hideturtle()
        self.penup()
        self.goto(-380, 255)
        self.display_level()

    def display_level(self):
        self.write(f"Level: {self.current_level}",
                   align="left", font=("Courier", 25, "normal"))

    def level_up(self):
        self.clear()
        self.current_level += 1
        self.display_level()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over!\n", align="center",
                   font=("Arial", 40, "normal"))
        self.write(f"Your level: {self.current_level}😍",
                   align="center", font=("Courier", 30, "normal"))
