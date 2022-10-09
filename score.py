import turtle
from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.create()


    def create(self):
        self.scoree1= Turtle()
        self.scoree1.color("white")
        self.scoree1.penup()
        self.scoree1.goto(600, 250)
        self.scoree1.write(f"Score: {self.score1}", align='center', font=20)
        self.scoree1.hideturtle()

        self.scoree2= Turtle()
        self.scoree2.color("white")
        self.scoree2.penup()
        self.scoree2.goto(-600, 250)
        self.scoree2.write(f"Score: {self.score2}", align='center', font=20)
        self.scoree2.hideturtle()

    def increase_score(self):
        self.score1+=1
        self.scoree1.clear()
        self.scoree1.write(f"Score: {self.score1}", align='center', font=20)
        self.scoree2.write(f"Score: {self.score2}", align='center', font=20)

    def increase_scoree(self):
        self.score2 += 1
        self.scoree2.clear()
        self.scoree1.write(f"Score: {self.score1}", align='center', font=20)
        self.scoree2.write(f"Score: {self.score2}", align='center', font=20)

    def finals(self):
        self.clear()
        self.scoree2.clear()
        self.scoree1.clear()
        self.color("white")
        self.penup()
        self.hideturtle()

        self.write('GAME OVER')





