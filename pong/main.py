from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball=Ball()
scoreboard= Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



game_on = True

while game_on:

    time.sleep(ball.moving_speed)
    screen.update()
    ball.moving()

#detect collision with walls
    if ball.ycor()< -290 or ball.ycor() >290:
        ball.bounce_y()

#detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    elif ball.xcor() > 390:
        ball.reset()
        scoreboard.l_point()
    elif ball.xcor() < -390:
        ball.reset()
        scoreboard.r_point()




screen.exitonclick()