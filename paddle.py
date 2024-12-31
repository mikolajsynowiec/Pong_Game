from turtle import Turtle

class Paddle:
    def __init__(self, position):
        self.paddle = Turtle()
        self.paddle.penup()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.goto(position)



    def xcor(self):
        return self.paddle.xcor()

    def ycor(self):
        return self.paddle.ycor()

    def go_up(self):
        new_y = self.ycor() + 20
        self.paddle.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.paddle.goto(self.xcor(), new_y)
