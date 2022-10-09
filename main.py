import turtle
import time
import pads
import ball
import score
from score import Score
from ball import Ball
from pads import Paddle
from turtle import Turtle, Screen
screen= Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title('CUP PONG')
screen.tracer(0)
paddy = Paddle()
screen.listen()
balls= Ball()
scoree=Score()
game= True
turn=True

while game == True:
    time.sleep(0.1)
    balls.move()
    screen.update()
    if balls.ycor()>250 or balls.ycor()<-250:
        balls.change()
    if balls.distance(paddy.paddle1)<50 and balls.xcor()>690:
        balls.bounce()
    if balls.distance(paddy.paddle2) < 50 and balls.xcor() <-690:
        balls.bounce()

    if balls.xcor()>700:
        balls.reeturn()
        balls.move()
        scoree.increase_scoree()
        if scoree.score2==5:

            scoree.finals()
            game = False

    if balls.xcor()<-700:
        balls.reeturn()
        balls.move()
        scoree.increase_score()
        if scoree.score1==5:

            scoree.finals()
            game = False



    screen.onkey(key='Up', fun=paddy.up)
    screen.onkey(key='Down', fun=paddy.down)

    screen.onkey(key='a', fun=paddy.up2)
    screen.onkey(key='s', fun=paddy.down2)

screen.exitonclick()
