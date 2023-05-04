from turtle import Turtle, Screen
STARTING_POSITION = [(0, -230), (0, -240), (0, -250)]
MOVE_DISTANCE = 20


class Paddle:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # ham tao them segment khi an duoc food
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            # lấy vị trí của segment trước để segment sau chen vào chỗ đó
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.goto(1200, 1200)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    # test

    def up(self):
        self.head.forward(10)

    # test
    def down(self):
        self.head.backward(10)

    def right(self):
        self.head.right(90)

    def left(self):
        self.head.left(90)
