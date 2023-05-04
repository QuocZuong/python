from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title('Snake Game')
# dung de set hieu ung lien mach cho snake
screen.tracer(0)
# tim1 = Turtle("square")
# tim1.color("white")

# tim2 = Turtle("square")
# tim2.color("white")
# tim2.goto(-20, 0)

# tim3 = Turtle("square")
# tim3.color("white")
# tim3.goto(-40, 0)

snake = Snake()
food = Food()
title = Turtle()
title.hideturtle()
screen.listen()
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    screen.update()   # chạy xong hết rồi mới update hiện lên
    snake.move()
    time.sleep(0.1)
    # check xem khi con ran cham vao food bang ham distance
    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    # check khi con ran va vao tuong
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # su dung phan tu dau tien de loai bo viec thang thu hai nhay len thang dau
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            break

screen.exitonclick()
