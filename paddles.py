from turtle import Turtle
class Paddles(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=5,stretch_len=1)

    def up(self):
        self.goto(self.xcor(),self.ycor()+60)

    def down(self):
        self.goto(self.xcor(),self.ycor()-60)
        
