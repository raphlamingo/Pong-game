import turtle
from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.range=[0,1,2,3,4,5,6,7,8,9]
        self.penup()
        self.shape('circle')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('white')
        self.ymoves=10
        self.xmoves = 10

    def move(self):

        new_y= self.ycor() + self.ymoves
        new_x = self.xcor() + self.xmoves
        self.goto(new_x,new_y)
        self.speed(random.choice(self.range))

    def change(self):
        self.ymoves=-self.ymoves
        self.speed(random.choice(self.range))

    def bounce(self):
        self.xmoves=-self.xmoves
        self.speed(random.choice(self.range))

    def reeturn(self):
        self.goto(0,0)







