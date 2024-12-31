from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from score_board import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_1.go_up,"Up")
screen.onkey(paddle_1.go_down, "Down")

screen.onkey(paddle_2.go_up, "w")
screen.onkey(paddle_2.go_down, "s")



game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(paddle_1.paddle) < 50 and ball.xcor() > 320) or (ball.distance(paddle_2.paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.add_point_1()


    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.add_point_2()






screen.exitonclick()