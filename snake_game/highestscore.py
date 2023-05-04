from turtle import Turtle


class HighestScore(Turtle):
    def __init__(self, highest_score):
        super().__init__()
        self.file = open("highest_score.txt", "r+")
        self.hideturtle()
        self.penup()

    def save(self, score):
        self.file.write(score)
        self.write(f"    Your highest score is {highest_score}", align="left", font=(
            "Arial", 20, "normal"))
