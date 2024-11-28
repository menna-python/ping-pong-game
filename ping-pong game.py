from turtle import Screen
import turtle
from tkinter import *
from paddles import Paddles
from ball import Ball
from score import Score
import time

window=Screen()
window.title("ping-pong game")
window.bgcolor("black")
window.setup(width=800,height=600)

def on_close():
    global game_on
    game_on = False  # Stop the game loop
    try:
        window.bye()  # Close the Turtle graphics window
    except turtle.Terminator:
        pass 
window.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", on_close)

window.tracer(0)

r_paddle=Paddles((350,0))
l_paddle=Paddles((-350,0))
ball=Ball()
r_score=Score((370,250))
l_score=Score((-370,250))

window.listen()
window.onkey(r_paddle.up,"Up")
window.onkey(r_paddle.down,"Down")
window.onkey(l_paddle.up,"w")
window.onkey(l_paddle.down,"s")

ball.goto(-330,0)
default_sleep=0.07

game_on=True

while game_on:
   time.sleep(default_sleep)
   ball.goto(ball.xcor()+ball.ball_dx,ball.ycor()+ball.ball_dy)
   if ball.ycor()>=280 or ball.ycor()<=-280: 
      ball.ball_dy*=-1
      ball.goto(ball.xcor(),ball.ycor()+ball.ball_dy)

   if (ball.xcor()>=330 and ball.distance(r_paddle)<50) or (ball.xcor()<=-330 and ball.distance(l_paddle)<50):
      ball.ball_dx*=-1
      default_sleep*=0.9
      
   if ball.xcor()>400:
      ball.goto(0,0)
      ball.ball_dx*=-1
      default_sleep=0.07
      l_score.increase_score()
      
         
   if ball.xcor()<-400:
      ball.goto(0,0)
      ball.ball_dx*=-1
      default_sleep=0.07
      r_score.increase_score()

   window.update()



   

   
      


