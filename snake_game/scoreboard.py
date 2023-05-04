from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        with open("/Users/quoczuong/Udemy/Python/Code/FinalProject/snake_game/data.txt", "r") as file:
            self.high_score = int(file.read())

        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}     High Score: {self.high_score}", align="center",
                   font=("Arial", 25, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("/Users/quoczuong/Udemy/Python/Code/FinalProject/snake_game/data.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.clear()
    #     self.goto(0, -40)
    #     self.color("white")
    #     self.write(f"Game Over!\n", align="center",
    #                font=("Arial", 50, "normal"))
    #     self.write(f"Your score is {self.score}",
    #                align="center", font=("Arial", 40, "normal"))
