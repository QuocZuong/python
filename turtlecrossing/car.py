from turtle import Turtle
import random
COLOR = ["purple", "orange", "blue", "yellow", "red", "green"]
CARS = []

RANDOM_X = [-400, -390, -380, -370, -360, -350, -340, -330, -320, -310, -300, -290, -280, -270, -260, -250, -240, -230, -220, -210, -200, -190, -180, -170, -160, -150, -140, -130, -120, -110, -100, -90, -80, -70, -60, -
            50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400]
RANDOM_Y = [-250, -240, -230, -220, -210, -200, -190, -180, -170, -160, -150, -140, -130, -70, -60, -50, -40, -30, -
            20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]


class Car():
    def __init__(self):
        self.cars = []
        self.speed_of_car = 3

    def create_car(self):
        for _ in range(20):
            position = (RANDOM_X[random.randint(0, 80)],
                        RANDOM_Y[random.randint(0, 44)])
            car = Turtle("square")
            car.color(COLOR[random.randint(0, 5)])
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.penup()
            car.goto(position)
            car.setheading(180)
            self.cars.append(car)

    def create_more_cars(self):

        position = (RANDOM_X[random.randint(77, 80)],
                    RANDOM_Y[random.randint(0, 44)])
        car = Turtle("square")
        car.color(COLOR[random.randint(0, 5)])
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.penup()
        car.goto(position)
        car.setheading(180)
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.speed_of_car)

    def speed_up(self):
        self.speed_of_car += 2
