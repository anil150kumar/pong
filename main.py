from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from  score import  Score

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("pong")
screen.tracer(0)

paddle_1 = Paddle(350, 0)
paddle_2 = Paddle(-350, 0)
ball = Ball()
score = Score()

is_game_on = True

while is_game_on:
    screen.update()
    screen.listen()
    time.sleep(ball.ball_speed)
    screen.onkey(paddle_1.go_up, "Up")
    screen.onkey(paddle_1.go_down, "Down")
    screen.onkey(paddle_2.go_up, "w")
    screen.onkey(paddle_2.go_down, "s")
    ball.move()

    # detect collision

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # detect collision with right paddles

    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_ball_position()
        score.left_score()

    if ball.xcor() < -380:
        ball.reset_ball_position()
        score.right_score()

screen.exitonclick()
