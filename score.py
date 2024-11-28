from turtle import Turtle
class Score(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(position)
        self.hideturtle()
        self.score=0
        self.show_score()

    def show_score(self):
        self.write(f"{self.score}",font={"courier",40,"bold"})

    def increase_score(self):
        self.score+=1
        self.clear()
        self.show_score()

    




   