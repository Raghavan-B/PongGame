from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import ScoreBoard

screen = Screen()
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)


r_paddle=Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard=ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    ##Detecting Collision with wall:
    if abs(ball.ycor()) > 280:
        ball.bounce_y()

    ##Detecting Collision with paddle:
    if ball.distance(r_paddle) < 50 and abs(ball.xcor()) >320 or ball.distance(l_paddle )<50 :
        ball.bounce_x()

    ##Detecting when paddle misses:
    if ball.xcor() >380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
    
screen.exitonclick()