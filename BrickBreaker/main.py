from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
screen = Screen()
screen.bgcolor("black")
screen.title("Brick Breaker")
screen.setup(width=1000, height=800)
screen.tracer(0)
paddle = Paddle()
ball = Ball()
screen.listen()
screen.onkey(paddle.left, "a")
screen.onkey(paddle.right, "d")

screen.onkey(paddle.left, "Left")
screen.onkey(paddle.right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.02)
    screen.update()
    ball.move()

    if ball.ycor() > 380 or ball.ycor() < -380 or ball.distance(paddle) < 45:
        ball.bounce()

    if ball.xcor() > 480 or ball.xcor() < -480:
        ball.collision()
screen.exitonclick()
