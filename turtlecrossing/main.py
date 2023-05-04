from turtle import Turtle, Screen
from turtleClass import LittleTurtle
from scoreboard import ScoreBoard
import time
from car import Car

# set up screen
screen = Screen()
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.setup(height=600, width=800)
screen.tracer(0)

# create turtle & cars
turtle = LittleTurtle()
cars = Car()
screen.listen()
screen.onkey(turtle.move_forward, "w")
screen.onkey(turtle.move_backward, "s")

# create score board & cars
scoreboard = ScoreBoard()
cars.create_car()
# game!!!
game_is_on = True

time_to_create_car = 0
while game_is_on:
    time_to_create_car += 0.5
    cars.move()
    time.sleep(0.1)

    for car in cars.cars:
        if turtle.distance(car) < 20:
            screen.clear()
            scoreboard.game_over()
            game_is_on = False
            break

    if time_to_create_car % 5 == 0:
        cars.create_more_cars()

    if turtle.ycor() > 280:
        scoreboard.level_up()
        turtle.return_to_begin()
        cars.speed_up()

    screen.update()
screen.exitonclick()
