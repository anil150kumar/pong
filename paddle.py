from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_position, y_position):
        super().__init__()
        self.x = x_position
        self.y = y_position
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(x_position, y_position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.x, new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.x, new_y)
